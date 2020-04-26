import copy

def is_cell_empty(board, x, y):
    return board[y][x] == "."


def is_cell_0(board, x, y):
    return board[y][x] == "O"


def is_board_win(board):
    # Test columns
    for x in range(3):
        is_column_win = True
        for y in range(3):
            is_column_win = is_column_win and is_cell_0(board, x, y)
        if is_column_win:
            return True

    # Test lines
    for y in range(3):
        is_line_win = True
        for x in range(3):
            is_line_win = is_line_win and is_cell_0(board, x, y)
        if is_line_win:
            return True

    # Test diagonals
    is_first_diagonal_win = True
    for (x, y) in [(0, 0), (1, 1), (2, 2)]:
        is_first_diagonal_win = is_first_diagonal_win and is_cell_0(board, x, y)

    is_second_diagonal_win = True
    for (x, y) in [(2, 0), (1, 1), (0, 2)]:
        is_second_diagonal_win = is_second_diagonal_win and is_cell_0(board, x, y)
    if is_first_diagonal_win or is_second_diagonal_win:
        return True
    return False


def print_board(board):
    for line in board:
        print(line)


def create_new_board(board, x, y):
    new_board = copy.copy(board)
    new_line = list(new_board[y])
    new_line[x] = "O"
    new_board[y] = "".join(new_line)
    return new_board


board = []
for i in range(3):
    line = input()
    board.append(line)

for x in range(3):
    for y in range(3):
        if is_cell_empty(board, x, y):
            new_board = create_new_board(board, x, y)
            if is_board_win(new_board):
                print_board(new_board)
