parser grammar EnglishLangParser;

options { tokenVocab=EnglishLangLexer; }

// Entry point
program : START_PROGRAM statement* END_PROGRAM ;

// Statements
statement
    : variableDeclaration
    | functionDeclaration
    | functionCall
    | displayStatement
    | ifStatement
    | forEachStatement
    | whileStatement
    | returnStatement
    ;

// Variable Declaration & Assignment
variableDeclaration
    : SET IDENTIFIER TO expression typeAnnotation
    ;

typeAnnotation
    : TYPE_INT
    | TYPE_STRING
    | TYPE_BOOL
    ;

// Function Declaration
functionDeclaration
    : DEFINE_FUNCTION IDENTIFIER LPAREN parameterList? RPAREN block END_FUNCTION
    ;

// Function Call
functionCall
    : CALL IDENTIFIER WITH argumentList
    ;

// Return
returnStatement
    : RETURN expression
    ;

// Display
displayStatement
    : DISPLAY displayPart (COMMA displayPart)*
    ;

displayPart
    : STRING
    | IDENTIFIER
    | expression
    ;

// If / Else
ifStatement
    : IF condition block (ELSE_IF condition block)* (ELSE block)? END_IF
    ;

// While
whileStatement
    : WHILE condition block END_WHILE
    ;

// For Each
forEachStatement
    : FOR_EACH IDENTIFIER FROM expression TO expression block END_FOR
    ;

// Parameters and Arguments
parameterList
    : typedParameter (COMMA typedParameter)*
    ;

typedParameter
    : IDENTIFIER typeAnnotation
    ;

argumentList
    : expression (COMMA expression)*
    ;

// Blocks
block
    : statement*
    ;

// Expressions
expression
    : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDED_BY expression
    | expression MODULO expression
    | expression comparisonOp expression
    | LPAREN expression RPAREN
    | NUMBER
    | IDENTIFIER
    ;

// Conditions
condition
    : expression comparisonOp expression
    ;

// Comparison Operators
comparisonOp
    : EQUALS
    | GREATER_THAN
    | LESS_THAN
    | GREATER_EQUAL
    | LESS_EQUAL
    ;
