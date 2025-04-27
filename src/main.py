from antlr4 import FileStream, CommonTokenStream
from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, input_file, output_file):
        # Read input file and initialize lexer and parser
        input_stream = FileStream(input_file)
        lexer = EnglishLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = EnglishLangParser(token_stream)

        # Parse the input and get the parse tree
        tree = parser.program()

        # Open output file for writing
        with open(output_file, 'w') as output:
            # Walk through the parse tree manually and interpret
            self.walk(tree, output)

    def walk(self, tree, output):
        # Check if the tree is a terminal node (leaf)
        if isinstance(tree, TerminalNodeImpl):
            # If it's a terminal node, process it directly
            return

        # If it's not a terminal node, process its children
        for child in tree.getChildren():
            if isinstance(child, EnglishLangParser.AssignmentContext):
                self.handle_assignment(child)
            elif isinstance(child, EnglishLangParser.PrintStatementContext):
                self.handle_print(child, output)
            elif isinstance(child, EnglishLangParser.FuncDeclContext):
                self.handle_func_decl(child)
            # Add more conditions as necessary based on your grammar
            else:
                self.walk(child, output)

    def handle_assignment(self, ctx):
        # Handle variable assignments
        var_name = ctx.IDENTIFIER().getText()
        var_type = ctx.typeName().getText() if ctx.typeName() else "unknown"

        # Get the assigned value (it should be a number or an expression)
        value = self.evaluate_expression(ctx.expression())

        if var_name in self.variables:
            raise Exception(f"Variable '{var_name}' redeclared.")

        # Store the variable and its value
        self.variables[var_name] = value

    def evaluate_expression(self, expr):
        # Evaluate simple expressions (like a number or variable)
        if expr.NUMBER():
            return float(expr.NUMBER().getText())  # Return the numeric value of the number
        elif expr.IDENTIFIER():
            var_name = expr.IDENTIFIER().getText()
            if var_name in self.variables:
                return self.variables[var_name]  # Return the value of the variable
            else:
                raise Exception(f"Variable '{var_name}' not declared.")
        elif expr.STRING():
            return expr.STRING().getText()[1:-1]  # Return the string value without quotes
        # Add more cases here if needed for more complex expressions
        return None

    def handle_print(self, ctx, output):
        # Handle the print statements
        expression = ctx.expression()
        if expression:
            # If the expression is a variable, get its value
            if expression.IDENTIFIER():
                var_name = expression.IDENTIFIER().getText()
                if var_name in self.variables:
                    # Output the value of the variable
                    output.write(f"{self.variables[var_name]}\n")
                else:
                    output.write(f"Error: Variable '{var_name}' not declared\n")
            # If the expression is a string, output the string
            elif expression.STRING():
                output.write(f"{expression.STRING().getText()[1:-1]}\n")  # Remove quotes
            else:
                # If it's a number or other expression type, evaluate and print
                output.write(f"{expression.getText()}\n")
        else:
            output.write("Error: Invalid print expression\n")

    def handle_func_decl(self, ctx):
        # Handle function declarations
        func_name = ctx.IDENTIFIER().getText()
        # You can add more logic to process function declarations here

    # Add more handlers for other grammar rules if necessary

# Run the interpreter
if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.interpret("input_code.txt", "output.txt")  # Replace with your file

    # After running, you can check the output in the "output.txt" file.
