import numpy as np
import random as rd

class Matrix:
    def __init__(self, rows, cols, fill=0, matrix=None):
        self.rows = rows
        self.cols = cols
        self.data = np.zeros((rows, cols), dtype=float) + fill
        if matrix is not None:
            if isinstance(matrix, np.ndarray):
                if matrix.shape != (rows, cols):
                    raise ValueError("Provided matrix dimensions do not match")
                self.data = np.copy(matrix)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __identity_matrix__(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to create identity matrix")
        identity = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            identity[i, i] = 1
        return identity

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Incompatible dimensions for addition")
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + other[i, j]
            return result
        else:
            raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Incompatible dimensions for subtraction")
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - other[i, j]
            return result
        else:
            raise TypeError("Unsupported type for subtraction")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Incompatible dimensions for multiplication")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    result[i, j] = sum(self[i, k] * other[k, j] for k in range(self.cols))
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] * other
            return result
        else:
            raise TypeError("Unsupported type for multiplication")

    def __pow__(self, pow):
        if not isinstance(pow, int) or pow < 0:
            raise ValueError("Power must be a non-negative integer")
        if not self.rows == self.cols:
            raise ValueError("Matrix must be square for exponentiation")
        result = Matrix(self.rows, self.cols).__identity_matrix__()
        for _ in range(pow):
            result = result * self
        return result

    def copy_matrix(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only copy from another Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to copy")
        self.data = np.copy(other.data)

    def find_min_values(self, is_row=True):
        if is_row:
            return np.min(self.data, axis=1)
        else:
            return np.min(self.data, axis=0)

    def substract_from_list(self, lst, is_row=True):
        if len(lst) != (self.rows if is_row else self.cols):
            raise ValueError("Length of list must match the number of rows or columns")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                if is_row:
                    result[i, j] = self[i, j] - lst[i]
                else:
                    result[i, j] = self[i, j] - lst[j]
        self.data = result.data

    def write_to_file(self, filename):
        with open(f"{filename}.txt", 'w') as f:
            for i in range(self.rows):
                row_data = ";".join(self.data[i].astype(str))
                f.write(row_data + "\n")

class RandomMatrix(Matrix):
    def __init__(self, rows, cols, is_int = True):
        super().__init__(rows, cols, fill=1)
        for i in range(rows):
            for j in range(cols):
                self[i, j] = rd.randint(0, 100) if is_int else rd.uniform(0, 100)

class DiagonalMatrix(Matrix):
    def __init__(self, size, fill=0):
        super().__init__(size, size, fill=fill)
        for i in range(size):
            self[i, i] = 1
            self[i, size - 1 - i] = 1