now that this is new grammar file 
grammar EnglishLang;

// Parser Rules
program: statement* EOF;

statement
    : variableDeclaration
    | assignment
    | loopStatement
    | whileLoop
    | printStatement
    | expressionStatement
    ;

variableDeclaration
    : 'define' type IDENTIFIER 'as' expression
    ;

assignment
    : 'set' IDENTIFIER 'to' expression
    ;

loopStatement
    : 'repeat' 'from' NUMBER 'to' NUMBER ('step' NUMBER)? NEWLINE statement* 'end' 'repeat'
    ;

whileLoop
    : 'repeat' 'while' expression NEWLINE statement* 'end' 'repeat'
    ;

printStatement
    : 'print' expression
    ;

expressionStatement
    : expression
    ;

expression
    : expression op=('*'|'/') expression
    | expression op=('+'|'-') expression
    | expression op=('>'|'>='|'<'|'<='|'=='|'!=') expression
    | expression op=('and'|'or') expression
    | 'not' expression
    | '(' expression ')'
    | IDENTIFIER
    | NUMBER
    | STRING
    | BOOLEAN
    ;

type
    : 'number'
    | 'text'
    | 'boolean'
    ;

// Lexer Rules
BOOLEAN: 'true' | 'false';
STRING: '"' (~["\\\r\n])* '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

// Operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';

// Comparison
EQUAL: '==';
NOT_EQUAL: '!=';
GREATER_THAN: '>';
LESS_THAN: '<';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';

// Logical
AND: 'and';
OR: 'or';
NOT: 'not';

// Punctuation and Symbols
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
COLON: ':';
NEWLINE: ('\r'? '\n')+;

// Comments
LINE_COMMENT: '#' ~[\r\n]* -> skip;

// Whitespace
WS: [ \t]+ -> skip;
