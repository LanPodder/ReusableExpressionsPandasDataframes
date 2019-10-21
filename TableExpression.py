class TableExpression:
    def __init__(self):
        self.expressionmap = {}
    
    def add_condition(self, key, expression):
        self.expressionmap[key] = expression
    
    def allmatch(self, checkmap):
        for key in self.expressionmap:
            if(not self.expressionmap[key](checkmap[key])):
                return False
        return True
    
    def anymatch(self, checkmap):
        for key in self.expressionmap:
            if(self.expressionmap[key](checkmap[key])):
                return True
        return False