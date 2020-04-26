import sys

width, height = [int(i) for i in input().split()]


def is_exit(board, x, y):
    try:
        return board[y][x] == "0"
    except Exception as e:
        return False


def compute_number_close_exit(board, x, y):
    number = 0
    neighbour = [
        (x - 1, y),
        (x + 1, y),
        (x, y + 1),
        (x, y - 1),
    ]
    for (xbis, ybis) in neighbour:
        if -1 < xbis < width:
            if -1 < ybis < height:
                if is_exit(board, xbis, ybis):
                    number += 1
    return str(number)


board = []
for i in range(height):
    line = list(input())
    board.append(line)
new_board = []
for y in range(height):
    new_line = []
    for x in range(width):
        if is_exit(board, x, y):
            new_line.append(compute_number_close_exit(board, x, y))
        else:
            new_line.append("#")
    new_board.append(new_line)

for i in range(height):
    print("".join(new_board[i]))
