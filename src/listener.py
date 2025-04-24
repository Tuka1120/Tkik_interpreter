from EnglishLangParser import EnglishLangParser
from EnglishLangParserListener import EnglishLangParserListener

class VariableCollector(EnglishLangParserListener):
    def __init__(self):
        self.variables = {}

    def enterDeclareStmt(self, ctx: EnglishLangParser.DeclareStmtContext):
        var_name = ctx.ID().getText()
        var_type = ctx.type().getText()

        if var_name in self.variables:
            raise Exception(f"Variable '{var_name}' redeclared.")

        self.variables[var_name] = var_type

