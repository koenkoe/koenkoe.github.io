import random

gameover = 0
groote = 3

bord = [
['.','.','.'],
['.','.','.'],
['.','.','.']
]


print("Links boven is 1,1 en rechtsonder is 3,3")


def gewonnen():
    global gameover
    if gameover == 1:  
        return
    for p in range(groote):
        if all(bord[p][a] == bord[p][0] and bord[p][0] != '.' for a in range(groote)): 
            if bord[p][0] == 'O':  
                print("De computer heeft gewonnen!")
                gameover = 1
            elif bord[p][0] == 'X': 
                print("Je hebt gewonnen!")
                gameover = 1
    for p in range(groote):
        if all(bord[a][p] == bord[0][p] and bord[0][p] != '.' for a in range(groote)):
            if bord[0][p] == 'O': 
                print("De computer heeft gewonnen!")
                gameover = 1
            elif bord[0][p] == 'X':  
                print("Je hebt gewonnen!")
                gameover = 1
    if bord[0][0] == bord[1][1] == bord[2][2] and bord[0][0] != '.':
        if bord[0][0] == 'O':
            print("De computer heeft gewonnen!")
        else:
            print("Je hebt gewonnen!")
        gameover = 1
    elif bord[0][2] == bord[1][1] == bord[2][0] and bord[0][2] != '.':
        if bord[0][2] == 'O':
            print("De computer heeft gewonnen!")
        else:
            print("Je hebt gewonnen!")
        gameover = 1
    if all(bord[y][x] != '.' for y in range(groote) for x in range(groote)) and gameover == 0:
        print("Het is een gelijkspel!")
        gameover = 1



def jouwinput():
    while True:
        try:
            yplaats = int(input("Op welke rij wil je een x neerzetten?: "))
            yplaats = yplaats - 1
            xplaats = int(input("Waar in het rijtje staat die?: "))
            xplaats = xplaats - 1
            if 0 <= yplaats < groote and 0 <= xplaats < groote:
                if bord[yplaats][xplaats] != '.':
                    print("deze plaats is bezet")
                else:
                    bord[yplaats][xplaats] = 'X'
                    break
                
            else:
                print("deze is buiten het speelveld!")
        except ValueError:
            print("Voer een getal in!")
        except IndexError:
            print("Deze plek is ongeldig! Probeer opnieuw")

def computerinput():
    while True:
        y = random.randint(0, 2) 
        x = random.randint(0, 2)  

        if bord[y][x] == '.': 
            bord[y][x] = 'O' 
            break  

def print_bord():
    for p in bord:
        for a in p:
            print(a, end='')
        print()


print_bord() 
while gameover == 0:

    jouwinput()  
    print_bord() 
    gewonnen() 
    if gameover == 1:
        break
    print("De computer deed:")
    computerinput() 
    if gameover == 1:
        break
    print_bord()  
    gewonnen()  

print("Einde spel!")