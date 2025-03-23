class Matrix:
      length = 0
      width = 0

def main():
    Matrix.width = int(input("Введите кол-во cтрок:"))
    Matrix.length = int(input("Введите кол-во столбцов:"))
    element = [[0 for i in range(Matrix.length)] for j in range(Matrix.width)]
    print("Введите значения матрицы")
    for i in range (Matrix.width):
        for j in range (Matrix.length):
             if element[i][j] == ' ':
                print("Ошибка ввода матрицы")
                return main()
             else:
                element[i][j] = float(input())

    print()
    print("Ваша матрица")
    print()

    for i in range (Matrix.width):
        for j in range (Matrix.length):
             print(f"{element[i][j]} ", end="")
        print()

    print()
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
       pass
    elif choice == 2:
       pass
    elif choice == 3:
       target = float(input("Введи число, на которое хотите умножить матрицу"))
       for i in range(Matrix.width):
          for j in range(Matrix.length):
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

       for i in range(Matrix.width):
          for j in range(Matrix.length):
              print(f"{matrix[i][j]} ", end="")
          print()
       return apply_matrix(matrix, width, length)
    elif choice == 6:
       pass
    elif choice == 7:
       pass
    elif choice == 8:
       return 0

__name__ = "__main__" and main()
