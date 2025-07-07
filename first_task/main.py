import numpy as np
import random as rd

def create_np(line):
    if any(not x.isdigit() for x in line.split()):
        raise ValueError("Ввод должен содержать только числа, разделенные пробелами.")
    np_array = np.array([int(x) for x in line.split()])
    return np_array

def create_chessboard(size):
    if size <= 0 or not isinstance(size, int):
        raise ValueError("Размер шахматной доски должен быть положительным целым числом.")
    chessboard = np.fromfunction(lambda i, j: (i + j) % 2, (size, size), dtype=int)
    return chessboard

def create_random_matrix_from_file(file_name):
    with open(file_name, 'r') as f:
        line = f.readline()
    if not line.strip() or len(line.split()) != 2 or not all(x.isdigit() for x in line.split()):
        raise ValueError("Файл должен содержать две целых числа, разделенных пробелом.")
    rows, cols = map(int, line.split())
    matrix = np.random.randint(0, 101, size=(rows, cols))
    return matrix

def process_and_multiply_matrices(rd_matrix):
    A = rd_matrix
    B = np.random.randint(0, 101, size=(A.shape[1], rd.randint(1, 10)))
    print(f"Матрица A:\n{A}")
    print(f"Матрица B:\n{B}")

    max_val = np.max(A, axis=1)
    print(f"Максимальные значения матрицы: {max_val}")
    A = A / max_val[:, None]
    C = np.dot(A, B)
    write_matrix_to_file(C, "first_task/result_matrix")
    return C

def first_calculation():
    data_A = np.array([[2, 3], [4, 7]])
    data_B = np.array([[5, 1], [2, 3]])
    A_1 = np.dot(data_A.T, data_B)
    A_2 = np.dot(data_A, data_B.T)
    C = np.dot(A_1, A_2)
    return C

def second_calculation():
    data_A = np.array([[2, 3], [1, 2]])
    data_B = np.array([[1, -2], [3, 1]])
    A_1 = data_A.T - data_B
    A_2 = data_B.T * 2
    C = A_1 - A_2
    return C

def third_calculation():
    data_A = np.array([[5, 8, 2], [-1, 3, 1], [2, 0, 3]])
    data_B = np.array([[2, 4, 1], [3, -1, 8], [0, 1, 2]])
    A_1 = data_A * 3
    A_2 = np.dot(data_B.T, data_A.T)
    C = A_1 + A_2
    return C

def fourth_calculation():
    data_A = np.array([[1, 0, 2], [-1, 2, 1], [2, 0, 1]])
    data_B = np.array([[2, 1, 0], [3, -1, 4], [0, 0, 2]])
    A_1 = np.linalg.matrix_power(data_A, 2)
    A_2 = np.dot(data_A.T, data_B)
    C = A_1 + A_2
    return C

def write_matrix_to_file(matrix, filename):
    with open(f"{filename}.txt", 'w') as f:
        for row in matrix:
            row_data = ";".join(map(str, row))
            f.write(row_data + "\n")

def all_task():
    line = input("Введите числа разделенные пробелом: \n")
    line = line.strip()
    create_np(line)
    size = int(input("Введите размер шахматной доски \n"))
    chess_board = create_chessboard(size)
    print(chess_board)
    rd_matrix = create_random_matrix_from_file("input.txt")
    rd_matrix_2 = process_and_multiply_matrices(rd_matrix)
    vectorized_function = np.vectorize(lambda x: round(x, 1))
    print("Результат вычислений матриц:\n", vectorized_function(rd_matrix_2))
    C_1 = first_calculation()
    C_2 = second_calculation()
    C_3 = third_calculation()
    C_4 = fourth_calculation()
    print("Результат вычисления A^T * B * A * B^T\n", C_1)
    input("Нажмите Enter для продолжения...")
    print("Результат вычисления A^T - B - 2 * B^T:\n", C_2)
    input("Нажмите Enter для продолжения...")
    print("Результат вычисления 3 * A + B^T * A^T:\n", C_3)
    input("Нажмите Enter для продолжения...")
    print("Результат вычисления A^2 + A^T * B:\n", C_4)
    input("Нажмите Enter для продолжения...")
    print(1)

def main():
    choice = input("Выберите задачу (1-4): \n")
    match choice:
        case "1":
            print("Задача 1: Чтение массива NumPy")
            line = input("Введите числа разделенные пробелом: \n")
            np_array = create_np(line)
            print(np_array)
        case "2":
            print("Задача 2: Создание шахматной доски")
            size = int(input("Введите размер шахматной доски \n"))
            chessboard = create_chessboard(size)
            print(chessboard)
        case "3":
            rd_matrix = create_random_matrix_from_file("input.txt")
            rd_matrix_2 = process_and_multiply_matrices(rd_matrix)
            vectorized_function = np.vectorize(lambda x: round(x, 1))
            print("Результат вычислений матриц:\n", vectorized_function(rd_matrix_2))
        case "4":
            print("Задача 4: Выполнение математических операций с матрицами")
            C_1 = first_calculation()
            print("Результат вычисления A^T * B * A * B^T\n", C_1)
            input("Нажмите Enter для продолжения...")
            C_2 = second_calculation()
            print("Результат вычисления A^T - B - 2 * B^T:\n", C_2)
            input("Нажмите Enter для продолжения...")
            C_3 = third_calculation()
            print("Результат вычисления 3 * A + B^T * A^T:\n", C_3)
            input("Нажмите Enter для продолжения...")
            C_4 = fourth_calculation()
            print("Результат вычисления A^2 + A^T * B:\n", C_4)
        case _:
            print("Неверный выбор задачи. Пожалуйста, выберите от 1 до 4.")
            return

if __name__ == "__main__":
    all_task()