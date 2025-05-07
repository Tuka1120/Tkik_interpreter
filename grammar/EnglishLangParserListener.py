# Generated from EnglishLangParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EnglishLangParser import EnglishLangParser
else:
    from EnglishLangParser import EnglishLangParser

# This class defines a complete listener for a parse tree produced by EnglishLangParser.
class EnglishLangParserListener(ParseTreeListener):

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


    # Enter a parse tree produced by EnglishLangParser#typeAnnotation.
    def enterTypeAnnotation(self, ctx:EnglishLangParser.TypeAnnotationContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#typeAnnotation.
    def exitTypeAnnotation(self, ctx:EnglishLangParser.TypeAnnotationContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:EnglishLangParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:EnglishLangParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#functionCall.
    def enterFunctionCall(self, ctx:EnglishLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#functionCall.
    def exitFunctionCall(self, ctx:EnglishLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#returnStatement.
    def enterReturnStatement(self, ctx:EnglishLangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#returnStatement.
    def exitReturnStatement(self, ctx:EnglishLangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#displayStatement.
    def enterDisplayStatement(self, ctx:EnglishLangParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#displayStatement.
    def exitDisplayStatement(self, ctx:EnglishLangParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#displayPart.
    def enterDisplayPart(self, ctx:EnglishLangParser.DisplayPartContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#displayPart.
    def exitDisplayPart(self, ctx:EnglishLangParser.DisplayPartContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#ifStatement.
    def enterIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#ifStatement.
    def exitIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#whileStatement.
    def enterWhileStatement(self, ctx:EnglishLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#whileStatement.
    def exitWhileStatement(self, ctx:EnglishLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#forEachStatement.
    def enterForEachStatement(self, ctx:EnglishLangParser.ForEachStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#forEachStatement.
    def exitForEachStatement(self, ctx:EnglishLangParser.ForEachStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#parameterList.
    def enterParameterList(self, ctx:EnglishLangParser.ParameterListContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#parameterList.
    def exitParameterList(self, ctx:EnglishLangParser.ParameterListContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#typedParameter.
    def enterTypedParameter(self, ctx:EnglishLangParser.TypedParameterContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#typedParameter.
    def exitTypedParameter(self, ctx:EnglishLangParser.TypedParameterContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#argumentList.
    def enterArgumentList(self, ctx:EnglishLangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#argumentList.
    def exitArgumentList(self, ctx:EnglishLangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#block.
    def enterBlock(self, ctx:EnglishLangParser.BlockContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#block.
    def exitBlock(self, ctx:EnglishLangParser.BlockContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#expression.
    def enterExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#expression.
    def exitExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#condition.
    def enterCondition(self, ctx:EnglishLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#condition.
    def exitCondition(self, ctx:EnglishLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#comparisonOp.
    def enterComparisonOp(self, ctx:EnglishLangParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#comparisonOp.
    def exitComparisonOp(self, ctx:EnglishLangParser.ComparisonOpContext):
        pass



del EnglishLangParser