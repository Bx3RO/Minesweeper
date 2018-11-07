#This is to test git
from functions import set_board, touching, recursive_touching

def play():
    alive = True
    x, y, z = int(input('How many rows? ')), int(input('How many columns? ')), int(input('How many bombs? '))
    remaining = 1
    secret_board = set_board(x, y, z)
    visible = set_board(x, y, 0)
    for i in range(1, x+1):
        for j in range(1, y+1):
            visible[i][j] = '?'
    print()
    for i in visible:
        print(*i)
    print()
    while alive and remaining > 0:
        r, c = int(input('Select a row: ')), int(input('Select a column: '))
        print()
        visible[r][c] = secret_board[r][c]
        if visible[r][c] == '*':
            for i in visible:
                print(*i)
            print()
            print('Game over')
            alive = False
            break
        if visible[r][c] == ' ':
            touchers = touching([r, c], x, y)
            for spot in touchers:
                visible[spot[0]][spot[1]] = secret_board[spot[0]][spot[1]]
                if visible[spot[0]][spot[1]] == ' ':
                    touchers += [new_spot for new_spot in recursive_touching(spot, x, y) if visible[new_spot[0]][new_spot[1]] == '?']
            for i in visible:
                print(*i)
        else:
            for i in visible:
                print(*i)
        remaining = -z
        for i in visible:
            remaining += i.count('?')
        print('Non-bomb cells remainging: {}'.format(remaining))
    print()
    if remaining == 0:
        for i in secret_board:
            print(*i)
        print('You win!')
play()