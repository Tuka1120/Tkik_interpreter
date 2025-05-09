from antlr4.error.ErrorListener import ErrorListener

class EnglishLangErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"❌ Syntax Error at line {line}, column {column}: {msg}"
        raise SyntaxError(error_message)
