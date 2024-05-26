#!/usr/bin/python3
"""
divides the elements of a matrix based on a number
"""


def matrix_divided(matrix, div):
    """
    function that divides a matrix

    Args:
        matrix: the matrix to divide
        div: the number that divides

    Returns:
        a new matrix

    Raises:
        TypeError if matrix isnt a list of integers of floats, if each row of the matrix doesnt have
        the same size or if div isnt a number
        ZeroDivisionError if div is zero
    """
    if not all(isinstance(i, list) for i in matrix) or not all(isinstance(num, (int, float)) for i in matrix for num in i):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
