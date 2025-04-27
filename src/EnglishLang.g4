grammar EnglishLang;

program: statement* EOF;

statement:
    assignment SEMICOLON
  | reassignment SEMICOLON
  | funcDecl
  | loopStatement
  | displayDecl
  | printStatement
  | ifStatement
  | operation SEMICOLON;

block: LEFT_BRACE statement* RIGHT_BRACE;

assignment: typeName? IDENTIFIER ASSIGN expression;

reassignment: IDENTIFIER ADD_TO expression 
            | IDENTIFIER SUBTRACT_FROM expression
            | IDENTIFIER TIMES expression
            | IDENTIFIER DIVIDE_FROM expression;

expression:
    numExpression
  | boolExpression
  | stringExpression
  | IDENTIFIER
  | NUMBER
  | STRING
  | funcCall
  | indexedVar;

indexedVar: IDENTIFIER LEFT_BRACKET indexList RIGHT_BRACKET;

indexList: expression (COMMA expression)*;

numExpression: numExpression (PLUS|MINUS) term | term;

term: term (MULTIPLY|DIVIDE|MODULO) factor
    | factor;

factor: NUMBER
      | IDENTIFIER
      | LEFT_PAREN numExpression RIGHT_PAREN;

stringExpression: STRING (PLUS STRING)*;

funcCall: IDENTIFIER LEFT_PAREN (expression (COMMA expression)*)? RIGHT_PAREN;

boolExpression: numExpression comparisonOperator numExpression
              | IDENTIFIER comparisonOperator IDENTIFIER
              | boolValue
              | NOT? LEFT_PAREN boolExpression RIGHT_PAREN;

comparisonOperator:
    EQUAL
  | NOT_EQUAL
  | LESS_THAN
  | GREATER_THAN
  | LESS_EQUAL
  | GREATER_EQUAL;

boolValue: TRUE_VALUE | FALSE_VALUE;

funcDecl: FUNC_INSTR typeName IDENTIFIER LEFT_PAREN parameters? RIGHT_PAREN block;

parameters: typeName IDENTIFIER (COMMA typeName IDENTIFIER)*;

ifStatement: IF_INSTR LEFT_PAREN boolExpression RIGHT_PAREN block (ELSE_INSTR block)?;

loopStatement: forLoop | whileLoop;

forLoop: FOR_INSTR LEFT_PAREN assignment SEMICOLON boolExpression SEMICOLON reassignment RIGHT_PAREN block;

whileLoop: WHILE_INSTR LEFT_PAREN boolExpression RIGHT_PAREN block;

displayDecl: DISPLAY_INSTR LEFT_PAREN expression RIGHT_PAREN SEMICOLON;

printStatement: PRINT_INSTR LEFT_PAREN expression RIGHT_PAREN SEMICOLON;

typeName: TYPE_STRING | TYPE_INT | TYPE_FLOAT | TYPE_BOOL | TYPE_MATRIX;

operation: IDENTIFIER (INCREMENT | DECREMENT);

// --------------- Operators and Assignment -------------------
ADD_TO           : '+=';
SUBTRACT_FROM    : '-=';
TIMES            : '*=';
DIVIDE_FROM      : '/=';

INCREMENT        : '++';
DECREMENT        : '--';

// --------------- Data Types ------------------
TYPE_STRING      : 'string';
TYPE_INT         : 'int';
TYPE_FLOAT       : 'float';
TYPE_BOOL        : 'bool';
TYPE_MATRIX      : 'matrix';

// --------------- Logic Operators -------------------
NOT             : '!';

// --------------- Reserved Keywords ------------------
TRUE_VALUE      : 'true';
FALSE_VALUE     : 'false';
IF_INSTR        : 'if';
ELSE_INSTR      : 'else';
FOR_INSTR       : 'for';
WHILE_INSTR     : 'while';
FUNC_INSTR      : 'func';
DISPLAY_INSTR   : 'display';
PRINT_INSTR     : 'print';
RETURN_INSTR    : 'return';
PLOT_INSTR      : 'plot';

// --------------- Special Characters -------------
SEMICOLON       : ';';
COMMA           : ',';
ASSIGN          : '=';

PLUS            : '+';
MINUS           : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
MODULO          : '%';

EQUAL           : '==';
NOT_EQUAL       : '!=';
LESS_THAN       : '<';
GREATER_THAN    : '>';
LESS_EQUAL      : '<=';
GREATER_EQUAL   : '>=';

LEFT_PAREN      : '(';
RIGHT_PAREN     : ')';
LEFT_BRACKET    : '[';
RIGHT_BRACKET   : ']';
LEFT_BRACE      : '{';
RIGHT_BRACE     : '}';

// --------------- Identifiers and Numbers ----------------
NUMBER: [0-9]+('.'[0-9]+)?;
STRING: '"' (ESC | ~["\\])* '"';
fragment ESC: '\\' ["\\/bfnrt];

IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;

WHITE_SPACE     : [ \t\r\n]+ -> skip;

COMMENT         : '//' ~[\r\n]* -> skip;
