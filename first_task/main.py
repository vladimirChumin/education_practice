import numpy as np
import random as rd
from first_task.Matrix import Matrix, Chessboard, RandomMatrix

def read_np():
    line = input("Введите числа разделенные пробелом: \n")
    np_array = np.array([int(x) for x in line.split()])
    print("NP массив: ", np_array)

def create_chessboard():
    size = int(input(": Введите размер шахматной доски \n"))
    chessboard = Chessboard(size)
    print(chessboard)

def create_random_matrix_from_file():
    with open("input.txt", 'r') as f:
        line = f.readline()
    rows, cols = map(int, line.split())
    matrix = RandomMatrix(rows, cols)
    return matrix

def process_and_multiply_matrices():
    A = create_random_matrix_from_file()
    B = RandomMatrix(len(A.data[0]), rd.randint(1, 10))
    print(f"Матрица A:\n{A}")
    print(f"Матрица B:\n{B}")

    max_val = A.find_max_values(is_row=True)
    print(f"Максимальные значения матрицы: {max_val}")
    A.divide_by_list(max_val, is_row=True)
    print(f"Матрица а после вычитания максимальных элементов:\n{A}")
    C = A * B
    print(f"A * B:\n{C}")
    C.write_to_file("first_task/result_matrix")

def first_calculation():
    data_A = np.array([[2, 3], [4, 7]])
    data_B = np.array([[5, 1], [2, 3]])
    print(f"Матрица A:\n{data_A}\n Матрица B:\n{data_B}")
    A = Matrix(matrix=data_A)
    B = Matrix(matrix=data_B)
    A_1 = A.transpone_matrix() * B
    A_2 = A * B.transpone_matrix()
    C = A_1 * A_2
    print("Результат вычисления A^T * B * A * B^T\n", C)

def second_calculation():
    data_A = np.array([[2, 3], [1, 2]])
    data_B = np.array([[1, -2], [3, 1]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)
    A_1 = A.transpone_matrix() - B
    A_2 = B.transpone_matrix() * 2
    C = A_1 - A_2
    print("Результат вычисления A^T - B - 2 * B^T:\n", C)

def third_calculation():
    data_A = np.array([[5, 8, 2], [-1, 3, 1], [2, 0, 3]])
    data_B = np.array([[2, 4, 1], [3, -1, 8], [0, 1, 2]])
    A = Matrix(matrix=data_A)
    B = Matrix(matrix=data_B)
    A_1 = A * 3
    A_2 = B.transpone_matrix() * A.transpone_matrix()
    C = A_1 + A_2
    print("Результат вычисления 3 * A + B^T * A^T:\n", C)

def fourth_calculation():
    data_A = np.array([[1, 0, 2], [-1, 2, 1], [2, 0, 1]])
    data_B = np.array([[2, 1, 0], [3, -1, 4], [0, 0, 2]])
    A = Matrix(matrix=data_A)
    B = Matrix(matrix=data_B)
    A_1 = A ** 2
    A_2 = A.transpone_matrix() * B
    C = A_1 + A_2
    print("Результат вычисления A^2 + A^T * B:\n", C)

def all_task():
    read_np()
    create_chessboard()
    process_and_multiply_matrices()
    first_calculation()
    second_calculation()
    third_calculation()
    fourth_calculation()
    print(1)

def main():
    choice = input("Выберите задачу (1-4): \n")
    match choice:
        case "1":
            print("Задача 1: Чтение массива NumPy")
            read_np()
        case "2":
            print("Задача 2: Создание шахматной доски")
            create_chessboard()
        case "3":
            print("Задача 3: Обработка и умножение матриц")
            process_and_multiply_matrices()
        case "4":
            print("Задача 4: Выполнение математических операций с матрицами")
            first_calculation()
            input("Нажмите Enter для продолжения...")
            second_calculation()
            input("Нажмите Enter для продолжения...")
            third_calculation()
            input("Нажмите Enter для продолжения...")
            fourth_calculation()
        case _:
            print("Неверный выбор задачи. Пожалуйста, выберите от 1 до 4.")
            return

if __name__ == "__main__":
    all_task()