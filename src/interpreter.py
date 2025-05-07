import sys
import os
from antlr4 import *

grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar')
sys.path.append(grammar_path)

from EnglishLangParser import EnglishLangParser
from EnglishLangParserVisitor import EnglishLangParserVisitor as EnglishLangVisitor


class Interpreter(EnglishLangVisitor):
    def __init__(self):
        self.variables = {}
        self.output_lines = []

    def visitProgram(self, ctx: EnglishLangParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)
        return self.output_lines

    def visitVariableDeclaration(self, ctx: EnglishLangParser.VariableDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.variables[name] = value

    def visitDisplayStatement(self, ctx: EnglishLangParser.DisplayStatementContext):
        values = []
        for part in ctx.displayPart():
            identifier = part.IDENTIFIER().getText()
            value = self.variables.get(identifier, f"<undefined {identifier}>")
            values.append(str(value))
        self.output_lines.append(" ".join(values))

    def visitExpression(self, ctx: EnglishLangParser.ExpressionContext):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.IDENTIFIER():
            return self.variables.get(ctx.IDENTIFIER().getText(), 0)
        # Extend this later to handle +, -, *, / etc.
    
 