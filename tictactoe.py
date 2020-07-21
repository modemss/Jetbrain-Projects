lst = []
flag = 0
import string
def inputi():
    global inp
    global lst
    inp = input('Enter cells: ')
    lst = [[inp[i] for i in range(3)], [inp[i] for i in range(3, 6)], [inp[i] for i in range(6, 9)]]
def inputiG():
    global inp
    global lst
    inp = '_________'
    lst = [[inp[i] for i in range(3)], [inp[i] for i in range(3, 6)], [inp[i] for i in range(6, 9)]]
def noonewin():
    global lst
    noone = [lst[i][j] for i in range(3) for j in range(3)]
    if '_' not in noone:
        return True
    else:
        return False
def displayi(ilst):
    print('---------')
    for i in range(len(ilst)):
        print('|', *ilst[i], '|', sep=' ')
    print('---------')
def coordinp():
    global lst
    global XO
    while True:
        try:
            x, y = input('Enter the coordinates: ').split()
        except ValueError:
            print('Enter both coordinates!')
            continue
        if x.isdigit() is False or y.isdigit() is False:
            print("You should enter numbers!")
            continue
        x, y = int(x), int(y)
        if x not in range(1, 4) or y not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue
        x = x - 1
        y = y - 1
        if y == 0: y = y + 2
        elif y == 2: y = y - 2
        if lst[y][x] == '_':
            lst[y][x] = XO
            break
        else:
            print('This cell is occupied! Choose another one!')
            continue
def transpose(ilst):
    newlst = [[ilst[j][i] for j in range(len(ilst))] for i in range(len(ilst[0]))]
    return newlst
def toomuch():
    new_list = [i for i in inp]
    if inp.count('X') - inp.count('O') > 1 or inp.count('O') - inp.count('X') > 1:
        return True
    else:
        return False
def notfinished(ilst):
    count = 0
    for i in range(3):
        if '_' in ilst[i]:
            count += 1
            continue
    if count == 3:
        return True
    else:
        return False
def checkrows(chlst: list):
    count = 0
    global flag
    lst_ = []
    for i in chlst:
        if 'O' in i or 'X' in i:
            if all(j == i[0] for j in i):
                lst_.append(i[0])
                count += 1
    if count > 1:
        flag += 1
        return False
    elif count != 1:
        return False
    else:
        return lst_[0]
def checkdi():
    if '_' not in [lst[0][0], lst[2][2], lst[1][1]] or '_' not in [lst[0][2], lst[1][1], lst[2][0]]:
        if lst[0][0] == lst[2][2] == lst[1][1] or lst[0][2] == lst[1][1] == lst[2][0]:
            return True
    else:
        return False
def checkcols():
    flst = lst.copy()
    new_list = checkrows(transpose(flst))
    return new_list

def play():
    global lst
    global flag
    while True:
        flag = 0
        inputi()
        displayi(lst)
        if toomuch():
            print('Impossible')
        elif checkrows(lst):
            print(checkrows(lst) + ' wins')
        elif checkcols():
            print(checkcols() + ' wins')
        elif flag != 0:
            print('Impossible')
        elif checkdi():
            print(checkdi() + ' wins')
        elif noonewin():
            print('Draw')
        else:
            print('Game not finished')
        continue
def playsec():
    inputi()
    displayi(lst)
    if toomuch():
        print('Impossible')
    elif checkrows(lst):
        print(checkrows(lst) + ' wins')
    elif checkcols():
        print(checkcols() + ' wins')
    elif flag != 0:
        print('Impossible')
    elif checkdi():
        print(checkdi() + ' wins')
    elif noonewin():
        print('Draw')
    else:
        print('Game not finished')
def stage4():
    inputi()
    displayi(lst)
    coordinp()
    displayi(lst)
def play():
    global lst
    global XO
    lst = []
    inputiG()
    flag2 = 0
    while True:
        if flag2 % 2 == 0:
            XO = 'X'
        else:
            XO = 'O'
        displayi(lst)
        coordinp()

        flag2 += 1
        if checkrows(lst):
            displayi(lst)
            print(checkrows(lst) + ' wins')
            break
        elif checkcols():
            displayi(lst)
            print(checkcols() + ' wins')
            break
        elif checkdi():
            displayi(lst)
            print(lst[1][1] + ' wins')
            break
        elif noonewin():
            displayi(lst)
            print('Draw')
            break
play()







