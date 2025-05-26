primaryOperators = ['+', '-']
secondaryOperators = ['*', '/','√', '^']
allOperators = primaryOperators + secondaryOperators

import math 
class Calculator:
    def __init__(self, on_display_update, on_display_clear):
        self.expression = ""
        self.onDecimal = False
        self.onError = False
        self.on_display_update = on_display_update
        self.on_display_clear = on_display_clear
        self.isSquareRoot = False

    def input(self, value: str):
        if self.onError:
            self.onError = False
            self.clear_expression()
        if(value == '='):
            if self.can_evaluate():
                result = self.evaluate_expression()
                if self.isSquareRoot:
                    self.isSquareRoot = False
                if result == "Error":
                    self.onError = True
                self.expression = result
                self.on_display_update(self.expression)
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
            if self.expression[len(self.expression) - 1] == '√':
                self.isSquareRoot = False
                self.expression = self.expression[:-1]
            elif self.onDecimal and self.expression[len(self.expression) - 1] == '.':
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
            elif value == '√':
                self.isSquareRoot = True
                return True
            elif value in secondaryOperators:
                return False
            elif value == '.':
                self.onDecimal = True
                self.addOnExpression('0')
                return True
            else:
                return True
        else:
            if value == '√':
                return False
            if self.expression[len(self.expression) - 1] == '.' and value in allOperators:
                return False
            if self.onDecimal and value == '.':
                return False
            if value in secondaryOperators:
                if self.expression[len(self.expression) - 1] in allOperators:
                    return False
                else:
                    self.onDecimal = False
                    return True
            if value in primaryOperators:
                if self.expression[len(self.expression) - 1] == '√':
                    return True
                if self.expression[len(self.expression) - 2] in allOperators and self.expression[len(self.expression) - 1] in allOperators:
                    return False
                else:
                    self.onDecimal = False
                    return True
            if value == '.':
                if self.onDecimal:
                    return False
                else:
                    self.onDecimal = True
                    if self.expression[len(self.expression) - 1] in allOperators:
                        self.addOnExpression('0')
                    return True                
        return True
        
    def can_evaluate(self):
        if len(self.expression) == 0 or self.onError or self.expression is None or self.expression == '':
            return False
        if self.expression[len(self.expression) - 1] in allOperators or self.expression[len(self.expression) - 1] == '.':
            return False
        if not any(c in self.expression for c in allOperators):
            return False
        else:
            return True

    def evaluate_expression(self):
        try:
            self.expression = self.expression.replace('^', '**')
            if self.isSquareRoot:
                self.expression = self.expression.replace('√', '')
            result = eval(self.expression)
            if self.isSquareRoot:
                result = math.sqrt(result)
            return str(result)
        except Exception as e:
            print(e)
            return "Error"