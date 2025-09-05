# Sudoku Solver using Backtracking Algorithm

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Function to find the next empty cell (0 means empty)
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None

# Function to check if placing a number is valid
def is_valid(grid, num, pos):
    row, col = pos

    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Backtracking solver
def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            # Backtrack
            grid[row][col] = 0

    return False

# Example Sudoku puzzle (0 = empty cell)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_grid(sudoku_grid)

if solve(sudoku_grid):
    print("\nSolved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("No solution exists")
