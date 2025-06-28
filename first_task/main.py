import numpy as np
from Matrix import Matrix, RandomMatrix, DiagonalMatrix

def find_max_in_np():
    line = input("Enter a line of numbers separated by spaces: \n")
    np_array = np.array([int(x) for x in line.split()])
    print("You entered:", np_array)
    print("Max value in the array:", np.max(np_array))

def create_diagonal_matrix():
    size = int(input("Enter the size of the diagonal Matrix: \n"))
    chessboard = DiagonalMatrix(size)
    print(f"Diagonal Matrix of size {size}:\n{chessboard}")

def create_random_matrix_from_file():
    with open("input.txt", 'r') as f:
        line = f.readline()
    rows, cols = map(int, line.split())
    matrix = RandomMatrix(rows, cols)
    return matrix

def process_and_add_matrices():
    A = create_random_matrix_from_file()
    B = RandomMatrix(A.rows, A.cols)
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")

    min_value = A.find_min_values(is_row=True)
    print(f"Min values of A by row: {min_value}")
    A.substract_from_list(min_value, is_row=True)
    print(f"Matrix A after substruct by min values of each row:\n{A}")
    C = A + B
    print(f"Result of A + B:\n{C}")
    C.write_to_file("result_matrix")

def first_calculation():
    data_A = np.array([[2, 4], [6, 2]])
    data_B = np.array([[2, -2], [3, 2]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def second_calculation():
    data_A = np.array([[2, 4], [7, 2]])
    data_B = np.array([[-6, -2], [3, 3]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def third_calculation():
    data_A = np.array([[5, 5, 3], [-1, 2, 1], [2, -1, 3]])
    data_B = np.array([[-2, 4, 1], [5, 1, 6], [0, 1, -2]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def fourth_calculation():
    data_A = np.array([[1, 0, 2], [0, 2, 1], [2, 0, 1]])
    data_B = np.array([[0, 1, 0], [3, 1, 4], [0, 0, 2]])
    A = Matrix(data_A.shape[0], data_A.shape[1], matrix=data_A)
    B = Matrix(data_B.shape[0], data_B.shape[1], matrix=data_B)

def main():
    find_max_in_np()
    create_diagonal_matrix()
    process_and_add_matrices()
    # Uncomment the following lines to run the calculations
    # first_calculation()
    # second_calculation()
    # third_calculation()
    # fourth_calculation()


if __name__ == "__main__":
    main()