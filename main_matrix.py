import numpy as np
import random as rd
from base_classes.Matrix import Matrix, RandomMatrix, Chessboard

def read_np():
    line = input("Enter a line of numbers separated by spaces: \n")
    np_array = np.array([int(x) for x in line.split()])
    print("You entered:", np_array)

def create_chessboard():
    size = int(input("Enter the size of the chessboard: \n"))
    chessboard = Chessboard(size)
    print("Chessboard created:")
    print(chessboard)

def create_random_matrix_from_file():
    with open("source/input_1.txt", 'r') as f:
        line = f.readline()
    rows, cols = map(int, line.split())
    matrix = RandomMatrix(rows, cols)
    return matrix

def process_and_multiply_matrices():
    A = create_random_matrix_from_file()
    B = RandomMatrix(len(A.data[0]), rd.randint(1, 10))
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")

    max_val = A.find_max_values(is_row=True)
    print(f"Max values of A by row: {max_val}")
    A.divide_by_list(max_val, is_row=True)
    print(f"Matrix A after dividing by max values of each row:\n{A}")
    C = A * B
    print(f"Result of A * B:\n{C}")
    C.write_to_file("result_matrix")

def first_calculation():
    data_A = np.array([[2, 3], [4, 7]])
    data_B = np.array([[5, 1], [2, 3]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def second_calculation():
    data_A = np.array([[2, 3], [1, 2]])
    data_B = np.array([[1, -2], [3, 1]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def third_calculation():
    data_A = np.array([[5, 8, 2], [-1, 3, 1], [2, 0, 3]])
    data_B = np.array([[2, 4, 1], [3, -1, 8], [0, 1, 2]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def fourth_calculation():
    data_A = np.array([[1, 0, 2], [-1, 2, 1], [2, 0, 1]])
    data_B = np.array([[2, 1, 0], [3, -1, 4], [0, 0, 2]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def main():
    read_np()
    create_chessboard()
    process_and_multiply_matrices()
    # Uncomment the following lines to run the calculations
    # first_calculation()
    # second_calculation()
    # third_calculation()
    # fourth_calculation()


if __name__ == "__main__":
    main()