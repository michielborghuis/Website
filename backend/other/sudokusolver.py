sudoku = []

def grid():
    count = 0
    global sudoku
    for i in range(9):
        count += 1
        str_row = ''
        while len(str_row) != 9:
            str_row = input("Row {}: ".format(count))
            int_row = []
            for i in str_row:
                int_row.append(int(i))
            sudoku.append(int_row)


def print_board(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")


def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if solve(sudoku):
                return True
            sudoku[row][col] = 0
    return False


def valid(sudoku, num, pos):
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 +3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudoku[i][j] == num and (i,j) != pos:
                return False
    return True


def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)
    return None


def main():
    grid()
    print_board(sudoku)
    print('\n\n')
    solve(sudoku)
    print_board(sudoku)

if __name__ == "__main__":
    main()
