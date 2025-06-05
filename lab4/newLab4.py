import math
from weakref import ref

class Matrix:
    def __init__(self, obj):
        if isinstance(obj, Matrix):
            self.width = obj.width
            self.length = obj.length
            for i in range(self.width):
                for j in range(self.length):
                    self.element[i][j] = obj.element[i][j]
        else:
            self.length = len(obj)
            self.element = [[y for y in x] for x in obj]
            self.width = len(self.element[0])

    def print_matrix(self):
        if not self.element:
            print("Матрица пуста.")
            return
        for row in self.element:
            print(" ".join(map(str, row)))

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.element])
    
    def __mul__(self, number):
        for i in range(self.width):
            for j in range(self.length):
                self.element[i][j] *= number
        return self
    
    def __truediv__(self, number):
        if number == 0:
            print("Деление на 0 недопустимо.")
            return self
        for i in range(self.width):
            for j in range(self.length):
                self.element[i][j] /= number
        return self
    def __neg__(self):
        res = [[-y for y in x] for x in self.element]
        return type(self)(res)
    
    def transponce_matrix(self):
        self.element = [[self.element[j][i] for j in range(self.width)] for i in range(self.length)]
        self.width, self.length = self.length, self.width
        return self
    
    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            i, j = index
            return self.values[i][j]
        else:
            return self.values[index]
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __add__(self, obj):
        res = [[0 for _ in range(self.width)] for _ in range(self.length)]
        if isinstance(obj, Matrix):
            if self.length != obj.length or self.width != obj.width:
                print("Не совпадают размеры матрицы")
            for i in range(self.width):
                for j in range(self.length):
                    res[i] += self.element[i][j] + obj.element[i][j]
            return res
        else:
            for i in range(self.width):
                for j in range(self.length):
                    res[i][j] += self.element[i][j] + obj
            return res

    def __sub__(self, obj):
        res = [[0 for _ in range(self.width)] for _ in range(self.length)]
        if self.width != obj.width or self.length != obj.length:
            print("Размеры матриц не совпадают.")
        if isinstance(obj, Matrix):
            for i in range(self.width):
                for j in range(self.length):
                    res[i][j] += self.element[i][j] - obj.element[i][j]
        else:
            for i in range(self.width):
                for j in range(self.length):
                    res[i][j] += self.element[i][j] - obj

    def __matmul__(self, obj):
            result_matrix = [[0 for _ in range(self.width)] for _ in range(self.length)]
            if self.length != obj.width:
                print("Матрицы не могут быть перемножены.")
                return
            for i in range(self.width):
                for j in range(obj.length):
                    for k in range(self.length):
                        result_matrix.element[i][j] += self.element[i][k] * obj.element[k][j]

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
        if isinstance(index, tuple) and len(index) == 2:
            i, j = index
            if j != 0:
                raise IndexError("Vector has only one column")
            return self.element[i]
        else:
            return self.element[index]
    def module(self):
        return math.sqrt(sum(element ** 2 for element in self.element))


def main():
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
                width1 = int(input("Введите количество строк матрицы: "))
                length1 = int(input("Введите количество столбцов матрицы: "))
                if (length1 < 0 or width1 < 0):
                    print("Размер матрицы не может быть отрицательным")
                element = [[0 for _ in range(width1)] for _ in range(length1)]
                print("Введите элементы матрицы")
                for i in range(width1):
                    for j in range(length1):
                        element[i][j] = float(input())
                matrix1 = Matrix(element)
                width2 = int(input("Введите количество строк матрицы: "))
                length2 = int(input("Введите количество столбцов матрицы: "))
                if (length1 < 0 or width1 < 0):
                    print("Размер матрицы не может быть отрицательным")
                element1 = [[0 for _ in range(width2)] for _ in range(length2)]
                print("Введите элементы матрицы")
                for i in range(width2):
                    for j in range(length2):
                        element1[i][j] = float(input())
                matrix2 = Matrix(element1)
                matrix1.__add__(matrix2) 
            elif choice == 2:
                while True:
                    try:
                        width1 = int(input("Введите количество строк матрицы: "))
                        length1 = int(input("Введите количество столбцов матрицы: "))
                        if (width1 < 0 or length1 < 0):
                            print("Размер матрицы не может быть отрицательным")
                        matrix1 = Matrix(width1, length1)
                        print("Введите элементы первой матрицы")
                        matrix1.add_matrix()
                        width2 = int(input("Введите количество строк матрицы: "))
                        length2 = int(input("Введите количество столбцов матрицы: "))
                        if (width2 < 0 or length2 < 0):
                            print("Размер матрицы не может быть отрицательным")
                        matrix2 = Matrix(width2, length2)
                        print("Введите элементы второй матрицы")
                        matrix2.add_matrix()
                        if (matrix1.width != matrix2.width or matrix1.length != matrix2.length):
                            print("Размер матрицы не совпадает с начальным")
                            return main()
                        matrix1.subsctract_matrix(matrix2)
                        matrix1.print_matrix()
                    except ValueError:
                        print("Некорректный ввод. Введите целое число.")
                    break
            elif choice == 3:
                width = int(input("Введите количество строк матрицы: "))
                length = int(input("Введите количество столбцов матрицы: "))
                if (width < 0 or length < 0):
                    print("Размер матрицы не может быть отрицательным")
                matrix = Matrix(width, length)
                print("Введите элементы матрицы")
                matrix.add_matrix()
                try:
                    num = int(input("Введите число: "))
                    matrix.multiply_by_number(num)
                    matrix.print_matrix()
                except ValueError:
                    print("Были введен символ, а не число")
            elif choice == 4:
                width = int(input("Введите количество строк матрицы: "))
                length = int(input("Введите количество столбцов матрицы: "))
                if (width < 0 or length < 0):
                    print("Размер матрицы не может быть отрицательным")
                matrix = Matrix(width, length)
                print("Введите элементы матрицы")
                matrix.add_matrix()
                try:
                    num = int(input("Введите число: "))
                    matrix.divide_by_number(num)
                    matrix.print_matrix()
                except ValueError:
                    print("Были введен символ, а не число")
            elif choice == 5:
                width = int(input("Введите количество строк матрицы: "))
                length = int(input("Введите количество столбцов матрицы: "))
                if (width < 0 or length < 0):
                    print("Размер матрицы не может быть отрицательным")
                matrix = Matrix(width, length)
                print("Введите элементы матрицы")
                matrix.add_matrix()
                matrix.transponce_matrix()
                matrix.print_matrix()
            elif choice == 6:
                width = int(input("Введите количество строк матрицы: "))
                length = int(input("Введите количество столбцов матрицы: "))
                if (width < 0 or length < 0):
                    print("Размер матрицы не может быть отрицательным")
                matrix = Matrix(width, length)
                print("Введите элементы матрицы")
                matrix.add_matrix()
                print("Примечание! Индексирование начинается с 0, а не с 1")
                new_width = int(input("Выберите строку: "))
                new_length = int(input("Выберите столбец: "))
                matrix.index_matrix(new_width, new_length)
                print()
            elif choice == 7:
                width1 = int(input("Введите количество строк матрицы: "))
                length1 = int(input("Введите количество столбцов матрицы: "))
                if (width1 < 0 or length1 < 0):
                    print("Размер матрицы не может быть отрицательным")
                matrix1 = Matrix(width1, length1)
                print("Введите элементы матрицы")
                matrix1.add_matrix()
                width2 = int(input("Введите количество строк матрицы: "))
                length2 = int(input("Введите количество столбцов матрицы: "))
                if (width2 < 0 or length2 < 0):
                    print("Размер матрицы не может быть отрицательным")
                matrix2 = Matrix(width2, length2)
                print("Введите элементы матрицы")
                matrix2.add_matrix()
                matrix1.multiply_matrix(matrix2)
                matrix1.print_matrix()
            elif choice == 8:
                        width = int(input("Введите количество строк матрицы: "))
                        length = int(input("Введите количество столбцов матрицы: "))
                        if (width < 0 or length < 0):
                            print("Размер матрицы не может быть отрицательным")
                        matrix = Matrix(width, length)
                        print("Введите элементы матрицы")
                        matrix.add_matrix()
                        vector = Vector(matrix)
                        while True:
                            try:
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
                                    return main()
                                else:
                                    print("Неправильная цифра")
                            except ValueError:
                                print("Были введен символ, а не число")
            elif choice == 9:
                break
        except ValueError:
            print("Enter the correct number")

main()
x = int("2")
x = Matrix()
x[1,0]
y = Vector([1,2])
y[1,0]
z = x+y
z[1,1]
print(z)