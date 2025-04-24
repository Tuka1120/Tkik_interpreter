# Generated from EnglishLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,52,8,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,84,8,6,10,6,12,6,87,9,6,1,
        6,0,1,12,7,0,2,4,6,8,10,12,0,1,1,0,2,3,98,0,15,1,0,0,0,2,22,1,0,
        0,0,4,24,1,0,0,0,6,30,1,0,0,0,8,35,1,0,0,0,10,39,1,0,0,0,12,51,1,
        0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,
        18,1,0,0,0,18,1,1,0,0,0,19,23,3,4,2,0,20,23,3,6,3,0,21,23,3,8,4,
        0,22,19,1,0,0,0,22,20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,
        23,0,0,25,26,5,6,0,0,26,27,5,1,0,0,27,28,3,10,5,0,28,29,5,21,0,0,
        29,5,1,0,0,0,30,31,5,6,0,0,31,32,5,20,0,0,32,33,3,12,6,0,33,34,5,
        21,0,0,34,7,1,0,0,0,35,36,5,22,0,0,36,37,3,12,6,0,37,38,5,21,0,0,
        38,9,1,0,0,0,39,40,7,0,0,0,40,11,1,0,0,0,41,42,6,6,-1,0,42,43,5,
        13,0,0,43,52,3,12,6,9,44,45,5,18,0,0,45,46,3,12,6,0,46,47,5,19,0,
        0,47,52,1,0,0,0,48,52,5,5,0,0,49,52,5,4,0,0,50,52,5,6,0,0,51,41,
        1,0,0,0,51,44,1,0,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,
        52,85,1,0,0,0,53,54,10,15,0,0,54,55,5,7,0,0,55,84,3,12,6,16,56,57,
        10,14,0,0,57,58,5,8,0,0,58,84,3,12,6,15,59,60,10,13,0,0,60,61,5,
        9,0,0,61,84,3,12,6,14,62,63,10,12,0,0,63,64,5,10,0,0,64,84,3,12,
        6,13,65,66,10,11,0,0,66,67,5,11,0,0,67,84,3,12,6,12,68,69,10,10,
        0,0,69,70,5,12,0,0,70,84,3,12,6,11,71,72,10,8,0,0,72,73,5,14,0,0,
        73,84,3,12,6,9,74,75,10,7,0,0,75,76,5,15,0,0,76,84,3,12,6,8,77,78,
        10,6,0,0,78,79,5,16,0,0,79,84,3,12,6,7,80,81,10,5,0,0,81,82,5,17,
        0,0,82,84,3,12,6,6,83,53,1,0,0,0,83,56,1,0,0,0,83,59,1,0,0,0,83,
        62,1,0,0,0,83,65,1,0,0,0,83,68,1,0,0,0,83,71,1,0,0,0,83,74,1,0,0,
        0,83,77,1,0,0,0,83,80,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,
        1,0,0,0,86,13,1,0,0,0,87,85,1,0,0,0,5,17,22,51,83,85
    ]

class EnglishLangParser ( Parser ):

    grammarFileName = "EnglishLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'be'", "'number'", "'boolean'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'plus'", "'minus'", "'times'", 
                     "'divided by'", "'and'", "'or'", "'not'", "'is'", "'is not'", 
                     "'less than'", "'greater than'", "'('", "')'", "'becomes'", 
                     "'.'", "'say'", "'let'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "BOOLEAN", "ID", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "AND", "OR", "NOT", "EQUAL", "NOTEQUAL", 
                      "LESS", "GREATER", "LPAREN", "RPAREN", "ASSIGN", "SEMICOLON", 
                      "PRINT", "VAR", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_assignStmt = 3
    RULE_printStmt = 4
    RULE_type = 5
    RULE_expression = 6

    ruleNames =  [ "program", "statement", "varDecl", "assignStmt", "printStmt", 
                   "type", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUMBER=4
    BOOLEAN=5
    ID=6
    PLUS=7
    MINUS=8
    MULTIPLY=9
    DIVIDE=10
    AND=11
    OR=12
    NOT=13
    EQUAL=14
    NOTEQUAL=15
    LESS=16
    GREATER=17
    LPAREN=18
    RPAREN=19
    ASSIGN=20
    SEMICOLON=21
    PRINT=22
    VAR=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.StatementContext,i)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = EnglishLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12582976) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(EnglishLangParser.VarDeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(EnglishLangParser.AssignStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(EnglishLangParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = EnglishLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.varDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.assignStmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.printStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(EnglishLangParser.VAR, 0)

        def ID(self):
            return self.getToken(EnglishLangParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(EnglishLangParser.TypeContext,0)


        def SEMICOLON(self):
            return self.getToken(EnglishLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = EnglishLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(EnglishLangParser.VAR)
            self.state = 25
            self.match(EnglishLangParser.ID)
            self.state = 26
            self.match(EnglishLangParser.T__0)
            self.state = 27
            self.type_()
            self.state = 28
            self.match(EnglishLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnglishLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(EnglishLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(EnglishLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = EnglishLangParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(EnglishLangParser.ID)
            self.state = 31
            self.match(EnglishLangParser.ASSIGN)
            self.state = 32
            self.expression(0)
            self.state = 33
            self.match(EnglishLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(EnglishLangParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(EnglishLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = EnglishLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(EnglishLangParser.PRINT)
            self.state = 36
            self.expression(0)
            self.state = 37
            self.match(EnglishLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EnglishLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = EnglishLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(EnglishLangParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,i)


        def LPAREN(self):
            return self.getToken(EnglishLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(EnglishLangParser.RPAREN, 0)

        def BOOLEAN(self):
            return self.getToken(EnglishLangParser.BOOLEAN, 0)

        def NUMBER(self):
            return self.getToken(EnglishLangParser.NUMBER, 0)

        def ID(self):
            return self.getToken(EnglishLangParser.ID, 0)

        def PLUS(self):
            return self.getToken(EnglishLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(EnglishLangParser.MINUS, 0)

        def MULTIPLY(self):
            return self.getToken(EnglishLangParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(EnglishLangParser.DIVIDE, 0)

        def AND(self):
            return self.getToken(EnglishLangParser.AND, 0)

        def OR(self):
            return self.getToken(EnglishLangParser.OR, 0)

        def EQUAL(self):
            return self.getToken(EnglishLangParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(EnglishLangParser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(EnglishLangParser.LESS, 0)

        def GREATER(self):
            return self.getToken(EnglishLangParser.GREATER, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EnglishLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 42
                self.match(EnglishLangParser.NOT)
                self.state = 43
                self.expression(9)
                pass
            elif token in [18]:
                self.state = 44
                self.match(EnglishLangParser.LPAREN)
                self.state = 45
                self.expression(0)
                self.state = 46
                self.match(EnglishLangParser.RPAREN)
                pass
            elif token in [5]:
                self.state = 48
                self.match(EnglishLangParser.BOOLEAN)
                pass
            elif token in [4]:
                self.state = 49
                self.match(EnglishLangParser.NUMBER)
                pass
            elif token in [6]:
                self.state = 50
                self.match(EnglishLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 54
                        self.match(EnglishLangParser.PLUS)
                        self.state = 55
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 57
                        self.match(EnglishLangParser.MINUS)
                        self.state = 58
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 59
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 60
                        self.match(EnglishLangParser.MULTIPLY)
                        self.state = 61
                        self.expression(14)
                        pass

                    elif la_ == 4:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 62
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 63
                        self.match(EnglishLangParser.DIVIDE)
                        self.state = 64
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 66
                        self.match(EnglishLangParser.AND)
                        self.state = 67
                        self.expression(12)
                        pass

                    elif la_ == 6:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 69
                        self.match(EnglishLangParser.OR)
                        self.state = 70
                        self.expression(11)
                        pass

                    elif la_ == 7:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 72
                        self.match(EnglishLangParser.EQUAL)
                        self.state = 73
                        self.expression(9)
                        pass

                    elif la_ == 8:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 74
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 75
                        self.match(EnglishLangParser.NOTEQUAL)
                        self.state = 76
                        self.expression(8)
                        pass

                    elif la_ == 9:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 77
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 78
                        self.match(EnglishLangParser.LESS)
                        self.state = 79
                        self.expression(7)
                        pass

                    elif la_ == 10:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 80
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 81
                        self.match(EnglishLangParser.GREATER)
                        self.state = 82
                        self.expression(6)
                        pass

             
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         




