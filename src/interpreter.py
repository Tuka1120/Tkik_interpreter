
from antlr4 import *
from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from EnglishLangParserVisitor import EnglishLangParserVisitor
import math


class BreakStatement:
    pass

class FunctionReturn(Exception):
    def __init__(self, value):
        self.value = value

class Scope:
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get_variable(name)
        else:
            raise Exception(f"Variable '{name}' not found in any scope")

class Interpreter(EnglishLangParserVisitor):
    def __init__(self):
        super().__init__()
        self.global_scope = Scope()
        self.current_scope = self.global_scope
        self.memory = {}
        self.variables = {}
        self.functions = {}        
        self.output_lines = []
        self.call_stack = []

    def push_env(self):
        self.current_scope = Scope(parent=self.current_scope)

    def pop_env(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
        else:
            raise Exception("Cannot pop global scope")

    def set_var(self, name, value):
        self.current_scope.set_variable(name, value)

    def get_var(self, name):
        return self.current_scope.get_variable(name)


    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is not None and not isinstance(result, BreakStatement):
                self.output_lines.append(str(result))
        return self.output_lines
    
    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        var_type = self.visit(ctx.typeIdentifier()) if ctx.typeIdentifier() else None

        if var_name not in self.memory:
            if var_type:
                self.memory[var_name] = self.cast_value(value, var_type)
            else:
                self.memory[var_name] = value
        else:
            self.memory[var_name] = value

        return self.memory[var_name]


    def visitVariableDeclaration(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())

        type_ctx = ctx.typeAnnotation()
        declared_type = type_ctx.getText().lower() if type_ctx else None

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
        elif declared_type is None:
            if isinstance(value, str):
                try:
                    value = float(value) if '.' in value else int(value)
                except:
                    pass  
        else:
            raise Exception(f"Unknown type '{declared_type}' for variable '{name}'")

        self.set_var(name, value)
        return None
    
    def lookup_variable(self, name):
        return self.current_scope.get_variable(name)

    def visitFunctionDeclaration(self, ctx):
        name = ctx.IDENTIFIER().getText()
        param_list = []

        if ctx.parameter():
            for typed_param in ctx.parameter().typedParameter():
                param_name = typed_param.IDENTIFIER().getText()
                param_list.append(param_name)

        body = ctx.blockStatement()
        self.functions[name] = {
            "params": param_list,
            "body": body
        }
        return None

    def visitFunctionCall(self, ctx):
        print("New visitFunctionCall reached")

        func_name = ctx.IDENTIFIER().getText()
        args = []

        if ctx.argumentList():
            for expr in ctx.argumentList().expression():
                arg_val = self.visit(expr)
                args.append(arg_val)

        print(f"Calling function: {func_name} with args: {args}")
        result = self.callFunction(func_name, args)
        return result        

    def callFunction(self, name, args):
        func = self.functions[name]
        param_names = func["params"]
        body = func["body"]

        if len(param_names) != len(args):
            raise Exception(f"Function '{name}' expects {len(param_names)} args, got {len(args)}")

        local_scope = Scope(parent=self.current_scope)
        for pname, arg in zip(param_names, args):
            local_scope.set_variable(pname, arg)

        self.current_scope = local_scope

        try:
            self.visit(body)
        except FunctionReturn as fr:
            return_value = fr.value
        else:
            return_value = None
        finally:
            self.current_scope = self.current_scope.parent

        print(f"Function {name} returned: {return_value}")
        return return_value
    
    def visitBuiltInFunctions(self, ctx):
        if ctx.POWER_FUNC():
            base = self.visit(ctx.numExpression(0))
            exponent = self.visit(ctx.numExpression(1))
            return math.pow(base, exponent)

        elif ctx.SIN_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.sin(value)

        elif ctx.COS_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.cos(value)

        elif ctx.TAN_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.tan(value)

        elif ctx.CTAN_FUNC():
            value = self.visit(ctx.numExpression(0))
            tan_val = math.tan(value)
            if tan_val == 0:
                raise ZeroDivisionError("Cotangent undefined: tan(value) = 0")
            return 1 / tan_val

        else:
            raise Exception("Unknown built-in function")


    def visitIdentifier(self, ctx):
        var_name = ctx.getText()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise Exception(f"Undefined variable: {var_name}")
        
    def visitScopedIdentifier(self, ctx):
        levels = len(ctx.getTokens(EnglishLangParser.PARENT_SCOPE))
        name = ctx.IDENTIFIER().getText()
        current_scope = self.current_scope
        for _ in range(levels):
            if current_scope.parent is None:
                raise Exception(f"No parent scope exists while resolving 'parent::{name}'")
            current_scope = current_scope.parent

        value = current_scope.get_variable(name)
        if value is None:
            raise Exception(f"Variable '{name}' not found in the specified parent scope")
        return value
    
    def visitBlockStatement(self, ctx):
        self.push_env()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.pop_env()

    
    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expression())
        raise FunctionReturn(value)

    def visitStatement(self, ctx):
        result = self.visitChildren(ctx)

        if ctx.functionCall() and result is not None:
            print("DEBUG: Standalone function call result:", result)
            self.output_lines.append(f"Result: {result}")

        return result

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
        return None

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

    def visitUnaryPlus(self, ctx):
        return +self.visit(ctx.factor())

    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.factor())

    def visitFactorNumber(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitFactorIdentifier(self, ctx):
        name = ctx.IDENTIFIER().getText()
        return self.lookup_variable(name)

    def visitFactorString(self, ctx):
        return ctx.STRING().getText().strip('"')

    def visitFactorParens(self, ctx):
        return self.visit(ctx.numExpression())

    def visitFactorFunctionCall(self, ctx):
        return self.visit(ctx.functionCall())

    def visitFactorOperation(self, ctx):
        return self.visit(ctx.operation())
    
    def visitFactorscopedIdentifier(self, ctx):
        return self.visit(ctx.scopedIdentifier())

    def visitOperation(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        if var_name not in self.memory:
            raise Exception(f"Variable '{var_name}' not defined.")

        current_value = self.memory[var_name]
        if not isinstance(current_value, (int, float)):
            raise Exception(f"Cannot increment/decrement non-numeric variable '{var_name}'.")

        if ctx.INCREMENT():
            self.memory[var_name] = current_value + 1
        elif ctx.DECREMENT():
            self.memory[var_name] = current_value - 1

        return self.memory[var_name]
    
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

    def transpose_matrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def invert_matrix(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise Exception("Only 2x2 matrix inversion supported")

        a, b = matrix[0]
        c, d = matrix[1]
        determinant = a * d - b * c

        if determinant == 0:
            raise Exception("Matrix is not invertible")

        inverse = [
            [d / determinant, -b / determinant],
            [-c / determinant, a / determinant]
        ]
        return inverse

    def visitMatrixExpression(self, ctx):
        matrix = self.visit(ctx.matrixAtom())

        if ctx.INVERT_MATRIX():
            return self.invert_matrix(matrix)

        if ctx.TRANSPOSITION():
            return self.transpose_matrix(matrix)

        return matrix

    def visitMatrixAtom(self, ctx):
        if ctx.IDENTIFIER():
            return self.lookup_variable(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.matrixConstruction())

    def visitMatrixConstruction(self, ctx):
        rows = []
        for rowCtx in ctx.row():
            row = [self.visit(value) for value in rowCtx.value()]
            rows.append(row)
            print("DEBUG row:", row)
        return rows

    def visitValue(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.IDENTIFIER():
            value = self.lookup_variable(ctx.IDENTIFIER().getText())
            if isinstance(value, list) and any(isinstance(row, list) for row in value):
                raise Exception("Matrix cannot contain another matrix as an element")
            return value
        elif ctx.matrixExpression():
            raise Exception("Matrix cannot contain another matrix as an element")
        else:
            raise Exception("Invalid matrix value: must be a number or scalar variable")

    def visitBoolExpression(self, ctx):
        return self.visitChildren(ctx)

    def visitLogicOr(self, ctx):
        for i in range(len(ctx.boolAndExpression())):
            if self.visit(ctx.boolAndExpression(i)):
                return True
        return False

    def visitLogicAnd(self, ctx):
        for i in range(len(ctx.boolNotExpression())):
            if not self.visit(ctx.boolNotExpression(i)):
                return False
        return True

    def visitLogicNot(self, ctx):
        return not self.visit(ctx.boolNotExpression())

    def visitLogicPrimaryWrap(self, ctx):
        return self.visit(ctx.boolPrimary())

    def visitLogicParen(self, ctx):
        return self.visit(ctx.boolExpression())

    def visitTrueLiteral(self, ctx):
        return True

    def visitFalseLiteral(self, ctx):
        return False

    def visitLogicIdentifier(self, ctx):
        name = ctx.IDENTIFIER().getText()
        return bool(self.lookup_variable(name))

    def visitIfStatement(self, ctx):
        if self.visit(ctx.boolExpression(0)):
            stmt_or_block = ctx.statement(0) or ctx.blockStatement(0)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        for i in range(len(ctx.ELSE_IF())):
            if self.visit(ctx.boolExpression(i + 1)):
                stmt_or_block = ctx.statement(i + 1) or ctx.blockStatement(i + 1)
                if stmt_or_block:
                    return self.visit(stmt_or_block)

        if ctx.ELSE():
            num_ifs = 1 + len(ctx.ELSE_IF())
            stmt_or_block = ctx.statement(num_ifs) or ctx.blockStatement(num_ifs)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        return None


    def visitLoopIfStatement(self, ctx):
        if self.visit(ctx.boolExpression(0)):
            if ctx.loopStatements(0):
                return self.visit(ctx.loopStatements(0))
            elif ctx.statement(0):
                return self.visit(ctx.statement(0))

        for i in range(1, len(ctx.boolExpression())):
            if self.visit(ctx.boolExpression(i)):
                if ctx.loopStatements(i):
                    return self.visit(ctx.loopStatements(i))
                elif ctx.statement(i):
                    return self.visit(ctx.statement(i))

        if ctx.ELSE(): 
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
        elif ctx.blockStatement():
            return self.visit(ctx.blockStatement())
        elif ctx.displayStatement():
            return self.visit(ctx.displayStatement())


    def visitWhileLoop(self, ctx):
        self.push_env()
        try:
            while self.visit(ctx.boolExpression()):
                if ctx.LBRACE():
                    for stmt in ctx.loopStatements():
                        self.visit(stmt)
                else:
                    self.visit(ctx.statement())
        finally:
            self.pop_env()

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
        self.push_env()
        try:
            while condition():
                for stmt in body_statements:
                    self.visit(stmt)
                update()
        finally:
            self.pop_env()

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
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.builtInFunctions():
            return self.visit(ctx.builtInFunctions())
        elif ctx.matrixExpression():
            return self.visit(ctx.matrixExpression())
        elif ctx.stringExpression():
            return self.visit(ctx.stringExpression())
        elif ctx.scopedIdentifier():
            return self.visit(ctx.scopedIdentifier())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.lookup_variable(name)
        return None
