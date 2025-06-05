import math

class Matrix:
      length = 0
      width = 0

def main():
    Matrix.width = int(input("Введите кол-во cтрок:"))
    if Matrix.width == " ":
       print("Введите число")
       return main()
    Matrix.length = int(input("Введите кол-во столбцов:"))
    if Matrix.length == " ":
       print("Введите число")
       return main()
    element = [[0 for i in range(Matrix.length)] for j in range(Matrix.width)]
    print("Введите значения матрицы")
    for i in range (Matrix.width):
        for j in range (Matrix.length):
             element[i][j] = float(input())
             if element[i][j] == ' ':
                print("Ошибка ввода матрицы")
                return main()
             else:
                continue

    print()
    print("Ваша матрица")
    print()

    for i in range (Matrix.width):
        for j in range (Matrix.length):
             print(f"{element[i][j]} ", end="")
        print()

    print()
    replace_element(element, Matrix.width, Matrix.length)
    apply_matrix(element, Matrix.width, Matrix.length)

def apply_matrix(matrix, width, length):
    print("Что хотите сделать?")
    print("1. Сложение матриц")
    print("2. Вычитание матриц")
    print("3. Умножение матрицы на число")
    print("4. Умножение матриц")
    print("5. Деление матрицы на число")
    print("6. Транспонирование матрицы")
    print("7. Индексирование матрицы")
    print("8. Выход")

    choice = int(input("Ваш выбор:"))

    if choice == 1:
       width2 = width
       length2 = length
       print("Введите элементы матрицы")
       element2 = [[0 for i in range(length2)] for j in range(width2)]
       for i in range (width2):
          for j in range (length2):

               if element2[i][j] == ' ':
                  print("Ошибка ввода матрицы")
                  return main()
               else:
                  element2[i][j] = float(input())

       for i in range (width2):
          for j in range (length2):
              matrix[i][j] += element2[i][j]

       for i in range (width):
          for j in range (length):
              print(f"{matrix[i][j]} ", end="")
          print()
       return apply_matrix(matrix, width, length)
    elif choice == 2:
       width3 = width
       length3 = length
       print("Введите элементы матрицы")
       element3 = [[0 for i in range(length3)] for j in range(width3)]
       for i in range (width3):
          for j in range (length3):
               if element3[i][j] == ' ':
                  print("Ошибка ввода матрицы")
                  return main()
               else:
                  element3[i][j] = float(input())

       for i in range (width3):
          for j in range (length3):
              matrix[i][j] -= element3[i][j]

       for i in range (width):
          for j in range (length):
              print(f"{matrix[i][j]} ", end="")
          print()
       return apply_matrix(matrix, width, length)
    elif choice == 3:
       target = float(input("Введи число, на которое хотите умножить матрицу"))
       for i in range(width):
          for j in range(length):
              matrix[i][j] = target * matrix[i][j]

       for i in range(width):
          for j in range(length):
              print(f"{matrix[i][j]} ", end="")
          print()
       return apply_matrix(matrix, width, length)
    elif choice == 4:
       pass
    elif choice == 5:
       target2 = float(input("Введите число, на которое хотите поделить:"))
       if target2 == 0:
          print("Деление на ноль")
          return apply_matrix(matrix, width, length)
       for i in range(width):
          for j in range(length):
              matrix[i][j] = matrix[i][j] / target2

       for i in range(width):
          for j in range(length):
              print(f"{matrix[i][j]} ", end="")
          print()
       return apply_matrix(matrix, width, length)
    elif choice == 6:
       width = length
       length = width
       elements = [[0 for i in range(length)] for j in range(width)]
       for i in range(width):
          for j in range(length):
               if i < len(matrix) and j < len(matrix[0]):
                   elements[j][i] = matrix[i][j]

       matrix = elements

       for i in range(length):
          for j in range(width):
                   print(f"{matrix[i][j]} ", end="")
          print()
    elif choice == 7:
       pass
    elif choice == 8:
       return 0

def replace_element(matrix, width, length):
    flag = 1
    while flag == 1:
        char = input("Хотите заменить элемент?")
        if char == 'Да':
            replace_width = int(input("Введите строку, где хотите заменить элемент"))
            replace_length = int(input("Введите столбец, где хотите заменить элемент"))
            value = float(input("На какое значение хотите поменять?"))
            for i in range(width):
                for j in range(length):
                    if matrix[i][j] == matrix[replace_width][replace_length]:
                       matrix[replace_width][replace_length] = value

            for i in range(width):
                for j in range(length):
                      print(f"{matrix[i][j]} ", end="")
                print()
            flag = 1
        else:
            flag = 0
            print("Подождитe...")

__name__ = "__main__" and main()


