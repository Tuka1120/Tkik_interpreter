
from EnglishLangParserVisitor import EnglishLangParserVisitor
from EnglishLangParser import EnglishLangParser

class Evaluator(EnglishLangParserVisitor):
    def __init__(self, variables):
        self.variables = variables
        self.values = {}

    def visitAssignStmt(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise Exception(f"Undeclared variable '{var_name}'")
        value = self.visit(ctx.expr())
        self.values[var_name] = value

    def visitPrintStmt(self, ctx):
        print(ctx.STRING().getText()[1:-1])

    def visitExpr(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.values:
                raise Exception(f"Variable '{name}' used before assignment")
            return self.values[name]
        elif ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == 'true'
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1)) if len(ctx.expr()) > 1 else None
            op = ctx.op.text
            if op in ('add', 'plus'):
                return left + right
            elif op in ('subtract', 'minus'):
                return left - right
            elif op in ('multiply', 'times'):
                return left * right
            elif op in ('divide', 'over'):
                return left / right
            elif op == 'and':
                return left and right
            elif op == 'or':
                return left or right
            elif op == 'is':
                return left == right
            elif op == 'is not':
                return left != right
            elif op == 'less than':
                return left < right
            elif op == 'greater than':
                return left > right
        elif ctx.getChild(0).getText() == 'not':
            return not self.visit(ctx.expr(0))
        elif ctx.expr():
            return self.visit(ctx.expr(0))
        return None
