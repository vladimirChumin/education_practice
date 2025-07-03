# python
import numpy as np
import random as rd

def read_np():
    line = input("Введите числа разделенные пробелом: \n")
    np_array = np.array([int(x) for x in line.split()])
    print("NP массив: ", np_array)

def create_chessboard():
    size = int(input("Введите размер шахматной доски \n"))
    # Формируем шахматную доску с элементами (i+j)%2
    chessboard = np.fromfunction(lambda i, j: (i + j) % 2, (size, size), dtype=int)
    print(chessboard)

def create_random_matrix_from_file():
    with open("input.txt", 'r') as f:
        line = f.readline()
    rows, cols = map(int, line.split())
    # Генерируем матрицу случайных целых чисел от 0 до 100
    matrix = np.random.randint(0, 101, size=(rows, cols))
    return matrix

def process_and_multiply_matrices():
    A = create_random_matrix_from_file()
    B = np.random.randint(0, 101, size=(A.shape[1], rd.randint(1, 10)))
    print(f"Матрица A:\n{A}")
    print(f"Матрица B:\n{B}")

    # Находим максимальные значения по строкам
    max_val = np.max(A, axis=1)
    print(f"Максимальные значения матрицы: {max_val}")
    # Делим каждую строку на её максимальное значение
    A = A / max_val[:, None]
    print(f"Матрица A после нормализации строк:\n{A}")
    # Умножение матриц (dot product)
    C = np.dot(A, B)
    print(f"A * B:\n{C}")
    write_matrix_to_file(C, "first_task/result_matrix")

def first_calculation():
    data_A = np.array([[2, 3], [4, 7]])
    data_B = np.array([[5, 1], [2, 3]])
    print(f"Матрица A:\n{data_A}\nМатрица B:\n{data_B}")
    # A_transposed * B
    A_1 = np.dot(data_A.T, data_B)
    # A * B_transposed
    A_2 = np.dot(data_A, data_B.T)
    # Результат вычисления A^T * B * A * B^T
    C = np.dot(A_1, A_2)
    print("Результат вычисления A^T * B * A * B^T\n", C)

def second_calculation():
    data_A = np.array([[2, 3], [1, 2]])
    data_B = np.array([[1, -2], [3, 1]])
    # A_transposed - B
    A_1 = data_A.T - data_B
    # 2 * B_transposed
    A_2 = data_B.T * 2
    C = A_1 - A_2
    print("Результат вычисления A^T - B - 2 * B^T:\n", C)

def third_calculation():
    data_A = np.array([[5, 8, 2], [-1, 3, 1], [2, 0, 3]])
    data_B = np.array([[2, 4, 1], [3, -1, 8], [0, 1, 2]])
    # Элементное умножение числа на матрицу
    A_1 = data_A * 3
    # В данном случае используем матричное умножение
    A_2 = np.dot(data_B.T, data_A.T)
    C = A_1 + A_2
    print("Результат вычисления 3 * A + B^T * A^T:\n", C)

def fourth_calculation():
    data_A = np.array([[1, 0, 2], [-1, 2, 1], [2, 0, 1]])
    data_B = np.array([[2, 1, 0], [3, -1, 4], [0, 0, 2]])
    # Матрица A в степени 2 (матричное умножение)
    A_1 = np.linalg.matrix_power(data_A, 2)
    A_2 = np.dot(data_A.T, data_B)
    C = A_1 + A_2
    print("Результат вычисления A^2 + A^T * B:\n", C)

def write_matrix_to_file(matrix, filename):
    with open(f"{filename}.txt", 'w') as f:
        for row in matrix:
            row_data = ";".join(map(str, row))
            f.write(row_data + "\n")

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