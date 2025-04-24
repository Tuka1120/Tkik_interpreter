# Generated from EnglishLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EnglishLangParser import EnglishLangParser
else:
    from EnglishLangParser import EnglishLangParser

# This class defines a complete generic visitor for a parse tree produced by EnglishLangParser.

class EnglishLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnglishLangParser#program.
    def visitProgram(self, ctx:EnglishLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#statement.
    def visitStatement(self, ctx:EnglishLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#varDecl.
    def visitVarDecl(self, ctx:EnglishLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#assignStmt.
    def visitAssignStmt(self, ctx:EnglishLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#printStmt.
    def visitPrintStmt(self, ctx:EnglishLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#type.
    def visitType(self, ctx:EnglishLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#expression.
    def visitExpression(self, ctx:EnglishLangParser.ExpressionContext):
        return self.visitChildren(ctx)


class EvalVisitor(ParseTreeVisitor): 
    def __init__(self, variables):
        self.variables = variables

    def visitVarDecl(self, ctx):
        var_name = ctx.ID().getText()
        var_type = ctx.type().getText()
        print(f"Evaluating variable declaration: {var_name} of type {var_type}")
        self.variables[var_name] = var_type  # Store in the shared variables

del EnglishLangParser