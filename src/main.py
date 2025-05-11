import sys
import os
from antlr4 import *
from io import StringIO

# Add grammar path
grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar')
sys.path.append(grammar_path)

from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from errorlistener import EnglishLangErrorListener
from interpreter import Interpreter

def main():
    input_file_path = os.path.join(os.path.dirname(__file__), 'input_code.txt')
    output_path = os.path.join(os.path.dirname(__file__), 'output.txt')

    with open(input_file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    input_stream = InputStream(code)

    lexer = EnglishLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EnglishLangParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(EnglishLangErrorListener())

    try:
        tree = parser.program()
        visitor = Interpreter()
        output_lines = visitor.visit(tree)
    except SyntaxError as e:
        print(e)
        return
    
    with open(output_path, 'w', encoding='utf-8') as out_file:
        if isinstance(output_lines, list):
            out_file.write("\n".join(str(line) for line in output_lines))
        else:
            out_file.write(str(output_lines))

    print("Parsed successfully.")

if __name__ == '__main__':
    main()
