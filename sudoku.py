import random as r
import os.path
path =  "E:/Code/ITGK_ovinger/Sudoku/"
brett = []
def difficulty(recursive):
    if recursive == 'first':
        opt = input('Do you wanna play Hard, Medium or easy?  H/M/E....\n')
    else:
        opt = input('One of the three: Hard, Medium or easy?  H/M/E....\n')
    if opt == 'H' or opt =='h':
        return [6,7]
    elif opt == 'm' or opt =='M':
        return [5,7] 
    elif opt == 'e' or opt == 'E':
        return [4,6]
    else:
        difficulty('again')
def remove(diff,brett):
    for i in range(9):
        number = r.randint(diff[0],diff[1])
        total = [1,2,3,4,5,6,7,8,9]
        fjern = r.sample(total,number)
        for y in fjern:
            brett[i][y-1] = '0'
    return brett
def new_game():
    brett = maker()
    diff = difficulty('first')
    brett = remove(diff,brett)
    return brett
def maker():
    brett = []
    brett.append(r.sample(range(1,10),9))
    appendes = []
    b = 1
    counter = 0
    k = 0
    while b == 1:
        b = 0
        if counter >= 5000:
            brett = brett[:len(brett)-2]
            counter = 0
            k+=1
        elif len(brett) == 8:
            counter = 4999
        if k == 10:
            brett = []
            brett.append(r.sample(range(1,10),9))
            k = 0
        counter+=1
        appendes = []
        for j in range(9):
            rad = [1,2,3,4,5,6,7,8,9]
            ikke = []
            if len(appendes) !=0:
                for y in appendes:
                    ikke.append(y)
            for k in range(len(brett)):
                ikke.append(brett[k][j])
            blokk(brett,j,ikke)
            ikke = set(ikke)
            ikke = list(ikke)
            for x in ikke:
                rad.remove(x)
            if len(rad) != 0:
                appendes.append(r.choice(rad))
        if len(appendes) != 9:
            b = 1
        if b == 0:
            brett.append(appendes)
            b=1
        if len(brett)==9:
            return brett
def blokk(brett,j,ikke):
    if len(brett)<3:
        if j<3: 
            for i in range(len(brett)):
                for k in range(3):
                        ikke.append(brett[i][k])
        elif j<6:
            for i in range(len(brett)):
                for k in range(3,6):
                        ikke.append(brett[i][k])
        else:
            for i in range(len(brett)):
                for k in range(6,9):
                        ikke.append(brett[i][k])
    elif len(brett)<6 and len(brett)>3:
        if j<3: 
            for i in range(3,len(brett)):
                for k in range(3):
                        ikke.append(brett[i][k])
        elif j<6:
            for i in range(3,len(brett)):
                for k in range(3,6):
                        ikke.append(brett[i][k])
        else:
            for i in range(3,len(brett)):
                for k in range(6,9):
                        ikke.append(brett[i][k])
    elif len(brett)>6:
        if j<3:
            for i in range(6,len(brett)):
                for k in range(3):
                        ikke.append(brett[i][k]) 
        elif j<6:
            for i in range(6,len(brett)):
                for k in range(3,6):
                        ikke.append(brett[i][k]) 
        else:
            for i in range(6,len(brett)):
                for k in range(6,9):
                        ikke.append(brett[i][k]) 
    return ikke
def hent_spill(fil):
    brett = []
    fil = os.path.join(path+fil+'.txt')
    f = open(fil,'r')
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        split = list(line)     
        if split[len(split)-1] == '\n':
            split = split[:len(split)-1]
        brett.append(split)
    f.close()
    return brett
def lagre_spill(brett,fil):
    new_fil = os.path.join(path+fil+'.txt')
    f = open(new_fil,'w+')
    for i in range(len(brett)):
        line = ''.join(str(elem) for elem in brett[i])
        if i == len(brett):
            f.write(line)
        else:    
            f.write(line+'\n')
    f.close
def slette_tall(x,y,brett,fil):
    brett[x][y] = 0
    return skriv_tall(brett, fil)
def sjekk_tall(tall):
    if tall <=9 and tall>=1:
        return True
    else:
        print('Invalid number, try again')
        return False
def sjekk_komplett(x,y,tall,brett):
    for i in range(len(brett)):
        if i == y:
            continue
        if tall == brett[x][i]:
            print('Invalid number, try again')
            return skriv_tall(brett,fil) 
    for i in range(len(brett)):
        if i == x:
            continue
        if tall == brett[i][y]:
            print('Invalid number, try again')
            return skriv_tall(brett,fil)
    for i in range(3):
        for j in range(3):
            if j == y and i == x:
                continue 
            if tall == brett[(x//3)*3+i][(y//3)*3+j]:
                print('Invalid number, try again')
                return skriv_tall(brett,fil)
    return True
def sjekk_fullført(brett):
    for i in range(9):
        for j in range(9):
            if brett[i][j] == '0':
                return False
    return True
def skriv_tall(brett,fil):
    print_spill(brett)
    if sjekk_fullført(brett) == True:
        print('\nCongratulations, you completed the sudoku!\n')
        lagre_spill(brett,fil)
        opin = input('Do you wanna play a new game? Y/N... \n')
        if opin == 'y' or opin =='Y':
            return start_spill()
        else:
            return print('Seeya')

    save = input('Continue or save game? C/S...\n')
    if save == 'S' or save == 's':
        lagre_spill(brett,fil)
        print('The game is saved under this path: "'+path+'"\n')
        cont = input('do you want to start a game again? Y/N...\n')
        if cont == 'Y' or cont == 'y':
            return start_spill()
        else:
            return print('Seeya')
    elif save == 'c' or save == 'C':
        opt = input('Do you want to insert or remove a number? I/R...\n')
        if opt == 'R' or opt =='r':
            los = str(input('Remove cell (x,y):\n'))
            pos = los.split(',')
            y = int(pos[0])
            x = int(pos[1])
            return slette_tall(x,y,brett,fil)
    else:
        print('wrong input, try again')
        skriv_tall(brett,fil)
    pos = str(input('Insert cell (x,y):\n'))
    cor = pos.split(',')
    y = int(cor[0])
    x = int(cor[1])
    tall = input('Insert number: \n')
    if sjekk_tall(x+1) == True and sjekk_tall(y+1) == True:
        if int(brett[x][y]) == 0:
            if sjekk_komplett(x,y,tall,brett) == True:
                brett[x][y] = tall
                return skriv_tall(brett,fil)
        else:
            change = input('Do you want to change the current cell? Y/N...\n')
            if change == 'Y' or change == 'y':
                if sjekk_komplett(x,y,tall,brett) == True:
                    brett[x][y] = tall
                    return skriv_tall(brett,fil)
            else:
                print('No changes has been made')
                return skriv_tall(brett,fil)
    else:
        print('Not a valid cell, try again!')
        return skriv_tall(brett,fil)
def start_spill(): 
    opt = input('Load or start new game? L/N\n')
    if opt == 'n' or opt == 'N':
        brett = new_game() 
        fil = input('Name your game: \n')
    elif opt == 'l' or opt == 'L':
        fil = input('Enter the game name: \n')
        brett = hent_spill(fil)
    else:
        start_spill()
    return skriv_tall(brett,fil)
def print_spill(brett):
    print('\n')
    print('        0   1   2     3   4   5     6   7   8    x-axis')
    print('    =============================================')
    for i in range(len(brett)):
        print('',i,' ||| ',end='')
        for j in range(len(brett[i])):
            if j == 5 or j == 2 or j == 8:
                print(brett[i][j],'||| ',end='')   
            else:
                print(brett[i][j],'| ',end='')  
        if i == 5 or i == 2:
            print('\n    =============================================')
        elif i == 8:
            print('\n    =============================================')
        else:
            print('\n    ---------------------------------------------') 
    print(' y-axis\n')
start_spill()
