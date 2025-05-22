import tkinter as tk
from core.calculator import Calculator
FONT = "Calibri"


class CalculatorUI:
    def __init__(self):
        self.window = tk.Tk()
        self.calculator = Calculator(on_display_clear=self._clear_display, on_display_update=self._update_display)
        self.window.title("Calculadora")
        self.window.geometry("300x400")
        self.window.iconbitmap(False, "./lib/icon.ico")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.window, font=(FONT, 20), borderwidth=3, relief="ridge", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('^', 5, 1), ('<-', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col, colspan) in [b if len(b) == 4 else (*b, 1) for b in buttons]:
            button = tk.Button(self.window, text=text, font=(FONT, 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        self.calculator.input(value)

    def _clear_display(self):
        self.display.delete(0, tk.END)

    def _update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, value)

    def run(self):
        self.window.mainloop()