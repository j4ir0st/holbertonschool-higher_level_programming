#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[columnas ** 2 for columnas in filas] for filas in matrix]
    return (new_matrix)
