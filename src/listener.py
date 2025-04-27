from EnglishLangParser import EnglishLangParser
from EnglishLangListener import EnglishLangListener

class VariableDeclarationListener(EnglishLangListener):
    def __init__(self):
        self.variables = {}

    def enterVariableDeclaration(self, ctx: EnglishLangParser.VariableDeclarationContext):
        var_name = ctx.IDENTIFIER().getText()
        var_type = ctx.type_().getText()

        if var_name in self.variables:
            raise Exception(f"Variable '{var_name}' redeclared.")

        self.variables[var_name] = var_type

