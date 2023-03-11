#!/usr/bin/python3
"""print elements in a list of lists in matrix form
    Args:
        matrix: the element that contain list of list
    Returns:
        NULL
    """


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")

        print("")
