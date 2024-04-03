HOD = ['x', 'o']


def print_pole():
    for i in pole:
        for j in i:
            print(j, end='\t')
        print()


def win(h):
    d1, d2 = 1, 1
    for j in range(1, 4):
        r, c = 1, 1
        for i in range(1, 4):
            c *= pole[j][i] == HOD[h]
            r *= pole[i][j] == HOD[h]
        d1 *= pole[j][j] == HOD[h]
        d2 *= pole[j][-j] == HOD[h]
        if c or r:
            print(f'Выиграл {h + 1} игрок!')
            return True
    if d1 or d2:
        print(f'Выиграл {h + 1} игрок!')
        return True
    return False


def game():
    h = 0
    while True:
        while True:
            print(f'{h + 1} игрок, напишите номер строки и столбца через пробел:')
            x, y = map(int, input().split())
            if pole[x][y] == '-':
                pole[x][y] = HOD[h]
                break
            print('Эта клетка занята, выберете другую!')
        print_pole()
        if win(h):
            return
        if all([pole[i][j] != '-' for i, j in zip(list(range(1, 4)), list(range(1, 4)))]):
            print('Ничья!')
            return
        h = 0 if h == 1 else 1


while True:
    print('Хотите начать новую игру?')
    ans = input()
    if ans.lower() == 'yes' or ans.lower() == 'да':
        pole = [['', 1, 2, 3]]
        for i in range(1, 4):
            pole.append([i, '-', '-', '-'])
        print_pole()
        game()
    else:
        break
