from EnglishLangVisitor import EnglishLangVisitor
from EnglishLangParser import EnglishLangParser

class EvalVisitor(EnglishLangVisitor):
    def __init__(self, variables=None):
        if variables is None:
            self.variables = {}
        else:
            self.variables = variables


    def visitProgram(self, ctx: EnglishLangParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitStatement(self, ctx: EnglishLangParser.StatementContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.printStatement():
            return self.visit(ctx.printStatement())

    def visitVariableDeclaration(self, ctx: EnglishLangParser.VariableDeclarationContext):
        var_name = ctx.IDENTIFIER().getText()
        var_type = ctx.type_().getText()
        self.variables[var_name] = {"type": var_type, "value": None}
        return None

    def visitAssignment(self, ctx: EnglishLangParser.AssignmentContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        if var_name in self.variables:
            self.variables[var_name]["value"] = value
        else:
            raise Exception(f"Variable '{var_name}' not declared before assignment.")
        return None

    def visitPrintStatement(self, ctx: EnglishLangParser.PrintStatementContext):
        value = self.visit(ctx.expression())
        if isinstance(value, str):
            print(value)
        else:
            print(value)
        return None

    def visitExpression(self, ctx: EnglishLangParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            # binary operation: expr op expr
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == 'and':
                return left and right
            elif op == 'or':
                return left or right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
            elif op == '<':
                return left < right
            elif op == '>':
                return left > right
            elif op == '<=':
                return left <= right
            elif op == '>=':
                return left >= right
            else:
                raise Exception(f"Unsupported binary operator: {op}")

        elif ctx.getChildCount() == 2:
            # unary operation: not expr
            if ctx.getChild(0).getText() == 'not':
                return not self.visit(ctx.getChild(1))

        elif ctx.getChildCount() == 1:
            # literal or variable
            if ctx.NUMBER():
                return float(ctx.NUMBER().getText())
            elif ctx.BOOLEAN():
                return ctx.BOOLEAN().getText() == 'true'
            elif ctx.STRING():
                text = ctx.STRING().getText()
                return text[1:-1]  # remove surrounding quotes
            elif ctx.IDENTIFIER():
                var_name = ctx.IDENTIFIER().getText()
                if var_name in self.variables:
                    value = self.variables[var_name]["value"]
                    if value is None:
                        raise Exception(f"Variable '{var_name}' is declared but has no value.")
                    return value
                else:
                    raise Exception(f"Variable '{var_name}' not declared.")
        
        elif ctx.LPAREN() and ctx.RPAREN():
            # expression inside parentheses
            return self.visit(ctx.expression(0))

        return None

    def visitType(self, ctx: EnglishLangParser.TypeContext):
        return ctx.getText()
