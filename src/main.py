import sys
import os
from antlr4 import *
from io import StringIO

grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar')
sys.path.append(grammar_path)

from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from errorlistener import EnglishLangErrorListener
from interpreter import Interpreter

# Optional: use your own error listener
# from errorlistener import MyErrorListener

def main():
    # Load input code from input_code.txt
    input_file_path = os.path.join(os.path.dirname(__file__), 'input_code.txt')
    output_path = os.path.join(os.path.dirname(__file__), 'output.txt')
    with open(input_file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # Set up ANTLR input stream
    input_stream = InputStream(code)

    # Initialize lexer and parser
    lexer = EnglishLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EnglishLangParser(token_stream)

    # Optional: Attach custom error listener
    #parser.removeErrorListeners()
    #parser.addErrorListener(errorListener())

    # Parse the input starting from the top-level rule (e.g., 'program')
    tree = parser.program()

        # NEW: Use the interpreter
    visitor = Interpreter()
    output_lines = visitor.visit(tree)

    with open(output_path, 'w', encoding='utf-8') as out_file:
        out_file.write("\n".join(output_lines))

    print("✅ Parsed successfully. Check output.txt for the parse tree.")

if __name__ == '__main__':
    main()
