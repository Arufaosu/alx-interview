#!/usr/bin/python3
"""0-rotate_2d_matrix.py"""


def rotate_2d_matrix(matrix):
    """rotate 90 degrees clockwise"""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
