// EnglishLang.g4 - English-like language grammar using ANTLR

grammar EnglishLang;

// Parser Rules
program: statement+ ;

statement
    : varDecl
    | assignStmt
    | printStmt
    ;

varDecl: VAR ID 'be' type SEMICOLON ;
assignStmt: ID ASSIGN expression SEMICOLON ;
printStmt: PRINT expression SEMICOLON ;

type: 'number' | 'boolean' ;

expression
    : expression PLUS expression
    | expression MINUS expression
    | expression MULTIPLY expression
    | expression DIVIDE expression
    | expression AND expression
    | expression OR expression
    | NOT expression
    | expression EQUAL expression
    | expression NOTEQUAL expression
    | expression LESS expression
    | expression GREATER expression
    | LPAREN expression RPAREN
    | BOOLEAN
    | NUMBER
    | ID
    ;

// Lexer Rules
fragment DIGIT: [0-9] ;
fragment LETTER: [a-zA-Z] ;

NUMBER: DIGIT+ ('.' DIGIT+)? ;
BOOLEAN: 'true' | 'false' ;
ID: LETTER (LETTER | DIGIT)* ;

PLUS: 'plus' ;
MINUS: 'minus' ;
MULTIPLY: 'times' ;
DIVIDE: 'divided by' ;
AND: 'and' ;
OR: 'or' ;
NOT: 'not' ;

EQUAL: 'is' ;
NOTEQUAL: 'is not' ;
LESS: 'less than' ;
GREATER: 'greater than' ;

LPAREN: '(' ;
RPAREN: ')' ;
ASSIGN: 'becomes' ;
SEMICOLON: '.' ;
PRINT: 'say' ;
VAR: 'let' ;

WS: [ \t\r\n]+ -> skip ;
