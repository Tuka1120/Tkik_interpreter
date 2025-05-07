# Generated from EnglishLangParser.g4 by ANTLR 4.13.1
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
        4,1,50,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        56,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,3,4,70,8,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,5,7,88,8,7,10,7,12,7,91,9,7,1,8,1,8,1,8,3,8,96,8,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,5,9,105,8,9,10,9,12,9,108,9,9,1,9,1,9,3,9,112,8,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,5,12,133,8,12,10,12,12,12,136,9,12,
        1,13,1,13,1,13,1,14,1,14,1,14,5,14,144,8,14,10,14,12,14,147,9,14,
        1,15,5,15,150,8,15,10,15,12,15,153,9,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,162,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,183,
        8,16,10,16,12,16,186,9,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,0,1,
        32,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,2,1,
        0,45,47,1,0,28,32,199,0,38,1,0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,63,
        1,0,0,0,8,65,1,0,0,0,10,75,1,0,0,0,12,80,1,0,0,0,14,83,1,0,0,0,16,
        95,1,0,0,0,18,97,1,0,0,0,20,115,1,0,0,0,22,120,1,0,0,0,24,129,1,
        0,0,0,26,137,1,0,0,0,28,140,1,0,0,0,30,151,1,0,0,0,32,161,1,0,0,
        0,34,187,1,0,0,0,36,191,1,0,0,0,38,42,5,1,0,0,39,41,3,2,1,0,40,39,
        1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,
        44,42,1,0,0,0,45,46,5,2,0,0,46,1,1,0,0,0,47,56,3,4,2,0,48,56,3,8,
        4,0,49,56,3,10,5,0,50,56,3,14,7,0,51,56,3,18,9,0,52,56,3,22,11,0,
        53,56,3,20,10,0,54,56,3,12,6,0,55,47,1,0,0,0,55,48,1,0,0,0,55,49,
        1,0,0,0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,
        55,54,1,0,0,0,56,3,1,0,0,0,57,58,5,8,0,0,58,59,5,48,0,0,59,60,5,
        9,0,0,60,61,3,32,16,0,61,62,3,6,3,0,62,5,1,0,0,0,63,64,7,0,0,0,64,
        7,1,0,0,0,65,66,5,3,0,0,66,67,5,48,0,0,67,69,5,41,0,0,68,70,3,24,
        12,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,42,0,0,72,
        73,3,30,15,0,73,74,5,4,0,0,74,9,1,0,0,0,75,76,5,6,0,0,76,77,5,48,
        0,0,77,78,5,7,0,0,78,79,3,28,14,0,79,11,1,0,0,0,80,81,5,5,0,0,81,
        82,3,32,16,0,82,13,1,0,0,0,83,84,5,10,0,0,84,89,3,16,8,0,85,86,5,
        33,0,0,86,88,3,16,8,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,
        89,90,1,0,0,0,90,15,1,0,0,0,91,89,1,0,0,0,92,96,5,44,0,0,93,96,5,
        48,0,0,94,96,3,32,16,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,
        96,17,1,0,0,0,97,98,5,11,0,0,98,99,3,34,17,0,99,106,3,30,15,0,100,
        101,5,12,0,0,101,102,3,34,17,0,102,103,3,30,15,0,103,105,1,0,0,0,
        104,100,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,
        107,111,1,0,0,0,108,106,1,0,0,0,109,110,5,13,0,0,110,112,3,30,15,
        0,111,109,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,5,14,0,
        0,114,19,1,0,0,0,115,116,5,19,0,0,116,117,3,34,17,0,117,118,3,30,
        15,0,118,119,5,20,0,0,119,21,1,0,0,0,120,121,5,15,0,0,121,122,5,
        48,0,0,122,123,5,16,0,0,123,124,3,32,16,0,124,125,5,9,0,0,125,126,
        3,32,16,0,126,127,3,30,15,0,127,128,5,18,0,0,128,23,1,0,0,0,129,
        134,3,26,13,0,130,131,5,33,0,0,131,133,3,26,13,0,132,130,1,0,0,0,
        133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,25,1,0,0,0,136,
        134,1,0,0,0,137,138,5,48,0,0,138,139,3,6,3,0,139,27,1,0,0,0,140,
        145,3,32,16,0,141,142,5,33,0,0,142,144,3,32,16,0,143,141,1,0,0,0,
        144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,29,1,0,0,0,147,
        145,1,0,0,0,148,150,3,2,1,0,149,148,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,31,1,0,0,0,153,151,1,0,0,0,154,155,
        6,16,-1,0,155,156,5,41,0,0,156,157,3,32,16,0,157,158,5,42,0,0,158,
        162,1,0,0,0,159,162,5,43,0,0,160,162,5,48,0,0,161,154,1,0,0,0,161,
        159,1,0,0,0,161,160,1,0,0,0,162,184,1,0,0,0,163,164,10,9,0,0,164,
        165,5,23,0,0,165,183,3,32,16,10,166,167,10,8,0,0,167,168,5,24,0,
        0,168,183,3,32,16,9,169,170,10,7,0,0,170,171,5,25,0,0,171,183,3,
        32,16,8,172,173,10,6,0,0,173,174,5,26,0,0,174,183,3,32,16,7,175,
        176,10,5,0,0,176,177,5,27,0,0,177,183,3,32,16,6,178,179,10,4,0,0,
        179,180,3,36,18,0,180,181,3,32,16,5,181,183,1,0,0,0,182,163,1,0,
        0,0,182,166,1,0,0,0,182,169,1,0,0,0,182,172,1,0,0,0,182,175,1,0,
        0,0,182,178,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,
        0,0,185,33,1,0,0,0,186,184,1,0,0,0,187,188,3,32,16,0,188,189,3,36,
        18,0,189,190,3,32,16,0,190,35,1,0,0,0,191,192,7,1,0,0,192,37,1,0,
        0,0,13,42,55,69,89,95,106,111,134,145,151,161,182,184
    ]

class EnglishLangParser ( Parser ):

    grammarFileName = "EnglishLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Start Program'", "'End Program'", "'Define Function'", 
                     "'End Function'", "'Return'", "'Call'", "'with'", "'Set'", 
                     "'to'", "'Display'", "'If'", "'Else If'", "'Else'", 
                     "'End If'", "'For each'", "'from'", "'in'", "'End For'", 
                     "'While'", "'End While'", "'Increment'", "'by'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'>'", "'<'", "'>='", 
                     "'<='", "','", "':'", "'.'", "'\"'", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'int'", "'string'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "START_PROGRAM", "END_PROGRAM", "DEFINE_FUNCTION", 
                      "END_FUNCTION", "RETURN", "CALL", "WITH", "SET", "TO", 
                      "DISPLAY", "IF", "ELSE_IF", "ELSE", "END_IF", "FOR_EACH", 
                      "FROM", "IN", "END_FOR", "WHILE", "END_WHILE", "INCREMENT", 
                      "BY", "PLUS", "MINUS", "TIMES", "DIVIDED_BY", "MODULO", 
                      "EQUALS", "GREATER_THAN", "LESS_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "COMMA", "COLON", "DOT", "QUOTE", "LBRACK", 
                      "RBRACK", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                      "NUMBER", "STRING", "TYPE_INT", "TYPE_STRING", "TYPE_BOOL", 
                      "IDENTIFIER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_typeAnnotation = 3
    RULE_functionDeclaration = 4
    RULE_functionCall = 5
    RULE_returnStatement = 6
    RULE_displayStatement = 7
    RULE_displayPart = 8
    RULE_ifStatement = 9
    RULE_whileStatement = 10
    RULE_forEachStatement = 11
    RULE_parameterList = 12
    RULE_typedParameter = 13
    RULE_argumentList = 14
    RULE_block = 15
    RULE_expression = 16
    RULE_condition = 17
    RULE_comparisonOp = 18

    ruleNames =  [ "program", "statement", "variableDeclaration", "typeAnnotation", 
                   "functionDeclaration", "functionCall", "returnStatement", 
                   "displayStatement", "displayPart", "ifStatement", "whileStatement", 
                   "forEachStatement", "parameterList", "typedParameter", 
                   "argumentList", "block", "expression", "condition", "comparisonOp" ]

    EOF = Token.EOF
    START_PROGRAM=1
    END_PROGRAM=2
    DEFINE_FUNCTION=3
    END_FUNCTION=4
    RETURN=5
    CALL=6
    WITH=7
    SET=8
    TO=9
    DISPLAY=10
    IF=11
    ELSE_IF=12
    ELSE=13
    END_IF=14
    FOR_EACH=15
    FROM=16
    IN=17
    END_FOR=18
    WHILE=19
    END_WHILE=20
    INCREMENT=21
    BY=22
    PLUS=23
    MINUS=24
    TIMES=25
    DIVIDED_BY=26
    MODULO=27
    EQUALS=28
    GREATER_THAN=29
    LESS_THAN=30
    GREATER_EQUAL=31
    LESS_EQUAL=32
    COMMA=33
    COLON=34
    DOT=35
    QUOTE=36
    LBRACK=37
    RBRACK=38
    LBRACE=39
    RBRACE=40
    LPAREN=41
    RPAREN=42
    NUMBER=43
    STRING=44
    TYPE_INT=45
    TYPE_STRING=46
    TYPE_BOOL=47
    IDENTIFIER=48
    WS=49
    COMMENT=50

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

        def START_PROGRAM(self):
            return self.getToken(EnglishLangParser.START_PROGRAM, 0)

        def END_PROGRAM(self):
            return self.getToken(EnglishLangParser.END_PROGRAM, 0)

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
            self.state = 38
            self.match(EnglishLangParser.START_PROGRAM)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 560488) != 0):
                self.state = 39
                self.statement()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(EnglishLangParser.END_PROGRAM)
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

        def variableDeclaration(self):
            return self.getTypedRuleContext(EnglishLangParser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(EnglishLangParser.FunctionDeclarationContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(EnglishLangParser.FunctionCallContext,0)


        def displayStatement(self):
            return self.getTypedRuleContext(EnglishLangParser.DisplayStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(EnglishLangParser.IfStatementContext,0)


        def forEachStatement(self):
            return self.getTypedRuleContext(EnglishLangParser.ForEachStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(EnglishLangParser.WhileStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(EnglishLangParser.ReturnStatementContext,0)


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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.variableDeclaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.functionDeclaration()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.functionCall()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.displayStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.ifStatement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.forEachStatement()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 7)
                self.state = 53
                self.whileStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 8)
                self.state = 54
                self.returnStatement()
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


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(EnglishLangParser.SET, 0)

        def IDENTIFIER(self):
            return self.getToken(EnglishLangParser.IDENTIFIER, 0)

        def TO(self):
            return self.getToken(EnglishLangParser.TO, 0)

        def expression(self):
            return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,0)


        def typeAnnotation(self):
            return self.getTypedRuleContext(EnglishLangParser.TypeAnnotationContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = EnglishLangParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(EnglishLangParser.SET)
            self.state = 58
            self.match(EnglishLangParser.IDENTIFIER)
            self.state = 59
            self.match(EnglishLangParser.TO)
            self.state = 60
            self.expression(0)
            self.state = 61
            self.typeAnnotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(EnglishLangParser.TYPE_INT, 0)

        def TYPE_STRING(self):
            return self.getToken(EnglishLangParser.TYPE_STRING, 0)

        def TYPE_BOOL(self):
            return self.getToken(EnglishLangParser.TYPE_BOOL, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_typeAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAnnotation" ):
                listener.enterTypeAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAnnotation" ):
                listener.exitTypeAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAnnotation" ):
                return visitor.visitTypeAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def typeAnnotation(self):

        localctx = EnglishLangParser.TypeAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typeAnnotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621824) != 0)):
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


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE_FUNCTION(self):
            return self.getToken(EnglishLangParser.DEFINE_FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(EnglishLangParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(EnglishLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(EnglishLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(EnglishLangParser.BlockContext,0)


        def END_FUNCTION(self):
            return self.getToken(EnglishLangParser.END_FUNCTION, 0)

        def parameterList(self):
            return self.getTypedRuleContext(EnglishLangParser.ParameterListContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = EnglishLangParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(EnglishLangParser.DEFINE_FUNCTION)
            self.state = 66
            self.match(EnglishLangParser.IDENTIFIER)
            self.state = 67
            self.match(EnglishLangParser.LPAREN)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 68
                self.parameterList()


            self.state = 71
            self.match(EnglishLangParser.RPAREN)
            self.state = 72
            self.block()
            self.state = 73
            self.match(EnglishLangParser.END_FUNCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(EnglishLangParser.CALL, 0)

        def IDENTIFIER(self):
            return self.getToken(EnglishLangParser.IDENTIFIER, 0)

        def WITH(self):
            return self.getToken(EnglishLangParser.WITH, 0)

        def argumentList(self):
            return self.getTypedRuleContext(EnglishLangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = EnglishLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(EnglishLangParser.CALL)
            self.state = 76
            self.match(EnglishLangParser.IDENTIFIER)
            self.state = 77
            self.match(EnglishLangParser.WITH)
            self.state = 78
            self.argumentList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(EnglishLangParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = EnglishLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(EnglishLangParser.RETURN)
            self.state = 81
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPLAY(self):
            return self.getToken(EnglishLangParser.DISPLAY, 0)

        def displayPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.DisplayPartContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.DisplayPartContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnglishLangParser.COMMA)
            else:
                return self.getToken(EnglishLangParser.COMMA, i)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_displayStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayStatement" ):
                listener.enterDisplayStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayStatement" ):
                listener.exitDisplayStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayStatement" ):
                return visitor.visitDisplayStatement(self)
            else:
                return visitor.visitChildren(self)




    def displayStatement(self):

        localctx = EnglishLangParser.DisplayStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_displayStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(EnglishLangParser.DISPLAY)
            self.state = 84
            self.displayPart()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 85
                self.match(EnglishLangParser.COMMA)
                self.state = 86
                self.displayPart()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EnglishLangParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(EnglishLangParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_displayPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayPart" ):
                listener.enterDisplayPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayPart" ):
                listener.exitDisplayPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayPart" ):
                return visitor.visitDisplayPart(self)
            else:
                return visitor.visitChildren(self)




    def displayPart(self):

        localctx = EnglishLangParser.DisplayPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_displayPart)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(EnglishLangParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(EnglishLangParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(EnglishLangParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.ConditionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.BlockContext,i)


        def END_IF(self):
            return self.getToken(EnglishLangParser.END_IF, 0)

        def ELSE_IF(self, i:int=None):
            if i is None:
                return self.getTokens(EnglishLangParser.ELSE_IF)
            else:
                return self.getToken(EnglishLangParser.ELSE_IF, i)

        def ELSE(self):
            return self.getToken(EnglishLangParser.ELSE, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = EnglishLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(EnglishLangParser.IF)
            self.state = 98
            self.condition()
            self.state = 99
            self.block()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 100
                self.match(EnglishLangParser.ELSE_IF)
                self.state = 101
                self.condition()
                self.state = 102
                self.block()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 109
                self.match(EnglishLangParser.ELSE)
                self.state = 110
                self.block()


            self.state = 113
            self.match(EnglishLangParser.END_IF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(EnglishLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(EnglishLangParser.ConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(EnglishLangParser.BlockContext,0)


        def END_WHILE(self):
            return self.getToken(EnglishLangParser.END_WHILE, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = EnglishLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(EnglishLangParser.WHILE)
            self.state = 116
            self.condition()
            self.state = 117
            self.block()
            self.state = 118
            self.match(EnglishLangParser.END_WHILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForEachStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_EACH(self):
            return self.getToken(EnglishLangParser.FOR_EACH, 0)

        def IDENTIFIER(self):
            return self.getToken(EnglishLangParser.IDENTIFIER, 0)

        def FROM(self):
            return self.getToken(EnglishLangParser.FROM, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(EnglishLangParser.TO, 0)

        def block(self):
            return self.getTypedRuleContext(EnglishLangParser.BlockContext,0)


        def END_FOR(self):
            return self.getToken(EnglishLangParser.END_FOR, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_forEachStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForEachStatement" ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForEachStatement" ):
                listener.exitForEachStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForEachStatement" ):
                return visitor.visitForEachStatement(self)
            else:
                return visitor.visitChildren(self)




    def forEachStatement(self):

        localctx = EnglishLangParser.ForEachStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forEachStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(EnglishLangParser.FOR_EACH)
            self.state = 121
            self.match(EnglishLangParser.IDENTIFIER)
            self.state = 122
            self.match(EnglishLangParser.FROM)
            self.state = 123
            self.expression(0)
            self.state = 124
            self.match(EnglishLangParser.TO)
            self.state = 125
            self.expression(0)
            self.state = 126
            self.block()
            self.state = 127
            self.match(EnglishLangParser.END_FOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.TypedParameterContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.TypedParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnglishLangParser.COMMA)
            else:
                return self.getToken(EnglishLangParser.COMMA, i)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = EnglishLangParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.typedParameter()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 130
                self.match(EnglishLangParser.COMMA)
                self.state = 131
                self.typedParameter()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(EnglishLangParser.IDENTIFIER, 0)

        def typeAnnotation(self):
            return self.getTypedRuleContext(EnglishLangParser.TypeAnnotationContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_typedParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedParameter" ):
                listener.enterTypedParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedParameter" ):
                listener.exitTypedParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedParameter" ):
                return visitor.visitTypedParameter(self)
            else:
                return visitor.visitChildren(self)




    def typedParameter(self):

        localctx = EnglishLangParser.TypedParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typedParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(EnglishLangParser.IDENTIFIER)
            self.state = 138
            self.typeAnnotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnglishLangParser.COMMA)
            else:
                return self.getToken(EnglishLangParser.COMMA, i)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = EnglishLangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.expression(0)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 141
                self.match(EnglishLangParser.COMMA)
                self.state = 142
                self.expression(0)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
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
            return EnglishLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = EnglishLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 560488) != 0):
                self.state = 148
                self.statement()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def LPAREN(self):
            return self.getToken(EnglishLangParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(EnglishLangParser.RPAREN, 0)

        def NUMBER(self):
            return self.getToken(EnglishLangParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(EnglishLangParser.IDENTIFIER, 0)

        def PLUS(self):
            return self.getToken(EnglishLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(EnglishLangParser.MINUS, 0)

        def TIMES(self):
            return self.getToken(EnglishLangParser.TIMES, 0)

        def DIVIDED_BY(self):
            return self.getToken(EnglishLangParser.DIVIDED_BY, 0)

        def MODULO(self):
            return self.getToken(EnglishLangParser.MODULO, 0)

        def comparisonOp(self):
            return self.getTypedRuleContext(EnglishLangParser.ComparisonOpContext,0)


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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.state = 155
                self.match(EnglishLangParser.LPAREN)
                self.state = 156
                self.expression(0)
                self.state = 157
                self.match(EnglishLangParser.RPAREN)
                pass
            elif token in [43]:
                self.state = 159
                self.match(EnglishLangParser.NUMBER)
                pass
            elif token in [48]:
                self.state = 160
                self.match(EnglishLangParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 182
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 164
                        self.match(EnglishLangParser.PLUS)
                        self.state = 165
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 167
                        self.match(EnglishLangParser.MINUS)
                        self.state = 168
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 170
                        self.match(EnglishLangParser.TIMES)
                        self.state = 171
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 173
                        self.match(EnglishLangParser.DIVIDED_BY)
                        self.state = 174
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 176
                        self.match(EnglishLangParser.MODULO)
                        self.state = 177
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = EnglishLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 178
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 179
                        self.comparisonOp()
                        self.state = 180
                        self.expression(5)
                        pass

             
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnglishLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnglishLangParser.ExpressionContext,i)


        def comparisonOp(self):
            return self.getTypedRuleContext(EnglishLangParser.ComparisonOpContext,0)


        def getRuleIndex(self):
            return EnglishLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = EnglishLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.expression(0)
            self.state = 188
            self.comparisonOp()
            self.state = 189
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(EnglishLangParser.EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(EnglishLangParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(EnglishLangParser.LESS_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(EnglishLangParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(EnglishLangParser.LESS_EQUAL, 0)

        def getRuleIndex(self):
            return EnglishLangParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOp" ):
                return visitor.visitComparisonOp(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOp(self):

        localctx = EnglishLangParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         




