from antlr4.error.ErrorListener import ErrorListener

class EnglishLangErrorListener(ErrorListener):
    def __init__(self, source_code=None):
        super().__init__()
        self.source_code = source_code.splitlines() if source_code else []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        actual_line_index = max(0, line - 1)
        code_line = self.source_code[actual_line_index] if actual_line_index < len(self.source_code) else ""
        pointer = " " * column + "^"

        offending_text = str(offendingSymbol).strip()
        if offending_text and offending_text in code_line:
            column = code_line.find(offending_text)
            pointer = " " * column + "^"

        suggestion = self._get_suggestion(msg, offending_text)

        error_message = (
            f"❌ Syntax Error at line {line}, column {column}:\n"
            f"❌ Code: {code_line}\n"
            f"❌        {pointer}\n"
            f"❌ Reason: {msg}\n"
            f"❌ Suggestion: {suggestion}"
        )
        raise SyntaxError(error_message)

    def _get_suggestion(self, msg, offending_text):
        if "no viable alternative" in msg:
            return f"Check expression before '{offending_text}' for missing or extra elements."
        if "mismatched input" in msg:
            return f"Unexpected token '{offending_text}'. Did you forget something before it?"
        return "Check the syntax near the highlighted area."