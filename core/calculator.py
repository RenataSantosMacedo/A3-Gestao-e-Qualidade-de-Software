primaryOperators = ['+', '-']
secondaryOperators = ['*', '/', '√', '^']
allOperators = primaryOperators + secondaryOperators

class Calculator:
    def __init__(self, on_display_update, on_display_clear):
        self.expression = ""
        self.onDecimal = False
        self.onError = False
        self.on_display_update = on_display_update
        self.on_display_clear = on_display_clear

    def input(self, value: str):
        if self.onError:
            self.onError = False
            self.clear_expression()
        if(value == '='):
            self.evaluate_expression()
        elif(value == 'C'):
            self.clear_expression()
        elif(value == '<-'):
            self.backspace()
        else:
            if self.canAddThisInput(value):
                self.addOnExpression(value)

    def addOnExpression(self, value: str):
        self.expression += value
        self.on_display_update(self.expression)

    def backspace(self):
        if len(self.expression) > 0:
            if self.onDecimal and self.expression[len(self.expression) - 1] == '.':
                if self.expression[len(self.expression) - 2] == '0':
                    self.expression = self.expression[:-2]
                else:
                    self.expression = self.expression[:-1]
                self.onDecimal = False
            elif self.expression[len(self.expression) - 1] in allOperators and self.expression[len(self.expression) - 2] not in allOperators:
                if '.' in self.expression:
                    self.expression = self.expression[:-1]
                    self.onDecimal = True
                else:
                    self.expression = self.expression[:-1]
            else:
                self.expression = self.expression[:-1]
            self.on_display_update(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.on_display_clear()

    def canAddThisInput(self, value: str):
        if len(self.expression) == 0:
            if value == '0':
                return False
            elif value in secondaryOperators:
                return False
            elif value == '.':
                self.onDecimal = True
                self.addOnExpression('0')
                return True
            else:
                return True
        else:
            if self.expression[len(self.expression) - 1] == '.' and value in allOperators:
                return False
            if self.onDecimal and value == '.':
                return False
            elif value in secondaryOperators:
                if self.expression[len(self.expression) - 1] in allOperators:
                    return False
                else:
                    self.onDecimal = False
                    return True
            elif value in primaryOperators:
                if self.expression[len(self.expression) - 2] in allOperators and self.expression[len(self.expression) - 1] in allOperators:
                    return False
                else:
                    self.onDecimal = False
                    return True
            elif value == '.':
                if self.onDecimal:
                    return False
                else:
                    self.onDecimal = True
                    if self.expression[len(self.expression) - 1] in allOperators:
                        self.addOnExpression('0')
                    return True                
        return True
        

        



    def can_evaluate(self):
        try:
            eval(self.expression)
            return True
        except:
            return False

    def evaluate_expression(self):
        if self.can_evaluate():
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.on_display_update(self.expression)
            except Exception as e:
                print(e)
                self.expression = "Error"
                self.onError = True
                self.on_display_update(self.expression)