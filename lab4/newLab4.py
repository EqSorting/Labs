import math

class Matrix:
    def __init__(self, zero=False):
        if zero == True:
            self.width = 0
            self.length = 0
            self.element = []
        else:
            while True:
                try:
                    self.width = int(input("Введите количество строк: "))
                    break
                except ValueError:
                    print("Были введены символы, введите цифры")
            while True:
                try:
                    self.length = int(input("Введите количество столбцов: "))
                    break
                except ValueError:
                    print("Были введены символы, введите цифры")
            self.element = [[0 for _ in range(self.length)] for _ in range(self.width)]

    def add_matrix(self):
        print("Введите значения матрицы")
        for i in range(self.width):
            for j in range(self.length):
                while True:
                    try:
                        self.element[i][j] = float(input())
                        break
                    except ValueError:
                        print("Ошибка ввода матрицы. Пожалуйста, введите число.")
    def print_matrix(self):
        for i in range(self.width):
            for j in range(self.length):
                print(f"{self.element[i][j]} ", end="")
            print()

    def multiply_by_number(self, number):
        for i in range(self.width):
            for j in range(self.length):
                self.element[i][j] *= number

    def divide_by_number(self):
        try:
            number = float(input("Введите число для деления: "))
            for i in range(self.width):
                for j in range(self.length):
                    if number != 0:
                        self.element[i][j] /= number
                    else:
                        print("Деление на 0 не допустимо.")
        except ValueError:
            print("Ошибка ввода числа. Пожалуйста, введите число.")

    def __pos__(self):
        return Matrix(self)
    
    def __neg__(self):
        for i in range(self.width):
            for j in range(self.length):
                self.element[i][j] *= -1
                return Matrix(self)
    
    def transponce_matrix(self):
        if (self.width == self.length):
            for i in range(self.width):
                for j in range(self.length):
                    self.element[i][j] = self.element[j][i]
        else:
            print("хуйня")

    def create_zero_matrix(self, width, length):
        self.width = width
        self.length = length
        self.element = [[0 for _ in range(self.length)] for _ in range(self.width)]

    def summ_matrix(self, matrix1, matrix2):
        result = Matrix(zero=True)
        result.create_zero_matrix(self.width, self.length)
        for i in range(matrix1.width):
            for j in range(matrix1.length):
                result.element[i][j] = matrix1.element[i][j] + matrix2.element[i][j]
        return result
    
    def subsctract_matrix(self, matrix1, matrix2):
        result = Matrix(zero=True)
        result.create_zero_matrix(self.width, self.length)
        for i in range(matrix1.width):
            for j in range(matrix1.length):
                result.element[i][j] = matrix1.element[i][j] - matrix2.element[i][j]
        return result
    
    def index_matrix(self, new_width, new_length):
        for i in range(self.width):
            for j in range(self.length):
                if (i == new_width and j == new_length):
                    print(f"{self.element[i][j]} ", end="")


def MENU(matrix):
    choice = 0
    while (choice != 8):
        try:
            print("MENU")
            print("1. Сумма матриц")
            print("2. Разность матриц")
            print("3. Умножение матрицы на число")
            print("4. Деление матрицы на число")
            print("5. Транспонирование матрицы")
            print("6. Индексирование матрицы")
            print("8. Выход")
            choice = int(input("Выберите интересующий ваш код: "))
            if choice == 1:
                matrix1 = Matrix()
                if (matrix1.width != matrix.width or matrix1.length != matrix.length):
                    print("Размер матрицы не совпадает с начальным")
                    return MENU(matrix)
                matrix1.add_matrix()
                result = matrix.summ_matrix(matrix, matrix1)
                result.print_matrix()
            elif choice == 2:
                matrix1 = Matrix()
                if (matrix1.width != matrix.width or matrix1.length != matrix.length):
                    print("Размер матрицы не совпадает с начальным")
                    return MENU(matrix)
                matrix1.add_matrix()
                result = matrix.subsctract_matrix(matrix, matrix1)
                result.print_matrix()
            elif choice == 3:
                try:
                    num = int(input("Введите число: "))
                    matrix.multiply_by_number(num)
                    matrix.print_matrix()
                except ValueError:
                    print("Были введен символ, а не число")
            elif choice == 4:
                try:
                    num = int(input("Введите число: "))
                    if (num == 0):
                        print("Деление на 0 не возможно")
                        return MENU(matrix)
                    matrix.divide_by_number(num)
                    matrix.print_matrix()
                except ValueError:
                    print("Были введен символ, а не число")
            elif choice == 5:
                matrix.transponce_matrix()
                matrix.print_matrix()
            elif choice == 6:
                print("Примечание! Индексирование начинается с 0, а не с 1")
                new_width = int(input("Выберите строку: "))
                new_length = int(input("Выберите столбец: "))
                if (new_width > matrix.width or new_length > matrix.length):
                    print("Неправильный индекс")
                    return MENU(matrix)
                if (new_width < 0 or new_length < 0):
                    print("Отрицательный индекс, введите положительный")
                matrix.index_matrix(new_width, new_length)
                print()
        except ValueError:
            print("Enter the correct number")
    
def main():
    print("Введите матрицу")
    matrix = Matrix()
    matrix.add_matrix()
    matrix.print_matrix()
    MENU(matrix)
    

main()