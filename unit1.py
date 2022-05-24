def create():
    print(' Добро пожаловать, в игру! ')
    print(' КРЕСТИКИ - X vs НОЛИКИ - 0')
    print('         ИНСТРУКЦИЯ        ')
    print('1. крестик <Х> ходит первым')
    print('2. чтобы сделать ход,      ')
    print('   ведите координаты x и y:')
    print('   x - номер строки        ')
    print('   y - номер столбца       ')
    print('         УДАЧИ!!!          ')


def show_field():
    print()
    print('  | 1 | 2 | 3 |')
    print('---------------')
    for i, row in enumerate(field_play, start=1):
        print(f'{i} | {" | ".join(row)} |')
        print('---------------')
    print()


def inp_xy(step):
    while True:
        if step % 2 == 1:
            print(f'Шаг {step}. Ваш ход, КРЕСТИК "Х": ')
        else:
            print(f'Шаг {step}. Ваш ход, НОЛИК "0": ')
        coord_xy = input().split()

        if len(coord_xy) != 2:
            print('Нужно ввести 2 координаты: X и Y!')
            continue

        x, y = coord_xy

        if not x.isdigit() or not y.isdigit():
            print('Координаты X и Y должны быть положительными числами!')
            continue

        x, y = int(x), int(y)

        if (x < 1 or x > 3) or (y < 0 or y > 3):
            print(f'Введенные координаты x={x}, y={y} вне игрового поля!')
            continue

        if field_play[x - 1][y - 1] != ' ':
            print(f'Выбранная клетка x={x}, y={y} уже занята!')
            continue

        return x, y


def check_win():
    win_tab = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2))
    )

    for tab in win_tab:
        win_list = []
        for i in tab:
            win_list.append(field_play[i[0]][i[1]])
        if win_list == ['X', 'X', 'X']:
            show_field()
            print('Победил КРЕСТИК - X!!!')
            return True
        if win_list == ['0', '0', '0']:
            show_field()
            print('Победил НОЛИК - 0!!!')
            return True

    return False


create()

field_play = [[' '] * 3 for _ in range(3)]
step = 0
while True:
    step += 1
    show_field()
    if step == 10:
        print('Победителя нет! Сражайтесь сново!')
        break

    x, y = inp_xy(step)

    if step % 2 == 1:
        field_play[x - 1][y - 1] = "X"
    else:
        field_play[x - 1][y - 1] = "0"

    if check_win():
        break
