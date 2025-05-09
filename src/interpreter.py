
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
        elif ctx.numExpression():
            return self.visit(ctx.numExpression())
        return 0

    def evaluateBinaryOp(self, left, right, op):
        if op == '+': return left + right
        elif op == '-': return left - right
        elif op == '*': return left * right
        elif op == '/': return left / right
        elif op == '%': return left % right
        else: raise Exception(f"Unknown operator {op}")

    def visitFunctionCall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        print(f"Function '{name}' called (args ignored in basic interpreter).")

    def visitExpression(self, ctx):
        if ctx.numExpression():
            return self.visit(ctx.numExpression())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.env.variables.get(name, 0)
        return None
