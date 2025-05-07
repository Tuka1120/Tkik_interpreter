# Generated from EnglishLangParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EnglishLangParser import EnglishLangParser
else:
    from EnglishLangParser import EnglishLangParser

# This class defines a complete generic visitor for a parse tree produced by EnglishLangParser.

class EnglishLangParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnglishLangParser#program.
    def visitProgram(self, ctx:EnglishLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#statement.
    def visitStatement(self, ctx:EnglishLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:EnglishLangParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#typeAnnotation.
    def visitTypeAnnotation(self, ctx:EnglishLangParser.TypeAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:EnglishLangParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#functionCall.
    def visitFunctionCall(self, ctx:EnglishLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#returnStatement.
    def visitReturnStatement(self, ctx:EnglishLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#displayStatement.
    def visitDisplayStatement(self, ctx:EnglishLangParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#displayPart.
    def visitDisplayPart(self, ctx:EnglishLangParser.DisplayPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#ifStatement.
    def visitIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#whileStatement.
    def visitWhileStatement(self, ctx:EnglishLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#forEachStatement.
    def visitForEachStatement(self, ctx:EnglishLangParser.ForEachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#parameterList.
    def visitParameterList(self, ctx:EnglishLangParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#typedParameter.
    def visitTypedParameter(self, ctx:EnglishLangParser.TypedParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#argumentList.
    def visitArgumentList(self, ctx:EnglishLangParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#block.
    def visitBlock(self, ctx:EnglishLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#expression.
    def visitExpression(self, ctx:EnglishLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#condition.
    def visitCondition(self, ctx:EnglishLangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#comparisonOp.
    def visitComparisonOp(self, ctx:EnglishLangParser.ComparisonOpContext):
        return self.visitChildren(ctx)



del EnglishLangParser