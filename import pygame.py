import pygame
import time
import random
import os
import sys





speler_x = 1
speler_y = 1



pygame.init()
info = pygame.display.Info()
BREEDTE = 600
HOOGTE = 600
screen = pygame.display.set_mode((BREEDTE,HOOGTE))  
pygame.display.set_caption("Darleks")
clock = pygame.time.Clock()
schaal = 40

#horizontalal
rijen = (((BREEDTE - 25) - 15)/schaal)
#vertivale
colome = (((HOOGTE - 25) - 15)/schaal)


speler_x = 15
speler_y = 15
WIT = (255, 255, 255)
ZWART = (0, 0, 0)
running = True


def dotplilbro():
    global speler_x,speler_y
    x = random.randint(0, rijen)
    y = random.randint(0,colome)
    speler_x = (x *schaal) + 15
    speler_y =( y *schaal) + 15





def lijnentekenen():
    lijn = 0
    while (lijn * 20) <= BREEDTE:
        #verticaal
        pygame.draw.line(screen, ZWART,((lijn * schaal),0 ),((lijn * schaal),HOOGTE))
        #horizontaal
        pygame.draw.line(screen, ZWART ,(0,(lijn*schaal)),(BREEDTE,(lijn*schaal)) )
        lijn += 1


def tekenspeler():
    pygame.draw.rect(screen, ZWART, (speler_x, speler_y, 10, 10))





while running == True:
    clock.tick(60)
    screen.fill(WIT)
    
    lijnentekenen()
    tekenspeler()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if (event.key in (pygame.K_LEFT, pygame.K_a)) and speler_x != 15:
                speler_x -= schaal
            if (event.key in (pygame.K_RIGHT, pygame.K_d)) and speler_x != (BREEDTE - 25):
                speler_x += schaal
            if (event.key in (pygame.K_UP, pygame.K_w)) and speler_y != 15:
                speler_y -= schaal
            if (event.key in (pygame.K_DOWN, pygame.K_s)) and speler_y != (HOOGTE - 25):
                speler_y += schaal
            if (event.key == pygame.K_q) and (speler_x != 15 and speler_y != 15) :
                speler_x -= schaal
                speler_y -= schaal
            if (event.key == pygame.K_e) and ((speler_x != (BREEDTE - 25)) and speler_y != 15) :
                speler_x += schaal
                speler_y -= schaal
            if (event.key == pygame.K_x) and ((speler_x != (BREEDTE - 25)) and (speler_y != (HOOGTE - 25))) :
                speler_x += schaal
                speler_y += schaal
            if (event.key == pygame.K_z) and ((speler_x != 15) and (speler_y != (HOOGTE - 25))) :
                speler_x -= schaal
                speler_y += schaal
            if (event.key == pygame.K_t) :
                dotplilbro()
            if (event.key == pygame.K_c) :
                speler_x = speler_x
                speler_y = speler_y


    
    pygame.display.update()


pygame.quit()
sys.exit()