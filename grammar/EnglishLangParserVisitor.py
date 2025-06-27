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


    # Visit a parse tree produced by EnglishLangParser#loopStatements.
    def visitLoopStatements(self, ctx:EnglishLangParser.LoopStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#variableDeclarationOrAssignment.
    def visitVariableDeclarationOrAssignment(self, ctx:EnglishLangParser.VariableDeclarationOrAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#matrixExpression.
    def visitMatrixExpression(self, ctx:EnglishLangParser.MatrixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#matrixAtom.
    def visitMatrixAtom(self, ctx:EnglishLangParser.MatrixAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#matrixConstruction.
    def visitMatrixConstruction(self, ctx:EnglishLangParser.MatrixConstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#row.
    def visitRow(self, ctx:EnglishLangParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#value.
    def visitValue(self, ctx:EnglishLangParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#stringExpression.
    def visitStringExpression(self, ctx:EnglishLangParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#expression.
    def visitExpression(self, ctx:EnglishLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#scopedIdentifier.
    def visitScopedIdentifier(self, ctx:EnglishLangParser.ScopedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#typeAnnotation.
    def visitTypeAnnotation(self, ctx:EnglishLangParser.TypeAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:EnglishLangParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#parameter.
    def visitParameter(self, ctx:EnglishLangParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#typedParameter.
    def visitTypedParameter(self, ctx:EnglishLangParser.TypedParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#returnStatement.
    def visitReturnStatement(self, ctx:EnglishLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#functionCall.
    def visitFunctionCall(self, ctx:EnglishLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#argumentList.
    def visitArgumentList(self, ctx:EnglishLangParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#builtInFunctions.
    def visitBuiltInFunctions(self, ctx:EnglishLangParser.BuiltInFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#ifStatement.
    def visitIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#loopIfStatement.
    def visitLoopIfStatement(self, ctx:EnglishLangParser.LoopIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#loopStatement.
    def visitLoopStatement(self, ctx:EnglishLangParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#forLoop.
    def visitForLoop(self, ctx:EnglishLangParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#forInit.
    def visitForInit(self, ctx:EnglishLangParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#forUpdate.
    def visitForUpdate(self, ctx:EnglishLangParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#forBody.
    def visitForBody(self, ctx:EnglishLangParser.ForBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#whileLoop.
    def visitWhileLoop(self, ctx:EnglishLangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#displayStatement.
    def visitDisplayStatement(self, ctx:EnglishLangParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#blockStatement.
    def visitBlockStatement(self, ctx:EnglishLangParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#numExpression.
    def visitNumExpression(self, ctx:EnglishLangParser.NumExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#term.
    def visitTerm(self, ctx:EnglishLangParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#unaryPlus.
    def visitUnaryPlus(self, ctx:EnglishLangParser.UnaryPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#unaryMinus.
    def visitUnaryMinus(self, ctx:EnglishLangParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#factorFunctionCall.
    def visitFactorFunctionCall(self, ctx:EnglishLangParser.FactorFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#factorNumber.
    def visitFactorNumber(self, ctx:EnglishLangParser.FactorNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#factorscopedIdentifier.
    def visitFactorscopedIdentifier(self, ctx:EnglishLangParser.FactorscopedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#factorIdentifier.
    def visitFactorIdentifier(self, ctx:EnglishLangParser.FactorIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#factorString.
    def visitFactorString(self, ctx:EnglishLangParser.FactorStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#factorOperation.
    def visitFactorOperation(self, ctx:EnglishLangParser.FactorOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#factorParens.
    def visitFactorParens(self, ctx:EnglishLangParser.FactorParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#castExpression.
    def visitCastExpression(self, ctx:EnglishLangParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#operation.
    def visitOperation(self, ctx:EnglishLangParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#reassignment.
    def visitReassignment(self, ctx:EnglishLangParser.ReassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#boolExpression.
    def visitBoolExpression(self, ctx:EnglishLangParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#logicOr.
    def visitLogicOr(self, ctx:EnglishLangParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#logicAnd.
    def visitLogicAnd(self, ctx:EnglishLangParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#logicNot.
    def visitLogicNot(self, ctx:EnglishLangParser.LogicNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#logicPrimaryWrap.
    def visitLogicPrimaryWrap(self, ctx:EnglishLangParser.LogicPrimaryWrapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#numComparison.
    def visitNumComparison(self, ctx:EnglishLangParser.NumComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#stringComparison.
    def visitStringComparison(self, ctx:EnglishLangParser.StringComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#matrixComparison.
    def visitMatrixComparison(self, ctx:EnglishLangParser.MatrixComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#logicParen.
    def visitLogicParen(self, ctx:EnglishLangParser.LogicParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#trueLiteral.
    def visitTrueLiteral(self, ctx:EnglishLangParser.TrueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#falseLiteral.
    def visitFalseLiteral(self, ctx:EnglishLangParser.FalseLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#logicIdentifier.
    def visitLogicIdentifier(self, ctx:EnglishLangParser.LogicIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnglishLangParser#comparisonOp.
    def visitComparisonOp(self, ctx:EnglishLangParser.ComparisonOpContext):
        return self.visitChildren(ctx)



del EnglishLangParser