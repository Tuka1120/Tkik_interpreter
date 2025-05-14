
from antlr4 import *
from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from EnglishLangParserVisitor import EnglishLangParserVisitor

class BreakStatement:
    pass

class FunctionReturn(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter(EnglishLangParserVisitor):
    def __init__(self):
        super().__init__()
        self.global_env = {}
        self.env_stack = [self.global_env]
        self.variables = {}
        self.functions = {}        
        self.output_lines = []
        self.call_stack = []

    def current_env(self):
        return self.env_stack[-1]

    def push_env(self):
        self.env_stack.append({})

    def pop_env(self):
        self.env_stack.pop()

    def set_var(self, name, value):
        env = self.current_env()
        env[name] = value

    def get_var(self, name):
        for env in reversed(self.env_stack):
            if name in env:
                return env[name]
        raise Exception(f"Variable '{name}' is not defined")

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt) 
        return self.output_lines

    def visitVariableDeclaration(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())

        type_ctx = ctx.typeAnnotation()
        declared_type = type_ctx.getText().lower() if type_ctx else "unknown"

        if declared_type == 'int':
            value = int(value) if isinstance(value, (int, float, str)) else 0
        elif declared_type == 'float':
            value = float(value) if isinstance(value, (int, float, str)) else 0.0
        elif declared_type == 'bool':
            if isinstance(value, str):
                value = value.lower() == 'true'
            else:
                value = bool(value)
        elif declared_type == 'string':
            value = str(value)
        elif declared_type == 'matrix':
            if not isinstance(value, list) or not all(isinstance(row, list) for row in value):
                raise Exception(f"Invalid matrix assignment to variable '{name}'")
        else:
            raise Exception(f"Unknown type '{declared_type}' for variable '{name}'")

        self.variables[name] = value
        return None

    def visitFunctionDeclaration(self, ctx):
        name = ctx.IDENTIFIER().getText()
        param_list = []

        if ctx.parameter():
            for typed_param in ctx.parameter().typedParameter():
                param_name = typed_param.IDENTIFIER().getText()
                param_list.append(param_name)

        body = ctx.block()
        self.functions[name] = {
            "params": param_list,
            "body": body
        }
        return None

    def visitFunctionCall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        print("New visitFunctionCall reached")

        if name not in self.functions:
            raise Exception(f"Function '{name}' is not defined")

        func = self.functions[name]
        if 'params' not in func or 'body' not in func:
            print("Functions dict:", self.functions)
            raise Exception(f"Function '{name}' is not properly defined")

        params = func['params']
        body = func['body']

        args = [self.visit(expr) for expr in ctx.expression()]
        if len(args) != len(params):
            raise Exception(f"Function '{name}' expects {len(params)} arguments, got {len(args)}")

        old_scope = self.variables.copy()

        for param, arg in zip(params, args):
            self.variables[param] = arg

        try:
            self.visit(body)
        except FunctionReturn as ret:
            self.variables = old_scope  
            return ret.value

        self.variables = old_scope  
        return None 

    
    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expression())
        raise FunctionReturn(value)


    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.global_scope[name] = value
        return None 

    def visitReassignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name not in self.variables:
            raise Exception(f"Variable '{name}' not defined.")
        value = self.visit(ctx.numExpression())
        if ctx.ADD_TO():
            self.variables[name] += value
        elif ctx.SUBTRACT_FROM():
            self.variables[name] -= value
        elif ctx.TIMES():
            self.variables[name] *= value
        elif ctx.DIVIDE_FROM():
            self.variables[name] /= value
        return self.variables[name]

    def visitDisplayStatement(self, ctx):
        expressions = ctx.expression()
        results = [self.visit(expr) for expr in expressions]
        display_output = ' '.join(str(r) for r in results)
        print("DEBUG: Displaying", results)
        self.output_lines.append(display_output)
        return display_output

    def visitNumExpression(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if op == '+':
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                else:
                    return left + right
            elif op == '-':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left - right
                else:
                    raise TypeError(f"Unsupported operand types for -: {type(left)} and {type(right)}")
        return self.visit(ctx.getChild(0))

    def visitTerm(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '%':
                return left % right
        return self.visit(ctx.getChild(0))

    def visitFactor(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.variables.get(name, 0)
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.numExpression():
            return self.visit(ctx.numExpression())
        return 0
    
    def visitNumComparison(self, ctx):
        left = self.visit(ctx.numExpression(0))
        right = self.visit(ctx.numExpression(1))
        op = ctx.comparisonOp().getText()
        return self.evaluateBinaryOp(left, right, op)

    def visitStringComparison(self, ctx):
        left = self.visit(ctx.stringExpression(0))
        right = self.visit(ctx.stringExpression(1))
        op = ctx.getChild(1).getText()
        return (left == right) if op == "==" else (left != right)

    def visitMatrixComparison(self, ctx):
        left = self.visit(ctx.matrixExpression(0))
        right = self.visit(ctx.matrixExpression(1))
        op = ctx.getChild(1).getText()
        return (left == right) if op == "==" else (left != right)

    def visitLogicBinary(self, ctx):
        left = self.visit(ctx.boolExpression(0))
        right = self.visit(ctx.boolExpression(1))
        op = ctx.getChild(1).getText()
        if op == "and":
            return bool(left) and bool(right)
        elif op == "or":
            return bool(left) or bool(right)
        else:
            raise Exception(f"Unsupported logical operator: {op}")

    def visitLogicParen(self, ctx):
        value = self.visit(ctx.boolExpression())
        if ctx.NOT():
            return not bool(value)
        return bool(value)

    def visitTrueLiteral(self, ctx):
        return True

    def visitFalseLiteral(self, ctx):
        return False

    def visitLogicIdentifier(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.variables.get(name, False)
        return not bool(value) if ctx.NOT() else bool(value)
    
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx):
        # If
        if self.visit(ctx.boolExpression(0)):
            stmt_or_block = ctx.statement(0) or ctx.block(0)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        # Else If
        for i in range(len(ctx.ELSE_IF())):
            if self.visit(ctx.boolExpression(i + 1)):
                stmt_or_block = ctx.statement(i + 1) or ctx.block(i + 1)
                if stmt_or_block:
                    return self.visit(stmt_or_block)

        # Else
        if ctx.ELSE():
            num_ifs = 1 + len(ctx.ELSE_IF())
            stmt_or_block = ctx.statement(num_ifs) or ctx.block(num_ifs)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        return None

    def visitLoopIfStatement(self, ctx):
        # Main IF condition
        if self.visit(ctx.boolExpression(0)):
            if ctx.loopStatements(0):
                return self.visit(ctx.loopStatements(0))
            elif ctx.statement(0):
                return self.visit(ctx.statement(0))

        # ELSE IFs
        for i in range(1, len(ctx.boolExpression())):
            if self.visit(ctx.boolExpression(i)):
                if ctx.loopStatements(i):
                    return self.visit(ctx.loopStatements(i))
                elif ctx.statement(i):
                    return self.visit(ctx.statement(i))

        # ELSE clause
        if ctx.ELSE():  # Check if ELSE exists
            idx = len(ctx.boolExpression())
            if len(ctx.loopStatements()) > idx:
                return self.visit(ctx.loopStatements(idx))
            elif len(ctx.statement()) > idx:
                return self.visit(ctx.statement(idx))

        return None

    def visitBreakStatement(self, ctx):
        return BreakStatement()
    
    def visitLoopStatements(self, ctx):
        if ctx.loopStatement():
            return self.visit(ctx.loopStatement())
        elif ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.reassignment():
            return self.visit(ctx.reassignment())
        elif ctx.functionDeclaration():
            return self.visit(ctx.functionDeclaration())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.loopIfStatement():
            return self.visit(ctx.loopIfStatement())
        elif ctx.block():
            return self.visit(ctx.block())
        elif ctx.displayStatement():
            return self.visit(ctx.displayStatement())


    def visitWhileLoop(self, ctx):
        while self.visit(ctx.boolExpression()):
            if ctx.LBRACE():
                for stmt in ctx.loopStatements():
                    self.visit(stmt)
            else:
                self.visit(ctx.statement())

    def visitForLoop(self, ctx):
        if ctx.forInit():
            self.visit(ctx.forInit())

        def condition():
            return self.visit(ctx.cond)

        def update():
            self.visit(ctx.forUpdate())

        if ctx.forBody().LBRACE():
            body_statements = ctx.forBody().loopStatements()
        else:
            body_statements = [ctx.forBody().statement()]

        while condition():
            for stmt in body_statements:
                self.visit(stmt)
            update()


    def evaluateBinaryOp(self, left, right, op):
        if op == '+': return left + right
        elif op == '-': return left - right
        elif op == '*': return left * right
        elif op == '/': return left / right
        elif op == '%': return left % right
        elif op == '<': return left < right
        elif op == '>': return left > right
        elif op == '==': return left == right
        elif op == '!=': return left != right
        elif op == '<=': return left <= right
        elif op == '>=': return left >= right
        else: raise Exception(f"Unknown operator {op}")

    def visitExpression(self, ctx):
        if ctx.numExpression():
            return self.visit(ctx.numExpression())
        elif ctx.boolExpression():
            return self.visit(ctx.boolExpression())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.variables.get(name, 0)
        return None
