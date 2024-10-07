#!/usr/bin/python3
import sys

def print_solution(board, N):
    """Prints the solution as a list of positions of queens"""
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N):
    """Solves the N queens problem using backtracking"""
    if col == N:
        print_solution(board, N)
        return True

    res = False
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            res = solve_nqueens(board, col + 1, N) or res
            board[row][col] = 0  # Backtrack

    return res

def nqueens(N):
    """Initializes the board and starts solving for N queens"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens(board, 0, N):
        print("No solution found")

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
