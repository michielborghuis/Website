import numpy

sudoku = [[5, 3, 4, 6, 7, 8, 1, 9, 2],
          [6, 7, 2, 1, 9, 6, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7]]


def grid():
    count = 0
    global sudoku
    for i in range(9):
        count += 1
        str_row = input("Row {}: ".format(count))
        int_row = []
        for i in str_row:
            int_row.append(int(i))
        sudoku.append(int_row)
    print(numpy.matrix(sudoku))


def possible(y,x,n):
    global sudoku
    for i in range(0,9):
        if sudoku[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+1][x0+j] == n:
                return False
    return True


def solve():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        sudoku[y][x] = n
                        solve()
                        sudoku[y][x] = 0
                return
    print(numpy.matrix(sudoku))
    input("More?")
#grid()
solve()