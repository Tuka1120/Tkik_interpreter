
# EnglishLang Interpreter – Documentation and Implementation Report

## 1. End-user Documentation

### 1.1 Installation

#### System Requirements
- Python: 3.7 or higher
- ANTLR4: Version 4.9.3 or higher
- Java: Java 8 or higher (for grammar generation)
- Dependencies:
  ```bash
  pip install antlr4-python3-runtime
  ```

#### Step-by-step Installation Guide

1. Clone the Repository:
   ```bash
   git clone <your-repo-url>
   cd your-repo-name
   ```

2. Install Python Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up ANTLR:
   - Download the ANTLR jar from: https://www.antlr.org/download.html
   - Example alias setup:
     ```bash
     alias antlr4='java -jar antlr-4.9.3-complete.jar'
     ```

4. Generate Lexer and Parser:
   ```bash
   antlr4 -Dlanguage=Python3 EnglishLangLexer.g4 EnglishLangParser.g4 -visitor
   ```

5. Run the Interpreter:
   ```bash
   python main.py
   ```

### 1.2 Getting Started

#### Writing Input Code
- Write your program in `input_code.txt`.
- Example:
  ```
  Set x to 10
  Set y to 20
  Display x + y
  ```

#### Running the Interpreter
```bash
python main.py
```

#### Output
- The result is saved in `output.txt`.
- Console output: `Parsed successfully.`

### 1.3 Language Syntax and Features

#### Supported Data Types
- int, float, bool, string, matrix

#### Variable Declaration
```text
Set x to 10 int
Set name to "Alice" string
Set y to 3.14 float
```

#### Type Annotations (Optional)
```text
Set grid [1, 2; 3, 4] matrix
```

#### Scoped Variables
Use `parent::` to access variables in outer scopes:
```text
Display parent::x
```

### 1.4 Control Structures

#### Conditional Statements
```text
If (x > 0)
    Display "Positive"
Else If x < 0
    Display "Negative"
Else
    Display "Zero"
End If
```

#### Loops

While Loop:
```text
While (x < 5) {
    Display x
    Set x to x + 1
}
```

For Loop:
```text
Set i to 0
For (Set j to 10; j > 0; Set j to j - 1)
{
    If (j / 2 == 0)
        Display "Even:", j
    Else
        Display "Odd:", j

    Set i to i + 1
}
```

### 1.5 Functions

#### Function Declaration
```text
Define Function add(a, b)
    Return a + b
End Function
```

#### Function Calls
```text
Call add(5, 10)
```

### 1.6 Built-in Operations

- Arithmetic: +, -, *, /, %
- Comparison: ==, !=, <, >, <=, >=
- Logical: and, or, not
- Increment/Decrement: ++, --
- Matrix: invert, 'T (transpose)

### 1.7 Input/Output

#### Displaying Output
```text
Display "Hello", x
```
Output is saved to `output.txt` line by line.

### 1.8 Error Handling

#### Common Syntax Errors
The interpreter raises syntax errors with helpful messages:
```
Syntax Error at line 3, column 5:
Code: Set x 10
        ^ 
Reason: mismatched input '10' expecting 'to'
Suggestion: Unexpected token '10'. Did you forget something before it?
```

### 1.9 Example Programs

#### Factorial Function
```text
Define Function factorial(n)
    If n <= 1
        Return 1
    Else
        Return n * Call factorial(n - 1)
    End If
End Function

Set x to 5
Set result to Call factorial(x)
Display result
```

#### Matrix Display
```text
Declare mat as matrix = [[1, 2], [3, 4]]
Display mat
```

## 2. Implementation Report

### 2.1 Project Overview

#### Purpose
Build an interpreter for a human-readable pseudocode-style language using Python and ANTLR4.

#### Architecture
- ANTLR Lexer & Parser: Grammar-based tokenization and parsing
- Interpreter: Python class (`Interpreter`) that evaluates the parse tree
- ErrorListener: Custom syntax checker for clear feedback

### 2.2 ANTLR Grammar

#### Lexer (EnglishLangLexer.g4)
Defines tokens such as:
- Keywords: Set, If, Else, Function, etc.
- Operators: +, -, *, /, ++, --
- Literals: NUMBER, STRING
- Comments & Whitespace: Skipped via `WS` and `COMMENT`

#### Parser (EnglishLangParser.g4)
Defines rules for:
- Statements: assignments, display, conditionals
- Expressions: arithmetic, boolean, function calls
- Function definitions and loops
- Scoping and type annotations

### 2.3 Interpreter Implementation

#### Core Class: `Interpreter`
Inherits from `EnglishLangParserVisitor`.

#### Scope Management
- `Scope` class allows for nested variable resolution.
- `self.current_scope` is pushed/popped for functions and blocks.

#### Variable and Memory
- `self.memory` stores typed variable values.
- `self.variables` and `self.output_lines` manage runtime data.

#### Function Mechanics
- `callFunction(name, args)` handles execution and scope.

#### Visitor Pattern
Implements methods such as:
- `visitAssignment`
- `visitFunctionCall`
- `visitDisplayStatement`
- `visitIfStatement`, `visitForLoop`, etc.

### 2.4 Error Handling

#### Custom Error Listener
- `EnglishLangErrorListener` displays line, column, offending code, and suggestions.

Example:
```
Unexpected token 'End'. Did you forget something before it?
```

### 2.5 Memory and Variable Management

- Variables stored in `Scope` instances.
- Lookups use parent chaining to support `parent::x` syntax.

### 2.6 Challenges and Solutions

| Challenge                        | Solution                                                     |
|----------------------------------|--------------------------------------------------------------|
| Scoped variables in nested blocks | Implemented Scope class with parent chaining                 |
| Ambiguity in grammar             | Fine-tuned rule precedence and structure                     |
| User-friendly error messages     | Created custom listener with contextual diagnostics          |
| Matrix validation                | Type-checked nested list structures                          |

### 2.7 Testing and Validation

#### Methodology
- Run sample programs through `input_code.txt`.
- Validate against `output.txt` results.

#### Example Test Case
```text
Set a to 5
Set b to 10
Display a + b
```
Expected Output:
```
15
```

### 2.8 Future Improvements

- Add support for additional data structures (arrays, dictionaries)
- File I/O and command-line arguments
- Enhanced type inference and static checking
- IDE integration or web-based interface

---
