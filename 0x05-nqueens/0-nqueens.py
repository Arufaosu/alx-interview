#!/usr/bin/python3
"""queens"""
import sys

total_solutions = []


def solve_nqueens(board, N, solution, row):
    """checks if there is a queen"""
    if row == N:
        print(solution)
        global total_solutions
        total_solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, N, row, col):
            board[row][col] = 1

            solution.append([row, col])

            solve_nqueens(board, N, solution, row + 1)

            solution.pop()
            board[row][col] = 0


def is_safe(board, N, row, col):
    """ tells if a square is safe or not"""
    up_row = row
    left_col = col
    right_col = col

    while up_row >= 0:
         if board[up_row][col] == 1:
             return False

         if left_col >= 0 and board[up_row][left_col] == 1:
             return False

         if right_col < N and board[up_row][right_col] == 1:
             return False
         
         up_row -= 1
         left_col -= 1
         right_col += 1
         
         return True

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solve_nqueens(board, N, [], 0)
