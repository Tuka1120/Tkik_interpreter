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


    # Enter a parse tree produced by EnglishLangParser#block.
    def enterBlock(self, ctx:EnglishLangParser.BlockContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#block.
    def exitBlock(self, ctx:EnglishLangParser.BlockContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#assignment.
    def enterAssignment(self, ctx:EnglishLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#assignment.
    def exitAssignment(self, ctx:EnglishLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#reassignment.
    def enterReassignment(self, ctx:EnglishLangParser.ReassignmentContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#reassignment.
    def exitReassignment(self, ctx:EnglishLangParser.ReassignmentContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#expression.
    def enterExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#expression.
    def exitExpression(self, ctx:EnglishLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#indexedVar.
    def enterIndexedVar(self, ctx:EnglishLangParser.IndexedVarContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#indexedVar.
    def exitIndexedVar(self, ctx:EnglishLangParser.IndexedVarContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#indexList.
    def enterIndexList(self, ctx:EnglishLangParser.IndexListContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#indexList.
    def exitIndexList(self, ctx:EnglishLangParser.IndexListContext):
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


    # Enter a parse tree produced by EnglishLangParser#stringExpression.
    def enterStringExpression(self, ctx:EnglishLangParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#stringExpression.
    def exitStringExpression(self, ctx:EnglishLangParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#funcCall.
    def enterFuncCall(self, ctx:EnglishLangParser.FuncCallContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#funcCall.
    def exitFuncCall(self, ctx:EnglishLangParser.FuncCallContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#boolExpression.
    def enterBoolExpression(self, ctx:EnglishLangParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#boolExpression.
    def exitBoolExpression(self, ctx:EnglishLangParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:EnglishLangParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:EnglishLangParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#boolValue.
    def enterBoolValue(self, ctx:EnglishLangParser.BoolValueContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#boolValue.
    def exitBoolValue(self, ctx:EnglishLangParser.BoolValueContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#funcDecl.
    def enterFuncDecl(self, ctx:EnglishLangParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#funcDecl.
    def exitFuncDecl(self, ctx:EnglishLangParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#parameters.
    def enterParameters(self, ctx:EnglishLangParser.ParametersContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#parameters.
    def exitParameters(self, ctx:EnglishLangParser.ParametersContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#ifStatement.
    def enterIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#ifStatement.
    def exitIfStatement(self, ctx:EnglishLangParser.IfStatementContext):
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


    # Enter a parse tree produced by EnglishLangParser#whileLoop.
    def enterWhileLoop(self, ctx:EnglishLangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#whileLoop.
    def exitWhileLoop(self, ctx:EnglishLangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#displayDecl.
    def enterDisplayDecl(self, ctx:EnglishLangParser.DisplayDeclContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#displayDecl.
    def exitDisplayDecl(self, ctx:EnglishLangParser.DisplayDeclContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#printStatement.
    def enterPrintStatement(self, ctx:EnglishLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#printStatement.
    def exitPrintStatement(self, ctx:EnglishLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#typeName.
    def enterTypeName(self, ctx:EnglishLangParser.TypeNameContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#typeName.
    def exitTypeName(self, ctx:EnglishLangParser.TypeNameContext):
        pass


    # Enter a parse tree produced by EnglishLangParser#operation.
    def enterOperation(self, ctx:EnglishLangParser.OperationContext):
        pass

    # Exit a parse tree produced by EnglishLangParser#operation.
    def exitOperation(self, ctx:EnglishLangParser.OperationContext):
        pass



del EnglishLangParser