#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div."""

    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all elements in the matrix are integers or floats
    for row in matrix:
        if not all(isinstance(ele, (int, float)) for ele in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all rows are of the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and non-zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements and return a new matrix
    return [[round(ele / div, 2) for ele in row] for row in matrix]
