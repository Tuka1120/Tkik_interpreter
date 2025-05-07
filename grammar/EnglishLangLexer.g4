lexer grammar EnglishLangLexer;

// Keywords
START_PROGRAM : 'Start Program';
END_PROGRAM   : 'End Program';
DEFINE_FUNCTION : 'Define Function';
END_FUNCTION : 'End Function';
RETURN : 'Return';
CALL : 'Call';
WITH : 'with';
SET : 'Set';
TO : 'to';
DISPLAY : 'Display';
IF : 'If';
ELSE_IF : 'Else If';
ELSE : 'Else';
END_IF : 'End If';
FOR_EACH : 'For each';
FROM : 'from';
IN : 'in';
END_FOR : 'End For';
WHILE : 'While';
END_WHILE : 'End While';
INCREMENT : 'Increment';
BY : 'by';

// Operators
PLUS      : '+';
MINUS     : '-';
TIMES     : '*';
DIVIDED_BY: '/';
MODULO    : '%';
EQUALS    : '==';
GREATER_THAN : '>';
LESS_THAN    : '<';
GREATER_EQUAL: '>=';
LESS_EQUAL   : '<=';

// Punctuation
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
NUMBER : [0-9]+ ('.' [0-9]+)?;
STRING : '"' (~["\r\n])* '"';

TYPE_INT    : 'int';
TYPE_STRING : 'string';
TYPE_BOOL   : 'bool';


// Identifiers
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

// Whitespace & Comments
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
