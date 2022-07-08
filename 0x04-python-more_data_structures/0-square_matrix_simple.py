#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    for i in matrix:
        sqr_matrix.append(list(map(lambda i: i*i, i)))
    return (sqr_matrix)
