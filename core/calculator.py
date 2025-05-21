class Calculator:
    def __init__(self, on_display_update, on_display_clear):
        self.expression = ""
        self.on_display_update = on_display_update
        self.on_display_clear = on_display_clear

    def add_input(self, value: str):
        if(value == '='):
            self.evaluate_expression()
        elif(value == 'C'):
            self.clear_expression()
        elif(value == '<-'):
            self.expression = self.expression[:-1]
            self.on_display_update(self.expression)
        else:
            self.expression += value
            self.on_display_update(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.on_display_clear()

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.on_display_update(self.expression)
        except Exception as e:
            self.expression = "Error"
            self.on_display_update(self.expression)