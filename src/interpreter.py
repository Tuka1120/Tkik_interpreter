
from antlr4 import *
from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from EnglishLangParserVisitor import EnglishLangParserVisitor

class Environment:
    def __init__(self):
        self.variables = {}
        self.functions = {}

class Interpreter(EnglishLangParserVisitor):
    def __init__(self):
        self.env = Environment()

    def visitProgram(self, ctx):
        output_lines = []
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is not None:
                output_lines.append(str(result))  # Only Display returns something
        return output_lines
    
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

        self.env.variables[name] = value
        return None


    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.global_scope[name] = value
        return None 

    def visitReassignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name not in self.env.variables:
            raise Exception(f"Variable '{name}' not defined.")
        value = self.visit(ctx.numExpression())
        if ctx.ADD_TO():
            self.env.variables[name] += value
        elif ctx.SUBTRACT_FROM():
            self.env.variables[name] -= value
        elif ctx.TIMES():
            self.env.variables[name] *= value
        elif ctx.DIVIDE_FROM():
            self.env.variables[name] /= value
        return self.env.variables[name]

    def visitDisplayStatement(self, ctx):
        expressions = ctx.expression()
        results = [self.visit(expr) for expr in expressions]
        print("DEBUG: Displaying", results)  
        return ' '.join(str(r) for r in results)


    def visitNumExpression(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
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
            return self.env.variables.get(name, 0)
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
        value = self.env.variables.get(name, False)
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
            # Check how many statements/blocks there are
            num_ifs = 1 + len(ctx.ELSE_IF())
            stmt_or_block = ctx.statement(num_ifs) or ctx.block(num_ifs)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        return None

    def visitLoopIfStatement(self, ctx):
        # Evaluate main IF condition
        if self.visit(ctx.boolExpression(0)):
            return self.visit(ctx.loopStatements(0)) if ctx.loopStatements(0) else self.visit(ctx.statement(0))

        # Check ELSE IF conditions
        for i in range(1, len(ctx.boolExpression())):
            if self.visit(ctx.boolExpression(i)):
                return self.visit(ctx.loopStatements(i)) if ctx.loopStatements(i) else self.visit(ctx.statement(i))

        # ELSE clause
        if ctx.ELSE():
            return self.visit(ctx.loopStatements(-1)) if ctx.loopStatements(-1) else self.visit(ctx.statement(-1))

        return None


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

    def visitFunctionCall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        print(f"Function '{name}' called (args ignored in basic interpreter).")

    def visitExpression(self, ctx):
        if ctx.numExpression():
            return self.visit(ctx.numExpression())
        elif ctx.boolExpression():
            return self.visit(ctx.boolExpression())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.env.variables.get(name, 0)
        return None
