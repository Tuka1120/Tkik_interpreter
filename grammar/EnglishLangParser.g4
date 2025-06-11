parser grammar EnglishLangParser;

options { tokenVocab=EnglishLangLexer; }

// Entry point
program : START_PROGRAM statement+ END_PROGRAM ;

// Statements
statement: 
      variableDeclaration
    | reassignment
    | functionDeclaration
    | functionCall
    | returnStatement
    | displayStatement
    | ifStatement
    | loopStatement
    | forLoop
    | whileLoop
    | operation
    ;

loopStatements:
      loopStatement
    | variableDeclaration
    | reassignment
    | functionDeclaration
    | returnStatement
    | loopIfStatement
    | block
    | BREAK
    | displayStatement
    ;


// Variable Declaration & Assignment
variableDeclaration
    : SET? IDENTIFIER TO expression typeAnnotation?
    ;

matrixExpression: (INVERT_MATRIX)? matrixAtom (TRANSPOSITION)?;
matrixAtom: IDENTIFIER | matrixConstruction;

matrixConstruction: LBRACE row (SEMICOLON row)* RBRACE;
row: value (COMMA value)*;
value: NUMBER | IDENTIFIER | matrixExpression;

stringExpression: (STRING | IDENTIFIER) ( PLUS (STRING | IDENTIFIER))*;


expression:
      functionCall
    | builtInFunctions
    | numExpression
    | boolExpression
    | matrixExpression
    | stringExpression
    | scopedIdentifier
    | NUMBER
    | STRING
    | IDENTIFIER
    | '(' expression ')'
    ;

scopedIdentifier
    : (PARENT_SCOPE DCOLON)+ IDENTIFIER
    ;

typeAnnotation: TYPE_STRING | TYPE_INT | TYPE_FLOAT | TYPE_BOOL | TYPE_MATRIX;


// Function Declaration
functionDeclaration
    : DEFINE_FUNCTION IDENTIFIER LPAREN parameter? RPAREN block END_FUNCTION
    ;

// Parameters and Arguments
parameter
    : typedParameter (COMMA typedParameter)*
    ;

typedParameter
    : IDENTIFIER typeAnnotation?
    ;

// Return
returnStatement
    : RETURN expression
    ;

// Function Call
functionCall
    : CALL? IDENTIFIER LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;


builtInFunctions:POWER_FUNC LPAREN numExpression COMMA numExpression RPAREN
                |
             (SIN_FUNC | COS_FUNC | TAN_FUNC | CTAN_FUNC )
              LPAREN numExpression RPAREN;


ifStatement: IF LPAREN boolExpression RPAREN (statement | block)
             (ELSE_IF LPAREN boolExpression RPAREN (statement | block))*
             (ELSE (statement | block))?;
loopIfStatement: IF LPAREN boolExpression RPAREN (LBRACE loopStatements+ RBRACE | statement)

             (ELSE_IF LPAREN boolExpression RPAREN (LBRACE loopStatements+ RBRACE | statement))*

             (ELSE (LBRACE loopStatements+ RBRACE | statement))?;

loopStatement: forLoop | whileLoop;

forLoop
    : FOR LPAREN forInit? SEMICOLON
              cond=boolExpression SEMICOLON
              forUpdate RPAREN
      forBody;

forInit
    : IDENTIFIER
    | variableDeclaration
    ;

forUpdate
    : variableDeclaration
    | reassignment
    | operation
    ;

forBody
    : LBRACE loopStatements+ RBRACE
    | statement
    ;

whileLoop:
           WHILE LPAREN boolExpression RPAREN
           (LBRACE loopStatements+ RBRACE | statement);

// Display
displayStatement: DISPLAY expression (',' expression)*;

// Blocks
block: LBRACE statement+ RBRACE ;

// Expressions
numExpression : numExpression (PLUS|MINUS) term 
    | term;

term: term (MULTIPLY|DIVIDED_BY|MODULO) factor
    | factor;

factor
    : PLUS factor                              #unaryPlus
    | MINUS factor                             #unaryMinus
    | functionCall                             #factorFunctionCall
    | NUMBER                                   #factorNumber
    | IDENTIFIER                               #factorIdentifier
    | STRING                                   #factorString
    | operation                                #factorOperation
    | LPAREN numExpression RPAREN              #factorParens
    ;

operation : IDENTIFIER (INCREMENT | DECREMENT) SEMICOLON? ;

reassignment: IDENTIFIER ((ADD_TO STRING | ADD_TO numExpression)
                          | SUBTRACT_FROM numExpression
                          | DIVIDE_FROM numExpression
                          | TIMES numExpression)
               SEMICOLON;

boolExpression
    : boolOrExpression
    ;

boolOrExpression
    : boolAndExpression (OR boolAndExpression)*       #logicOr
    ;

boolAndExpression
    : boolNotExpression (AND boolNotExpression)*      #logicAnd
    ;

boolNotExpression
    : NOT boolNotExpression                           #logicNot
    | boolPrimary                                     #logicPrimaryWrap
    ;

boolPrimary
    : numExpression comparisonOp numExpression        #numComparison
    | stringExpression (EQUALS | NOT_EQUALS) stringExpression   #stringComparison
    | matrixExpression (EQUALS | NOT_EQUALS) matrixExpression   #matrixComparison
    | LPAREN boolExpression RPAREN                    #logicParen
    | TRUE_VALUE                                      #trueLiteral
    | FALSE_VALUE                                     #falseLiteral
    | IDENTIFIER                                      #logicIdentifier
    ;


// Comparison Operators
comparisonOp
    : EQUALS
    | NOT_EQUALS
    | GREATER_THAN
    | LESS_THAN
    | GREATER_EQUAL
    | LESS_EQUAL
    ;
