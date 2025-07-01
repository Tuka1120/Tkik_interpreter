
from antlr4 import *
from EnglishLangLexer import EnglishLangLexer
from EnglishLangParser import EnglishLangParser
from EnglishLangParserVisitor import EnglishLangParserVisitor
import math


class BreakStatement:
    pass

class SemanticError(Exception):
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        location = f" at line {self.line}, column {self.column}" if self.line is not None else ""
        return f"❌ Semantic Error{location}:\n❌ {self.message}"

class FunctionReturn(Exception):
    def __init__(self, value):
        self.value = value

class Scope:
    def __init__(self, parent=None):
        self.variables = {}  # map: name -> {"value": ..., "type": ...}
        self.parent = parent

    def set_variable(self, name, value, var_type=None):
        self.variables[name] = {"value": value, "type": var_type}

    def has_variable(self, name):
        return name in self.variables

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]["value"]
        elif self.parent:
            return self.parent.get_variable(name)
        else:
            raise Exception(f"Variable '{name}' not found in any scope")

    def get_variable_type(self, name):
        if name in self.variables:
            return self.variables[name]["type"]
        elif self.parent:
            return self.parent.get_variable_type(name)
        else:
            return None


class Interpreter(EnglishLangParserVisitor):
    def __init__(self):
        super().__init__()
        self.global_scope = Scope()
        self.current_scope = self.global_scope
        self.memory = {}
        self.variables = {}
        self.functions = {}        
        self.output_lines = []
        self.call_stack = []
        self.skip_next_block_scope = False

    def push_env(self, new_scope=None):
        if new_scope:
            new_scope.parent = self.current_scope
            self.current_scope = new_scope
        else:
            self.current_scope = Scope(parent=self.current_scope)
        #print("DEBUG: PUSH — scope now at depth", self.scope_depth())

    def pop_env(self):
        if self.current_scope.parent:
            #print("DEBUG: POP — scope now at depth", self.scope_depth() - 1)
            self.current_scope = self.current_scope.parent
        else:
            raise Exception("Cannot pop global scope")
        
        #if self.scope_depth() == 1:
            #print("DEBUG: At global scope again")


    def scope_depth(self):
        depth = 0
        scope = self.current_scope
        while scope:
            depth += 1
            scope = scope.parent
        return depth

    def set_var(self, name, value):
        scope = self.current_scope
        while scope:
            if scope.has_variable(name):  # ✅ use has_variable here
                scope.set_variable(name, value)
                return
            scope = scope.parent
        # If not found, define in current scope
        self.current_scope.set_variable(name, value)

    def get_var(self, name):
        return self.current_scope.get_variable(name)

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is not None and not isinstance(result, BreakStatement):
                self.output_lines.append(str(result))
        return self.output_lines

    def visitVariableDeclarationOrAssignment(self, ctx):
        is_declaration = ctx.SET() is not None
        type_ctx = ctx.typeAnnotation()
        declared_type = type_ctx.getText().lower() if type_ctx else None

        # Determine if it's scopedIdentifier or simple IDENTIFIER
        if ctx.scopedIdentifier():
            levels = len(ctx.scopedIdentifier().getTokens(EnglishLangParser.PARENT_SCOPE))
            name = ctx.scopedIdentifier().IDENTIFIER().getText()
            target_scope = self.current_scope
            for _ in range(levels):
                if not target_scope.parent:
                    token = ctx.scopedIdentifier().IDENTIFIER().getSymbol()
                    raise SemanticError(f"No parent scope exists for assignment to 'parent::{'::' * levels}{name}'",
                                        line=token.line, column=token.column)
                target_scope = target_scope.parent
        else:
            name = ctx.IDENTIFIER().getText()
            target_scope = self.current_scope


        value = self.visit(ctx.expression())

        if is_declaration:
            if declared_type:
                value = self.cast_value(value, declared_type)
            if target_scope.has_variable(name):
                # error handling
                pass
            target_scope.set_variable(name, value, declared_type)
        else:
            # reassignment: find the variable's declared type from scope chain
            scope = target_scope
            var_type = None
            while scope:
                if scope.has_variable(name):
                    var_type = scope.get_variable_type(name)
                    if var_type:
                        value = self.cast_value(value, var_type)
                    scope.set_variable(name, value, var_type)
                    return None
                scope = scope.parent

            # if not found: error handling
            pass

        return None

    
    def lookup_variable(self, name):
        return self.current_scope.get_variable(name)

    def visitFunctionDeclaration(self, ctx):
        name = ctx.IDENTIFIER().getText()
        param_list = []
        seen_params = set()

        if name in self.functions:
            token = ctx.IDENTIFIER().getSymbol()
            raise SemanticError(
                f"Function '{name}' is already defined.",
                line=token.line,
                column=token.column
            )

        if ctx.parameter():
            for typed_param in ctx.parameter().typedParameter():
                param_name = typed_param.IDENTIFIER().getText()

                if param_name in seen_params:
                    token = typed_param.IDENTIFIER().getSymbol()
                    raise SemanticError(f"Duplicate parameter name '{param_name}' in function '{name}'",
                                        line=token.line, column=token.column)

                seen_params.add(param_name)

                # Extract type string here
                type_ctx = typed_param.typeAnnotation()
                param_type = type_ctx.getText().lower() if type_ctx else None

                param_list.append((param_name, param_type))  # Store tuple of (name, type)

        body = ctx.blockStatement()
        self.functions[name] = {
            "params": param_list,   # Now a list of (name, type)
            "body": body,
            "scope": self.current_scope  
        }
        return None


    def visitFunctionCall(self, ctx):
        #print("New visitFunctionCall reached")

        func_name = ctx.IDENTIFIER().getText()
        args = []

        if ctx.argumentList():
            for expr in ctx.argumentList().expression():
                arg_val = self.visit(expr)
                args.append(arg_val)

        #print(f"Calling function: {func_name} with args: {args}")
        result = self.callFunction(func_name, args)
        return result        

    def callFunction(self, name, args):
        func = self.functions[name]
        param_info = func["params"]   # List of (name, type)
        func_body = func["body"]
        defining_scope = func["scope"]

        if len(param_info) != len(args):
            raise SemanticError(
                f"Function '{name}' expects {len(param_info)} argument(s), but got {len(args)} instead."
            )

        call_scope = Scope(parent=defining_scope)

        for (param_name, param_type), arg_value in zip(param_info, args):
            # Cast argument value to the declared param_type
            casted_value = self.cast_value(arg_value, param_type) if param_type else arg_value
            call_scope.set_variable(param_name, casted_value)

        self.push_env(call_scope)
        self.skip_next_block_scope = True

        try:
            self.visit(func_body)
        except FunctionReturn as rv:
            self.pop_env()
            return rv.value

        self.pop_env()

    def visitBuiltInFunctions(self, ctx):
        if ctx.POWER_FUNC():
            base = self.visit(ctx.numExpression(0))
            exponent = self.visit(ctx.numExpression(1))
            return math.pow(base, exponent)

        elif ctx.SIN_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.sin(value)

        elif ctx.COS_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.cos(value)

        elif ctx.TAN_FUNC():
            value = self.visit(ctx.numExpression(0))
            return math.tan(value)

        elif ctx.CTAN_FUNC():
            value = self.visit(ctx.numExpression(0))
            tan_val = math.tan(value)
            if tan_val == 0:
                raise ZeroDivisionError("Cotangent undefined: tan(value) = 0")
            return 1 / tan_val

        else:
            raise Exception("Unknown built-in function")


    def visitIdentifier(self, ctx):
        var_name = ctx.getText()

        if not self.current_scope.has_variable(var_name):
            if self.current_scope.parent and self.current_scope.parent.has_variable(var_name):
                token = ctx.start
                raise SemanticError(
                    f"Variable '{var_name}' is not declared in the current scope. "
                    f"Did you mean 'parent::{var_name}'?",
                    line=token.line,
                    column=token.column
                )
            else:
                token = ctx.start
                raise SemanticError(
                    f"Variable '{var_name}' is not declared in the current scope.",
                    line=token.line,
                    column=token.column
                )

        return self.current_scope.get_variable(var_name)

    def visitScopedIdentifier(self, ctx):
        levels = len(ctx.getTokens(EnglishLangParser.PARENT_SCOPE))
        name = ctx.IDENTIFIER().getText()
        token = ctx.IDENTIFIER().getSymbol()

        current_scope = self.current_scope
        for _ in range(levels):
            if current_scope.parent is None:
                raise SemanticError(
                    f"Too many 'parent::' levels when accessing variable '{name}'",
                    line=token.line,
                    column=token.column
                )
            current_scope = current_scope.parent

        try:
            value = current_scope.get_variable(name)
        except Exception:
            raise SemanticError(
                f"Variable '{name}' not found in the specified parent scope",
                line=token.line,
                column=token.column
            )
        return value
    
    def visitBlockStatement(self, ctx):
        if self.skip_next_block_scope:
            self.skip_next_block_scope = False  # reset the flag
            for stmt in ctx.statement():
                self.visit(stmt)
            return  # DO NOT push/pop

        self.push_env()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.pop_env()

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expression())
        raise FunctionReturn(value)

    def visitStatement(self, ctx):
        result = self.visitChildren(ctx)

        if ctx.functionCall() and result is not None:
            #print("DEBUG: Standalone function call result:", result)
            self.output_lines.append(f"Result: {result}")

        return result

    def visitDisplayStatement(self, ctx):
        expressions = ctx.expression()
        results = [self.visit(expr) for expr in expressions]
        display_output = ' '.join(str(r) for r in results)
        print("DEBUG: Displaying", results)
        self.output_lines.append(display_output)
        return None

    def visitNumExpression(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if op == '+':
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                else:
                    return left + right
            elif op == '-':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left - right
                else:
                    raise TypeError(f"Unsupported operand types for -: {type(left)} and {type(right)}")
        return self.visit(ctx.getChild(0))

    def visitTerm(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '%':
                return left % right
        return self.visit(ctx.getChild(0))

    def visitUnaryPlus(self, ctx):
        return +self.visit(ctx.factor())

    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.factor())

    def visitFactorNumber(self, ctx):
        text = ctx.NUMBER().getText()
        if '.' in text:
            return float(text)
        else:
            return int(text)


    def visitFactorIdentifier(self, ctx):
        name = ctx.IDENTIFIER().getText()
        return self.lookup_variable(name)

    def visitFactorString(self, ctx):
        return ctx.STRING().getText().strip('"')

    def visitFactorParens(self, ctx):
        return self.visit(ctx.numExpression())

    def visitFactorFunctionCall(self, ctx):
        return self.visit(ctx.functionCall())

    def visitFactorOperation(self, ctx):
        return self.visit(ctx.operation())
    
    def visitFactorscopedIdentifier(self, ctx):
        return self.visit(ctx.scopedIdentifier())

    def visitOperation(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        if var_name not in self.memory:
            raise Exception(f"Variable '{var_name}' not defined.")

        current_value = self.memory[var_name]
        if not isinstance(current_value, (int, float)):
            raise Exception(f"Cannot increment/decrement non-numeric variable '{var_name}'.")

        if ctx.INCREMENT():
            self.memory[var_name] = current_value + 1
        elif ctx.DECREMENT():
            self.memory[var_name] = current_value - 1

        return self.memory[var_name]
    
    def visitNumComparison(self, ctx):
        left = self.visit(ctx.numExpression(0))
        right = self.visit(ctx.numExpression(1))
        op = ctx.comparisonOp().getText()
        return self.evaluateBinaryOp(left, right, op)

    def visitStringComparison(self, ctx):
        left = self.visit(ctx.stringExpression(0))
        right = self.visit(ctx.stringExpression(1))
        op = ctx.getChild(1).getText()
        return (left == right) if op == "==" else (left != right)

    def visitMatrixComparison(self, ctx):
        left = self.visit(ctx.matrixExpression(0))
        right = self.visit(ctx.matrixExpression(1))
        op = ctx.getChild(1).getText()
        return (left == right) if op == "==" else (left != right)

    def transpose_matrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def invert_matrix(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise Exception("Only 2x2 matrix inversion supported")

        a, b = matrix[0]
        c, d = matrix[1]
        determinant = a * d - b * c

        if determinant == 0:
            raise Exception("Matrix is not invertible")

        inverse = [
            [d / determinant, -b / determinant],
            [-c / determinant, a / determinant]
        ]
        return inverse

    def visitMatrixExpression(self, ctx):
        matrix = self.visit(ctx.matrixAtom())

        if ctx.INVERT_MATRIX():
            return self.invert_matrix(matrix)

        if ctx.TRANSPOSITION():
            return self.transpose_matrix(matrix)

        return matrix

    def visitMatrixAtom(self, ctx):
        if ctx.IDENTIFIER():
            return self.lookup_variable(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.matrixConstruction())

    def visitMatrixConstruction(self, ctx):
        rows = []
        for rowCtx in ctx.row():
            row = [self.visit(value) for value in rowCtx.value()]
            rows.append(row)
            #print("DEBUG row:", row)
        return rows

    def visitValue(self, ctx):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            if '.' in text:
                return float(text)
            else:
                return int(text)
        elif ctx.IDENTIFIER():
            value = self.lookup_variable(ctx.IDENTIFIER().getText())
            if isinstance(value, list) and any(isinstance(row, list) for row in value):
                raise Exception("Matrix cannot contain another matrix as an element")
            return value
        elif ctx.matrixExpression():
            raise Exception("Matrix cannot contain another matrix as an element")
        else:
            raise Exception("Invalid matrix value: must be a number or scalar variable")

    def visitCastExpression(self, ctx):
        type_str = ctx.typeAnnotation().getText().lower()
        value = self.visit(ctx.factor())
        return self.cast_value(value, type_str)

    def cast_value(self, value, type_str):
        if type_str == "int":
            return int(float(value))  # float → int works
        elif type_str == "float":
            return float(value)
        elif type_str == "bool":
            if isinstance(value, str):
                return value.lower() == "true"
            return bool(value)
        elif type_str == "string":
            return str(value)
        elif type_str == "matrix":
            # Assume matrix casting is only allowed on proper nested lists
            if isinstance(value, list) and all(isinstance(row, list) for row in value):
                return value
            raise Exception("Invalid matrix format")
        else:
            raise Exception(f"Unknown type: {type_str}")

    def visitBoolExpression(self, ctx):
        return self.visitChildren(ctx)

    def visitLogicOr(self, ctx):
        for i in range(len(ctx.boolAndExpression())):
            if self.visit(ctx.boolAndExpression(i)):
                return True
        return False

    def visitLogicAnd(self, ctx):
        for i in range(len(ctx.boolNotExpression())):
            if not self.visit(ctx.boolNotExpression(i)):
                return False
        return True

    def visitLogicNot(self, ctx):
        return not self.visit(ctx.boolNotExpression())

    def visitLogicPrimaryWrap(self, ctx):
        return self.visit(ctx.boolPrimary())

    def visitLogicParen(self, ctx):
        return self.visit(ctx.boolExpression())

    def visitTrueLiteral(self, ctx):
        return True

    def visitFalseLiteral(self, ctx):
        return False

    def visitLogicIdentifier(self, ctx):
        name = ctx.IDENTIFIER().getText()
        return bool(self.lookup_variable(name))

    def visitIfStatement(self, ctx):
        if self.visit(ctx.boolExpression(0)):
            stmt_or_block = ctx.statement(0) or ctx.blockStatement(0)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        for i in range(len(ctx.ELSE_IF())):
            if self.visit(ctx.boolExpression(i + 1)):
                stmt_or_block = ctx.statement(i + 1) or ctx.blockStatement(i + 1)
                if stmt_or_block:
                    return self.visit(stmt_or_block)

        if ctx.ELSE():
            num_ifs = 1 + len(ctx.ELSE_IF())
            stmt_or_block = ctx.statement(num_ifs) or ctx.blockStatement(num_ifs)
            if stmt_or_block:
                return self.visit(stmt_or_block)

        return None

    def visitBreakStatement(self, ctx):
        return BreakStatement()
    
    def visitLoopStatements(self, ctx):
        if ctx.loopStatement():
            return self.visit(ctx.loopStatement())
        elif ctx.variableDeclarationOrAssignment():
            return self.visit(ctx.variableDeclarationOrAssignment())
        elif ctx.functionDeclaration():
            return self.visit(ctx.functionDeclaration())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.blockStatement():
            return self.visit(ctx.blockStatement())
        elif ctx.displayStatement():
            return self.visit(ctx.displayStatement())

    def visitWhileLoop(self, ctx):
        while self.visit(ctx.boolExpression()):
            self.push_env()  

            for stmt in ctx.loopStatements():
                result = self.visit(stmt)
                if isinstance(result, BreakStatement):
                    self.pop_env()
                    return
                if result is not None:
                    self.pop_env()
                    return result

            self.pop_env()  
        return None

            
    def visitForLoop(self, ctx):
        if ctx.forInit():
            self.visit(ctx.forInit())

        while self.visit(ctx.cond): 
            self.push_env()  

            result = self.visit(ctx.forBody())
            if isinstance(result, BreakStatement):
                self.pop_env()
                return

            self.pop_env()

            self.visit(ctx.forUpdate())


    def evaluateBinaryOp(self, left, right, op):
        if op == '+': return left + right
        elif op == '-': return left - right
        elif op == '*': return left * right
        elif op == '/': return left / right
        elif op == '%': return left % right
        elif op == '<': return left < right
        elif op == '>': return left > right
        elif op == '==': return left == right
        elif op == '!=': return left != right
        elif op == '<=': return left <= right
        elif op == '>=': return left >= right
        else: raise Exception(f"Unknown operator {op}")

    def visitExpression(self, ctx):
        if ctx.numExpression():
            return self.visit(ctx.numExpression())
        elif ctx.boolExpression():
            return self.visit(ctx.boolExpression())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.builtInFunctions():
            return self.visit(ctx.builtInFunctions())
        elif ctx.matrixExpression():
            return self.visit(ctx.matrixExpression())
        elif ctx.stringExpression():
            return self.visit(ctx.stringExpression())
        elif ctx.scopedIdentifier():
            return self.visit(ctx.scopedIdentifier())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.lookup_variable(name)
        return None
