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


    # Enter a parse tree produced by EnglishLangParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:EnglishLangParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:EnglishLangParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#assignment.
    def enterAssignment(self, ctx:EnglishLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#assignment.
    def exitAssignment(self, ctx:EnglishLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#loopStatement.
    def enterLoopStatement(self, ctx:EnglishLangParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#loopStatement.
    def exitLoopStatement(self, ctx:EnglishLangParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#whileLoop.
    def enterWhileLoop(self, ctx:EnglishLangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#whileLoop.
    def exitWhileLoop(self, ctx:EnglishLangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#printStatement.
    def enterPrintStatement(self, ctx:EnglishLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#printStatement.
    def exitPrintStatement(self, ctx:EnglishLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#expressionStatement.
    def enterExpressionStatement(self, ctx:EnglishLangParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#expressionStatement.
    def exitExpressionStatement(self, ctx:EnglishLangParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#expression.
    def enterExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#expression.
    def exitExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#logicExpr.
    def enterLogicExpr(self, ctx:EnglishLangParser.LogicExprContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#logicExpr.
    def exitLogicExpr(self, ctx:EnglishLangParser.LogicExprContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#compareExpr.
    def enterCompareExpr(self, ctx:EnglishLangParser.CompareExprContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#compareExpr.
    def exitCompareExpr(self, ctx:EnglishLangParser.CompareExprContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#addExpr.
    def enterAddExpr(self, ctx:EnglishLangParser.AddExprContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#addExpr.
    def exitAddExpr(self, ctx:EnglishLangParser.AddExprContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#mulExpr.
    def enterMulExpr(self, ctx:EnglishLangParser.MulExprContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#mulExpr.
    def exitMulExpr(self, ctx:EnglishLangParser.MulExprContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#unaryExpr.
    def enterUnaryExpr(self, ctx:EnglishLangParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#unaryExpr.
    def exitUnaryExpr(self, ctx:EnglishLangParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:EnglishLangParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:EnglishLangParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#type.
    def enterType(self, ctx:EnglishLangParser.TypeContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#type.
    def exitType(self, ctx:EnglishLangParser.TypeContext):
        pass

del EnglishLangParser