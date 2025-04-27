import sys
from antlr4 import *
from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from listener import VariableDeclarationListener
from visitor import EvalVisitor

# Read input code
input_stream = FileStream("input_code.txt")

# Set up lexer and parser
lexer = EnglishLangLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = EnglishLangParser(stream)

# Enable line info in error messages
parser.removeErrorListeners()
parser.addErrorListener(DiagnosticErrorListener())

tree = parser.program()

# First pass: register variables using listener
listener = VariableDeclarationListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)

# Second pass: evaluate using visitor
visitor = EvalVisitor(listener.variables)

# Redirect stdout to a file
original_stdout = sys.stdout
with open("output.txt", "w") as f:
    sys.stdout = f
    visitor.visit(tree)
sys.stdout = original_stdout
