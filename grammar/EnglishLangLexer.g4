lexer grammar EnglishLangLexer;

// Keywords
START_PROGRAM : 'Start Program';
END_PROGRAM   : 'End Program';
DEFINE_FUNCTION : 'Define Function';
END_FUNCTION : 'End Function';
RETURN : 'Return';
CALL : 'Call';
SET : 'Set';
TO : 'to';
DISPLAY : 'Display';
IF : 'If';
ELSE_IF : 'Else If';
ELSE : 'Else';
END_IF : 'End If';
FOR : 'For';
FROM : 'from';
IN : 'in';
END_FOR : 'End For';
BREAK  : 'break';
WHILE : 'While';
END_WHILE : 'End While';
INVERT_MATRIX : 'invert';
TRANSPOSITION : '\'T';
PARENT_SCOPE: 'parent';
DCOLON: '::';


// Operators
PLUS      : '+';
MINUS     : '-';
MULTIPLY     : '*';
DIVIDED_BY: '/';
MODULO    : '%';
EQUALS    : '==';
GREATER_THAN : '>';
LESS_THAN    : '<';
GREATER_EQUAL: '>=';
LESS_EQUAL   : '<=';
ADD_TO          : '+=';
SUBTRACT_FROM   : '-=';
INCREMENT       : '++';
DECREMENT       : '--';
TIMES           : '*=';
DIVIDE_FROM     : '/=';
NOT_EQUALS : '!=';
AND        : 'and';
OR         : 'or';
NOT           : 'not';

// Punctuation
SEMICOLON : ';';
COMMA : ',';
COLON : ':';
DOT   : '.';
QUOTE : '"';
LBRACK : '[';
RBRACK : ']';
LBRACE : '{';
RBRACE : '}';
LPAREN : '(';
RPAREN : ')';

// Literals
NUMBER : [-]? [0-9]+ ('.' [0-9]+)?;
STRING : '"' (~["\r\n])* '"';

TYPE_INT    : 'int';
TYPE_STRING : 'string';
TYPE_BOOL   : 'bool';
TYPE_FLOAT    : 'float';
TYPE_MATRIX     : 'matrix';
TYPE_VOID       : 'void';
TRUE_VALUE      : 'true';
FALSE_VALUE     : 'false';

POWER_FUNC      : 'pow';
SIN_FUNC        : 'sin';
COS_FUNC        : 'cos';
TAN_FUNC        : 'tan';
CTAN_FUNC       : 'ctan';

// Identifiers
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

// Whitespace & Comments
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
