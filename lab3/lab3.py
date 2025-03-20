import re

def calculate(expression):
    if not re.match(r'^[\d\+\-\*\/\^\. ]+$', expression):
        raise ValueError("Некорректное выражение")

    def apply_operator():
        op = operators.pop()
        v2 = values.pop()
        v1 = values.pop()
        if op == '+':
            values.append(v1 + v2)
        elif op == '-':
            values.append(v1 - v2)
        elif op == '*':
            values.append(v1 * v2)
        elif op == '/':
            if v2 == 0:
                raise ZeroDivisionError("Деление на ноль")
            values.append(v1 / v2)
        elif op == '^':
            values.append(v1 ** v2)

    values = []
    operators = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '.':
            j = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            values.append(float(expression[j:i]))
        elif expression[i] in '+-*/^':
            if expression[i] and expression[i+1] == '+' or '-' or '*' or '/' or '^':
                print("Ошибка ввода")
            while operators and operators[-1] != '(' and get_priority(operators[-1]) >= get_priority(expression[i]):
                apply_operator()
            operators.append(expression[i])
            i += 1
        elif expression[i] == ' ':
            print("Ошибка ввода")
            return main()
    while operators:
        apply_operator()
    return values[0]

def get_priority(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    elif op == '^':
        return 3
    return 0

def main():
    while True:
        try:
            expression = input("Введите выражение:")
            result = calculate(expression)
            print("Результат:", result)
        except ValueError as e:
            print("Ошибка:", e)
        except ZeroDivisionError as e:
            print("Ошибка:", e)
        except Exception as e:
            print("Неизвестная ошибка:", e)


__name__ == "__main__" and main()
