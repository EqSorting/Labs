import tkinter as tk
import re

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Графический калькулятор")
        self.geometry("320x450")
        self.resizable(True, True)
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ('(', 1, 0), (')', 1, 1), ('C', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2, 2)
        ]

        for (text, row, col, colspan) in [(b[0], b[1], b[2], 1) if len(b) == 3 else b for b in buttons]:
            button = tk.Button(self, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display()
        elif char == '=':
            if self.is_valid_expression(self.expression):
                try:
                    result = str(eval(self.expression))
                    self.expression = result
                    self.update_display()
                except Exception:
                    self.expression = ""
                    self.update_display("Ошибка")
            else:
                self.expression = ""
                self.update_display("Ошибка")
        else:
            self.expression += char
            self.update_display()

    def is_valid_expression(self, expr):
        if not expr:
            return False
        expr = expr.replace(" ", "")
        if re.search(r"[^0-9+\-*/().]", expr):
            return False

        if not self.parentheses_balanced(expr):
            return False

        tokens = re.findall(r"[+\-*/()]|[0-9.]+", expr)
        prev_op = False
        for i, token in enumerate(tokens):
            if token in "+*/":
                if prev_op:
                    return False
                prev_op = True
            elif token == "-":
                if i == 0:
                    prev_op = False
                else:
                    prev_op = tokens[i-1] in "+-*/("
            elif token == "(":
                prev_op = False
            elif token == ")":
                if prev_op:
                    return False
                prev_op = False
            else:
                prev_op = False

        if expr[-1] in "+-*/(":
            return False

        return True

    def parentheses_balanced(self, expr):
        stack = []
        for char in expr:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def update_display(self, text=None):
        if text is None:
            text = self.expression
        self.display.delete(0, tk.END)
        self.display.insert(0, text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
