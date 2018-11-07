from random import randint

def touching(spot, num_rows, num_cols):
    x, y, = spot[0], spot[1]
    x_touchers = [i for i in range(x-1, x+2) if i in range(1, num_rows+1)]
    y_touchers = [i for i in range(y-1, y+2) if i in range(1, num_cols+1)]
    return [(i, j) for i in x_touchers for j in y_touchers]

def recursive_touching(spot, num_rows, num_cols):
    x, y, = spot[0], spot[1]
    x_touchers = [i for i in range(x-1, x+2, 2) if i in range(1, num_rows+1)]
    y_touchers = [i for i in range(y-1, y+2, 2) if i in range(1, num_cols+1)]
    return [(i, j) for i in x_touchers for j in y_touchers]

def set_board(num_rows, num_cols, num_bombs):
    bombs, board = set(), [[i for i in range(num_cols+1)]]
    while len(bombs) < num_bombs:
        bombs.add((randint(1, num_rows), randint(1, num_cols)))
    for i in range(1, num_rows+1):
        board.append([i])
        board[i]+= [0] * num_cols
    for i in bombs:
        for x in touching(i, num_rows, num_cols):
            try: board[x[0]][x[1]] += 1
            except Exception: pass
        board[i[0]][i[1]] = '*'
    for i in range(num_rows+1):
        for j in range(num_cols+1):
            if board[i][j] == 0:
                board[i][j] = ' '
    return board