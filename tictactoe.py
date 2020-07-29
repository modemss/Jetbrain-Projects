lst = []
flag = 0


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
            print('You should enter numbers!')
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
        if y == 0:
            y = y + 2
        elif y == 2:
            y = y - 2
        if lst[y][x] == '_':
            lst[y][x] = XO
            break
        else:
            print('This cell is occupied! Choose another one!')
            continue


def computermove(inp):
    import random
    global lst
    global XO
    displayi(lst)
    print('Making move level "easy"')
    emptylst = [(i, j) for i in range(3) for j in range(3) if lst[i][j] == '_']
    k, l = random.choice(emptylst)
    lst[k][l] = inp


def compMed(inp):
    from copy import deepcopy
    import random
    global lst
    global XO
    displayi(lst)
    print('Making move level "Medium"')
    posmove = [(i, j) for i in range(3) for j in range(3) if lst[i][j] == '_']
    alcheck = []
    if inp == 'X':
        opp = 'O'
    elif inp == 'O':
        opp = 'X'
    while True:
        k, l = random.choice(posmove)
        newlst = deepcopy(lst)
        newlst2 = deepcopy(lst)
        newlst[k][l] = opp
        newlst2[k][l] = inp
        alcheck.append((k, l))
        if set(alcheck) == set(posmove):
            lst[k][l] = inp
            break
        if checkrows(newlst):
            lst[k][l] = inp
            break
        if checkrows(newlst2):
            lst[k][l] = inp
            break
        if checkcols(newlst):
            lst[k][l] = inp
            break
        if checkcols(newlst2):
            lst[k][l] = inp
            break
        if checkdi(newlst):
            lst[k][l] = inp
            break
        if checkdi(newlst2):
            lst[k][l] = inp
            break


def compH(inp):
    from copy import deepcopy
    import random
    global lst
    global XO
    defense = False
    displayi(lst)
    print('Making move level "Hard"')
    score = 0
    posmove = [(i, j) for i in range(3) for j in range(3) if lst[i][j] == '_']
    if inp == 'X':
        opp = 'O'
    elif inp == 'O':
        opp = 'X'
    for i in posmove:
        newlst = deepcopy(lst)
        newlst[i[0]][i[1]] = opp
        if checkwin(newlst):
            defense = True
            lst[i[0]][i[1]] = inp
            break
    if not defense:
        for pos in posmove:
            newlst2 = deepcopy(lst)
            newlst2[pos[0]][pos[1]] = inp
            if checkwin(newlst2):
                lst[pos[0]][pos[1]] = inp
                break
            else:
                k, l = random.choice(posmove)
                lst[k][l] = inp
                break


def checkwin(lis):
    if checkrows(lis) or checkcols(lis) or checkdi(lis):
        return True
    else:
        return False


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


def checkdi(dia):
    if '_' not in [dia[0][0], dia[2][2], dia[1][1]] or '_' not in [dia[0][2], dia[1][1], dia[2][0]]:
        if dia[0][0] == dia[2][2] == dia[1][1] or dia[0][2] == dia[1][1] == dia[2][0]:
            return True
    else:
        return False


def checkcols(flst):
    new_list = checkrows(transpose(flst))
    return new_list


def play1():
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


def stage1AI():
    global lst
    global XO
    inputi()
    displayi(lst)
    new_lst = [j for i in lst for j in i]
    if new_lst.count('X') > new_lst.count('O'):
        XO = 'O'
    else:
        XO = 'X'
    if '_' in new_lst:
        coordinp()
        if checkrows(lst):
            displayi(lst)
            print(checkrows(lst) + ' wins')
        elif checkcols():
            displayi(lst)
            print(checkcols() + ' wins')
        elif checkdi():
            displayi(lst)
            print(lst[1][1] + ' wins')
        elif noonewin():
            displayi(lst)
            print('Draw')
        else:
            displayi(lst)
            print('Game not finished')
    else:
        print('Draw')


def stage2AI():
    import random
    random.seed()
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
        if XO == 'X':
            coordinp()
        else:
            computermove()
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


def menu():
    while True:
        command = input('Input command: ').split()
        if command[0] == 'exit':
            quit()
        if len(command) == 3 and command[0] == 'start':
            if command[1] in ['user', 'easy', 'medium', 'hard'] and command[2] in ['user', 'easy', 'medium', 'hard']:
                _, player1, player2 = command
                return [player1, player2]
                break
        else:
            print('Bad parameters!')
            continue


def playstage4AI():
    global lst, XO, flag2
    flag2 = 0
    userinfo = menu()
    inputiG()
    while True:
        if flag2 % 2 == 0:
            XO = 'X'
            if userinfo[0] == 'user':
                displayi(lst)
                coordinp()
            elif userinfo[0] == 'easy':
                computermove('X')
            elif userinfo[0] == 'medium':
                compMed('X')
            elif userinfo[0] == 'hard':
                compH('X')
        else:
            XO = 'O'
            if userinfo[1] == 'user':
                displayi(lst)
                coordinp()
            elif userinfo[1] == 'easy':
                computermove('O')
            elif userinfo[1] == 'medium':
                compMed('O')
            elif userinfo[1] == 'hard':
                compH('O')
        flag2 += 1
        if checkrows(lst):
            displayi(lst)
            print(checkrows(lst) + ' wins')
            break
        elif checkcols(lst):
            displayi(lst)
            print(checkcols(lst) + ' wins')
            break
        elif checkdi(lst):
            displayi(lst)
            print(lst[1][1] + ' wins')
            break
        elif noonewin():
            displayi(lst)
            print('Draw')
            break


playstage4AI()
