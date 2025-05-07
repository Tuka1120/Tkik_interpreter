from antlr4.error.ErrorListener import ErrorListener

class EnglishLangErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}, column {column}: {msg}")
