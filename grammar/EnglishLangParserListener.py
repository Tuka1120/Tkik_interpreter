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


    # Enter a parse tree produced by EnglishLangParser#loopStatements.
    def enterLoopStatements(self, ctx:EnglishLangParser.LoopStatementsContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#loopStatements.
    def exitLoopStatements(self, ctx:EnglishLangParser.LoopStatementsContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:EnglishLangParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:EnglishLangParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#matrixExpression.
    def enterMatrixExpression(self, ctx:EnglishLangParser.MatrixExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#matrixExpression.
    def exitMatrixExpression(self, ctx:EnglishLangParser.MatrixExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#matrixAtom.
    def enterMatrixAtom(self, ctx:EnglishLangParser.MatrixAtomContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#matrixAtom.
    def exitMatrixAtom(self, ctx:EnglishLangParser.MatrixAtomContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#matrixConstruction.
    def enterMatrixConstruction(self, ctx:EnglishLangParser.MatrixConstructionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#matrixConstruction.
    def exitMatrixConstruction(self, ctx:EnglishLangParser.MatrixConstructionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#row.
    def enterRow(self, ctx:EnglishLangParser.RowContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#row.
    def exitRow(self, ctx:EnglishLangParser.RowContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#value.
    def enterValue(self, ctx:EnglishLangParser.ValueContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#value.
    def exitValue(self, ctx:EnglishLangParser.ValueContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#stringExpression.
    def enterStringExpression(self, ctx:EnglishLangParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#stringExpression.
    def exitStringExpression(self, ctx:EnglishLangParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#expression.
    def enterExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#expression.
    def exitExpression(self, ctx:EnglishLangParser.ExpressionContext):
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


    # Enter a parse tree produced by EnglishLangParser#parameter.
    def enterParameter(self, ctx:EnglishLangParser.ParameterContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#parameter.
    def exitParameter(self, ctx:EnglishLangParser.ParameterContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#typedParameter.
    def enterTypedParameter(self, ctx:EnglishLangParser.TypedParameterContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#typedParameter.
    def exitTypedParameter(self, ctx:EnglishLangParser.TypedParameterContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#returnStatement.
    def enterReturnStatement(self, ctx:EnglishLangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#returnStatement.
    def exitReturnStatement(self, ctx:EnglishLangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#functionCall.
    def enterFunctionCall(self, ctx:EnglishLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#functionCall.
    def exitFunctionCall(self, ctx:EnglishLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#argumentList.
    def enterArgumentList(self, ctx:EnglishLangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#argumentList.
    def exitArgumentList(self, ctx:EnglishLangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#builtInFunctions.
    def enterBuiltInFunctions(self, ctx:EnglishLangParser.BuiltInFunctionsContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#builtInFunctions.
    def exitBuiltInFunctions(self, ctx:EnglishLangParser.BuiltInFunctionsContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#ifStatement.
    def enterIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#ifStatement.
    def exitIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#loopIfStatement.
    def enterLoopIfStatement(self, ctx:EnglishLangParser.LoopIfStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#loopIfStatement.
    def exitLoopIfStatement(self, ctx:EnglishLangParser.LoopIfStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#loopStatement.
    def enterLoopStatement(self, ctx:EnglishLangParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#loopStatement.
    def exitLoopStatement(self, ctx:EnglishLangParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#forLoop.
    def enterForLoop(self, ctx:EnglishLangParser.ForLoopContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#forLoop.
    def exitForLoop(self, ctx:EnglishLangParser.ForLoopContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#forInit.
    def enterForInit(self, ctx:EnglishLangParser.ForInitContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#forInit.
    def exitForInit(self, ctx:EnglishLangParser.ForInitContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#forUpdate.
    def enterForUpdate(self, ctx:EnglishLangParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#forUpdate.
    def exitForUpdate(self, ctx:EnglishLangParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#forBody.
    def enterForBody(self, ctx:EnglishLangParser.ForBodyContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#forBody.
    def exitForBody(self, ctx:EnglishLangParser.ForBodyContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#whileLoop.
    def enterWhileLoop(self, ctx:EnglishLangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#whileLoop.
    def exitWhileLoop(self, ctx:EnglishLangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#displayStatement.
    def enterDisplayStatement(self, ctx:EnglishLangParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#displayStatement.
    def exitDisplayStatement(self, ctx:EnglishLangParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#block.
    def enterBlock(self, ctx:EnglishLangParser.BlockContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#block.
    def exitBlock(self, ctx:EnglishLangParser.BlockContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#numExpression.
    def enterNumExpression(self, ctx:EnglishLangParser.NumExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#numExpression.
    def exitNumExpression(self, ctx:EnglishLangParser.NumExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#term.
    def enterTerm(self, ctx:EnglishLangParser.TermContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#term.
    def exitTerm(self, ctx:EnglishLangParser.TermContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#factor.
    def enterFactor(self, ctx:EnglishLangParser.FactorContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#factor.
    def exitFactor(self, ctx:EnglishLangParser.FactorContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#operation.
    def enterOperation(self, ctx:EnglishLangParser.OperationContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#operation.
    def exitOperation(self, ctx:EnglishLangParser.OperationContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#reassignment.
    def enterReassignment(self, ctx:EnglishLangParser.ReassignmentContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#reassignment.
    def exitReassignment(self, ctx:EnglishLangParser.ReassignmentContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#stringComparison.
    def enterStringComparison(self, ctx:EnglishLangParser.StringComparisonContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#stringComparison.
    def exitStringComparison(self, ctx:EnglishLangParser.StringComparisonContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#falseLiteral.
    def enterFalseLiteral(self, ctx:EnglishLangParser.FalseLiteralContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#falseLiteral.
    def exitFalseLiteral(self, ctx:EnglishLangParser.FalseLiteralContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#logicBinary.
    def enterLogicBinary(self, ctx:EnglishLangParser.LogicBinaryContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#logicBinary.
    def exitLogicBinary(self, ctx:EnglishLangParser.LogicBinaryContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#numComparison.
    def enterNumComparison(self, ctx:EnglishLangParser.NumComparisonContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#numComparison.
    def exitNumComparison(self, ctx:EnglishLangParser.NumComparisonContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#logicParen.
    def enterLogicParen(self, ctx:EnglishLangParser.LogicParenContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#logicParen.
    def exitLogicParen(self, ctx:EnglishLangParser.LogicParenContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#trueLiteral.
    def enterTrueLiteral(self, ctx:EnglishLangParser.TrueLiteralContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#trueLiteral.
    def exitTrueLiteral(self, ctx:EnglishLangParser.TrueLiteralContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#logicIdentifier.
    def enterLogicIdentifier(self, ctx:EnglishLangParser.LogicIdentifierContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#logicIdentifier.
    def exitLogicIdentifier(self, ctx:EnglishLangParser.LogicIdentifierContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#matrixComparison.
    def enterMatrixComparison(self, ctx:EnglishLangParser.MatrixComparisonContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#matrixComparison.
    def exitMatrixComparison(self, ctx:EnglishLangParser.MatrixComparisonContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#comparisonOp.
    def enterComparisonOp(self, ctx:EnglishLangParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#comparisonOp.
    def exitComparisonOp(self, ctx:EnglishLangParser.ComparisonOpContext):
        pass



del EnglishLangParser