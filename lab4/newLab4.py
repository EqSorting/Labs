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
                    if self.width < 0:
                        print("Количество строк не может быть отрицательным")
                    else:
                        break
                except ValueError:
                    print("Были введены символы, введите цифры")

            while True:
                try:
                    self.length = int(input("Введите количество столбцов: "))
                    if self.length < 0:
                        print("Количество столбцов не может быть отрицательным")
                    else:
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
    
    def multiply_matrix(self, first_matrix, second_matrix):
        result_matrix = Matrix(zero=True)
        result_matrix.width = first_matrix.width
        result_matrix.length = second_matrix.length
        result_matrix = [[0 for _ in range(second_matrix.length)] for _ in range(first_matrix.width)]
   
        for i in range(first_matrix.width):
            for j in range(second_matrix.length):
                for k in range(first_matrix.length):
                    result_matrix[i][j] += first_matrix.element[i][k] * second_matrix.element[k][j]
        
        for i in range(first_matrix.width):
            for j in range(second_matrix.length):
                print(f"{result_matrix[i][j]} ", end="")
            print()
    
    def multiply_by_number(self, number):
        for i in range(self.width):
            for j in range(self.length):
                self.element[i][j] *= number
        return self

    def divide_by_number(self, number):
            for i in range(self.width):
                for j in range(self.length):
                    if number != 0:
                        self.element[i][j] /= number
                    else:
                        print("Деление на 0 недопустимо.")

    def __neg__(self):
        for i in range(self.width):
            for j in range(self.length):
                self.element[i][j] *= -1
                return Matrix(self)
    
    def transponce_matrix(self):
       transponced = [[self.element[i][j] for j in range(self.length)] for i in range(self.width)]
       self.element = transponced
       old_width = self.width
       old_length = self.length
       self.width = old_length
       self.length = old_width
       for i in range(self.width):
            for j in range(self.length):
                print(f"{self.element[j][i]} ", end="")
            print()


    def summ_matrix(self, matrix1, matrix2):
        for i in range(matrix1.width):
            for j in range(matrix1.length):
                matrix1.element[i][j] += matrix2.element[i][j]
        return matrix1
    
    def subsctract_matrix(self, matrix1, matrix2):
        for i in range(matrix1.width):
            for j in range(matrix1.length):
                matrix1.element[i][j] -= matrix2.element[i][j]
    
    def index_matrix(self, new_width, new_length):
        for i in range(self.width):
            for j in range(self.length):
                if (i == new_width and j == new_length):
                    print(f"{self.element[i][j]} ", end="")

class Vector(Matrix):
    def __init__(self, matrix):
        self.width = 1
        self.length = matrix.length * matrix.width
        self.element = [element for row in matrix.element for element in row]
    def __len__(self):
        return self.length
    def __iter__(self):
        return iter(self.element)
    def __getitem__(self, index):
        return self.element[index]
    def module(self):
        return math.sqrt(sum(element ** 2 for element in self.element))


def MENU(matrix):
    choice = 0
    while True:
        try:
            print("MENU")
            print("1. Сумма матриц")
            print("2. Разность матриц")
            print("3. Умножение матрицы на число")
            print("4. Деление матрицы на число")
            print("5. Транспонирование матрицы")
            print("6. Индексирование матрицы")
            print("7. Умножение матриц")
            print("8. Работа с вектором")
            print("9. Выход")
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
            elif choice == 7:
                second_matrix = Matrix()
                if matrix.length != second_matrix.width:
                    print("Matrices cannot be multiplied")
                    return MENU(matrix)
                second_matrix.add_matrix()
                matrix.multiply_matrix(matrix, second_matrix)
            elif choice == 8:
                while True:
                    try:
                        vector = Vector(matrix)
                        print("MENU")
                        print("1. Длина вектора")
                        print("2. Норма вектора")
                        print("3. Индексирование элементов вектора")
                        print("4. Итерирование вектора")
                        print("5. Выход")
                        print("Выберете желаемый пункт")
                        second_choice = int(input())
                        if second_choice == 1:
                            print("Длина вектора: ", len(vector))
                        elif second_choice == 2:
                            print("Норма вектора: ", vector.module())
                        elif second_choice == 3:
                            index = int(input("Введите индекс элемента вектора: "))
                            if index > len(vector):
                                print("Неправильный индекс")
                            if index < 0:
                                print("Отрицательный индекс, введите положительный")
                            print("Элемент вектора по индексу {}: {}".format(index, vector[index]))
                        elif second_choice == 4:
                            print("Итерирование вектора:")
                            for element in vector:
                                print(element)
                        elif second_choice == 5:
                            return MENU(matrix)
                    except ValueError:
                        print("Были введен символ, а не число")
            elif choice == 9:
                break
        except ValueError:
            print("Enter the correct number")
    
def main():
    print("Введите матрицу")
    matrix = Matrix()
    matrix.add_matrix()
    matrix.print_matrix()
    MENU(matrix)
    
main()