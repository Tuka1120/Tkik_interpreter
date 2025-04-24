# Generated from EnglishLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EnglishLangParser import EnglishLangParser
else:
    from EnglishLangParser import EnglishLangParser

# This class defines a complete listener for a parse tree produced by EnglishLangParser.
class EnglishLangListener(ParseTreeListener):

    # Enter a parse tree produced by EnglishLangParser#program.
    def enterProgram(self, ctx:EnglishLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#program.
    def exitProgram(self, ctx:EnglishLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#statement.
    def enterStatement(self, ctx:EnglishLangParser.StatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#statement.
    def exitStatement(self, ctx:EnglishLangParser.StatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#varDecl.
    def enterVarDecl(self, ctx:EnglishLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#varDecl.
    def exitVarDecl(self, ctx:EnglishLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#assignStmt.
    def enterAssignStmt(self, ctx:EnglishLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#assignStmt.
    def exitAssignStmt(self, ctx:EnglishLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#printStmt.
    def enterPrintStmt(self, ctx:EnglishLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#printStmt.
    def exitPrintStmt(self, ctx:EnglishLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#type.
    def enterType(self, ctx:EnglishLangParser.TypeContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#type.
    def exitType(self, ctx:EnglishLangParser.TypeContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#expression.
    def enterExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#expression.
    def exitExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass



del EnglishLangParser