import sqlparse


class SQLParser():
    def __init__(self, whiteList):
        self.whitelistString = whiteList
        self.whitelist = set(whiteList.split(','))

    def parse(self, query):
        pOut = sqlparse.parse(query.upper())
        for res in pOut:
            self.__traverseAST(res.tokens)

    def __traverseAST(self, tokens):
        for token in tokens:
            if type(token).__name__ == 'Function':
                self.__checkWhiteList(token)
            if token.is_group:
                self.__traverseAST(token.tokens)

    def __checkWhiteList(self, token):
        fName = token.tokens
        fName = fName[0].value
        if fName not in self.whitelist:
            message = "Expression '" + fName + \
                "' not found in the allowed list: " + self.whitelistString
            raise Exception(message)
