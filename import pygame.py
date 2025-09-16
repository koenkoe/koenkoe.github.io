import pygame
import time
import random
import sys
import math

pygame.init()
BREEDTE = 600
HOOGTE = 600
screen = pygame.display.set_mode((BREEDTE, HOOGTE))
pygame.display.set_caption("Darleks")
clock = pygame.time.Clock()
schaal = 40


rijen = int(((BREEDTE - 25) - 15) / schaal)
colome = int(((HOOGTE - 25) - 15) / schaal)


vr = {
    "speler_x": 15,
    "speler_y": 15,
    "running": True,
    "mainscreen": True,
    "level": 0,
    "dalekses": [],
    "hoopjes" : [],
    "dood": False,
    "score" : 0,
    "gewonnen": False,
    "screw": True,
    "daleksonscreen": False,
    "settingss": False,
    "playerkleur": (0,0,0),

}
x = random.randint(0, rijen)
y = random.randint(0, colome)
vr["speler_x"] = (x * schaal) + 15
vr["speler_y"] = (y * schaal) + 15 

WIT = (255, 255, 255)
ZWART = (0, 0, 0)
ROOD = (255, 0, 0)
GROEN = (0, 255, 0)
BRUIN = (150, 75, 0)
GOUD = (255, 215, 0)

def dotplilbro():
    x = random.randint(0, rijen)
    y = random.randint(0, colome)
    vr["speler_x"] = (x * schaal) + 15
    vr["speler_y"] = (y * schaal) + 15

def move():
    nieuw = []
    for (x, y) in vr["dalekses"]:
        if x < vr["speler_x"]:
            x += schaal
        elif x > vr["speler_x"]:
            x -= schaal

        if y < vr["speler_y"]:
            y += schaal
        elif y > vr["speler_y"]:
            y -= schaal

        nieuw.append((x, y))

    vr["dalekses"] = nieuw

def daleksescheck():
    global vr
    nieuw = []
    for i in vr["dalekses"]:
        if vr["dalekses"].count(i) == 1 and i not in vr["hoopjes"]  :
            nieuw.append(i)
        else:
            vr["hoopjes"].append(i)
            vr["score"] += 10
    vr["dalekses"] = nieuw

def hoopjes():
    global vr
    for (x, y) in vr["hoopjes"]:
        pygame.draw.circle(screen, (120, 120, 120), (x+5, y+5), 8)

        # extra "metaalstukken"
        pygame.draw.rect(screen, (100, 100, 100), (x, y, 6, 3))
        pygame.draw.rect(screen, (80, 80, 80), (x+4, y+7, 8, 3))
        pygame.draw.circle(screen, (150, 150, 150), (x+10, y+2), 3)
        pygame.draw.circle(screen, (90, 90, 90), (x+2, y+10), 2)

def spawndaleks():
    vr["dalekses"] = []
    vr["daleksonscreen"] = True
    for i in range((vr["level"] * 2) + 1):
        while True:
            x = int(random.randint(0, rijen) )
            y = int(random.randint(0, colome) )
            dalek_x = (x * schaal) + 15
            dalek_y = (y * schaal) + 15
            afstand = math.dist((dalek_x, dalek_y), (vr["speler_x"], vr["speler_y"]))
            if (afstand >= (schaal * 5)) and ((dalek_x, dalek_y) not in vr["dalekses"]):
                vr["dalekses"].append((dalek_x, dalek_y))
                pygame.draw.rect(screen, ROOD, (dalek_x, dalek_y, 10, 10))
                pygame.display.update()
                break


def drawdalekses():
    for (x, y) in vr["dalekses"]:

        # Lichaam (kleine rode rechthoek)
        pygame.draw.rect(screen, (150, 0, 0), (x, y+2, 10, 8))

        # Kop (kleine rode cirkel bovenop)
        pygame.draw.circle(screen, (100, 0, 0), (x+5, y), 4)

        # Oogstok
        pygame.draw.line(screen, (0,0,0), (x+5, y), (x+10, y-2), 1)
        pygame.draw.circle(screen, (0,0,255), (x+10, y-2), 2)

        # Versiering (zwart bolletje onder)
        pygame.draw.circle(screen, (0,0,0), (x+3, y+8), 2)
        pygame.draw.circle(screen, (0,0,0), (x+7, y+8), 2)

   
def doscrew():
    nieuw = []
    for (dx, dy) in vr["dalekses"]:
        afstand = math.dist((dx, dy), (vr["speler_x"], vr["speler_y"]))
        if afstand >= (schaal * 1.5):
            nieuw.append((dx, dy))
        else :
            vr["score"] += 5
            vr["hoopjes"].append((dx,dy))
    vr["dalekses"] = nieuw
    vr["screw"] = False

def lijnentekenen():
    lijn = 0
    # teken grid
    while (lijn * schaal) <= BREEDTE:
        pygame.draw.line(screen, ZWART, ((lijn * schaal), 0), ((lijn * schaal), HOOGTE))
        pygame.draw.line(screen, ZWART, (0, (lijn * schaal)), (BREEDTE, (lijn * schaal)))
        lijn += 1




def daleksesdood():
    if len(vr["dalekses"]) == 0:
        vr["gewonnen"] = True
        vr["daleksonscreen"] = False

def tekenspeler():
    global vr
    pygame.draw.circle(screen, (100, 200, 0), (vr["speler_x"]+5, vr["speler_y"]+5), 5)

    # Lichaam
    pygame.draw.rect(screen, vr["playerkleur"], (vr["speler_x"], vr["speler_y"]+10, 10, 10))

    # Armen
    pygame.draw.line(screen, (0,0,0), (vr["speler_x"], vr["speler_y"]+12), (vr["speler_x"]-5, vr["speler_y"]+15), 2)
    pygame.draw.line(screen, (0,0,0), (vr["speler_x"]+10, vr["speler_y"]+12), (vr["speler_x"]+15, vr["speler_y"]+15), 2)

    # Benen
    pygame.draw.line(screen, (0,0,0), (vr["speler_x"]+3, vr["speler_y"]+20), (vr["speler_x"]+3, vr["speler_y"]+25), 2)
    pygame.draw.line(screen, (0,0,0), (vr["speler_x"]+7, vr["speler_y"]+20), (vr["speler_x"]+7, vr["speler_y"]+25), 2)

def checkdood():
    for (x, y) in vr["dalekses"]:
        if (vr["speler_x"] == x and vr["speler_y"] == y):
            vr["dood"] = True
    for (x, y) in vr["hoopjes"]:
        if (vr["speler_x"] == x and vr["speler_y"] == y):
            vr["dood"] = True

def doodscherm():
        global vr
        screen.fill(ROOD)
        font = pygame.font.SysFont(None, 72)
        tekst = font.render("You died", True, (255, 255, 255))
        screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, HOOGTE // 2 - 100))
        font = pygame.font.SysFont(None, 40)
        tekst = font.render("Score: "+ str(vr["score"]), True, (255, 255, 255))
        screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, HOOGTE // 2 - 50))
        tekst = font.render("Press space to restart or esc to exit!", True, (255, 255, 255))
        screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, HOOGTE // 2 ))
        pygame.display.update()
        while vr["running"] == True and vr["mainscreen"] != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    vr["running"] = False
                    vr["mainscreen"] = False
                    vr["settingss"] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        vr["running"] = False
                        vr["mainscreen"] = False
                        vr["settingss"] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        vr = {
    "speler_x": 15,
    "speler_y": 15,
    "running": True,
    "mainscreen": True,
    "level": 0,
    "dalekses": [],
    "hoopjes" : [],
    "dood": False,
    "score" : 0,
    "gewonnen": False,
    "screw": True,
    "daleksonscreen": False,
    "settingss": False,
    "playerkleur": (0,0,0),

}
        

def winscherm():
    global vr

def settings_menu():
    vr["settingss"] = True
    while vr["settingss"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vr["running"] = False
                vr["mainscreen"] = False
                vr["settingss"] = False
        clock.tick(60)
        screen.fill(GROEN)
        font = pygame.font.SysFont(None, 72)
        font1 = pygame.font.SysFont(None, 32)
        tekst = font.render("Settings", True, (255, 255, 255))
        screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, 50))
        #zwart
        button_xz = 100
        button_yz = 200
        pygame.draw.rect(screen, ZWART, (button_xz , button_yz, 50, 50))
        knop_rectz = pygame.Rect(button_xz, button_yz, 50, 50)
        #bruin
        button_xb = 400
        button_yb= 200
        pygame.draw.rect(screen, BRUIN, (button_xb , button_yb, 50, 50))
        knop_rectb = pygame.Rect(button_xb, button_yb, 50, 50)
        muispos = pygame.mouse.get_pos()
        muiscl = pygame.mouse.get_pressed()

        if knop_rectz.collidepoint(muispos) and (muiscl[0] == True):
            vr["playerkleur"] = (0,0,0)
            tekst = font1.render("Color updated", True, (255, 255, 255))
            screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, 100))
            pygame.display.update()
            pygame.time.delay(1000)
        pygame.draw.rect(screen, BRUIN, (button_xb , button_yb, 50, 50))
        knop_rect = pygame.Rect(button_xb, button_yb, 50, 50)
        
        if knop_rectb.collidepoint(muispos) and (muiscl[0] == True):
            vr["playerkleur"] = (150, 75, 0)
            tekst = font1.render("Color updated", True, (255, 255, 255))
            screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, 100))
            pygame.display.update()
            pygame.time.delay(1000)
        
        
        if vr["level"]  >= 4: 
            button_x = 100
            button_y = 400
            pygame.draw.rect(screen, GOUD, (button_x , button_y, 50, 50))
            knop_rect = pygame.Rect(button_x, button_y, 50, 50)
            if knop_rect.collidepoint(muispos) and (muiscl[0] == True):
                vr["playerkleur"] = (255, 215, 0)
                tekst = font1.render("Color updated", True, (255, 255, 255))
                screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, 100))
                pygame.display.update()
                pygame.time.delay(1000)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    vr["settingss"] = False
            if event.type == pygame.QUIT:
                vr["settingss"] = False
                vr["running"] = False
        pygame.display.update()

def main_menu():
    vr["mainscreen"] = True
    while vr["mainscreen"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vr["running"] = False
                vr["mainscreen"] = False
                vr["settingss"] = False
        clock.tick(60)
        screen.fill(ZWART)
        font = pygame.font.SysFont(None, 48)
        tekst = font.render("Main screen", True, WIT)
        screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, 50))
        tekst2 = font.render("Press space to start!", True, WIT)
        screen.blit(tekst2, (BREEDTE // 2 - tekst2.get_width() // 2, 120))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vr["mainscreen"] = False
            if event.type == pygame.QUIT:
                vr["mainscreen"] = False
                vr["running"] = False
        pygame.display.update()

def gameloop():
        clock.tick(60)
        screen.fill(WIT)
        pygame.display.set_caption("Darleks level = "  + str(vr["level"]) + "     Score: " + str(vr["score"]))

        lijnentekenen()
        tekenspeler()

        if not vr["daleksonscreen"]:
            vr["level"] += 1
            spawndaleks()
        else:
            drawdalekses()
        hoopjes()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vr["running"] = False
                vr["mainscreen"] = False
                vr["settingss"] = False

                

            if event.type == pygame.KEYDOWN:
                # beweging - gebruik vr waarden
                if (event.key in (pygame.K_LEFT, pygame.K_a)) and vr["speler_x"] != 15:
                    vr["speler_x"] -= schaal
                    move()
                elif (event.key in (pygame.K_RIGHT, pygame.K_d)) and vr["speler_x"] != (BREEDTE - 25):
                    vr["speler_x"] += schaal
                    move()
                elif (event.key in (pygame.K_UP, pygame.K_w)) and vr["speler_y"] != 15:
                    vr["speler_y"] -= schaal
                    move()
                elif (event.key in (pygame.K_DOWN, pygame.K_s)) and vr["speler_y"] != (HOOGTE - 25):
                    vr["speler_y"] += schaal
                    move()
                elif (event.key == pygame.K_q) and (vr["speler_x"] != 15 and vr["speler_y"] != 15):
                    vr["speler_x"] -= schaal
                    vr["speler_y"] -= schaal
                    move()
                elif (event.key == pygame.K_e) and ((vr["speler_x"] != (BREEDTE - 25)) and vr["speler_y"] != 15):
                    vr["speler_x"] += schaal
                    vr["speler_y"] -= schaal
                    move()
                elif (event.key == pygame.K_x) and ((vr["speler_x"] != (BREEDTE - 25)) and (vr["speler_y"] != (HOOGTE - 25))):
                    vr["speler_x"] += schaal
                    vr["speler_y"] += schaal
                    move()
                elif (event.key == pygame.K_z) and ((vr["speler_x"] != 15) and (vr["speler_y"] != (HOOGTE - 25))):
                    vr["speler_x"] -= schaal
                    vr["speler_y"] += schaal
                    move()
                elif (event.key == pygame.K_j) and vr["screw"]:
                    doscrew()
                elif (event.key == pygame.K_l):
                    move()
                elif (event.key == pygame.K_t):
                    dotplilbro()
                elif (event.key == pygame.K_ESCAPE):
                    settings_menu()

        daleksescheck()
        daleksesdood()
        checkdood()
        
        if vr["dood"] ==  True:
            doodscherm()

        if vr["gewonnen"] == True:
            vr["gewonnen"] = False
            vr["screw"] = True
            vr["hoopjes"] = []
            screen.fill(GROEN)
            font = pygame.font.SysFont(None, 72)
            tekst = font.render("GEWONNEN WAZAAAA", True, (255, 255, 255))
            screen.blit(tekst, (BREEDTE // 2 - tekst.get_width() // 2, HOOGTE // 2 - 50))
            pygame.display.update()
            pygame.time.delay(3000)

        pygame.display.update()


while vr["running"] ==  True:
    if vr["mainscreen"] == True:
        main_menu()
    else:
        gameloop()



