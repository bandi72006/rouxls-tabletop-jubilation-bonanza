#23/12/2021
#Main code
#Coded by:
#Bandar - bandi72006

#===================== MAIN CODE =====================

import pygame  
import time

from player import *
  
pygame.init()  
screen = pygame.display.set_mode((1280,720))  
run = True  

player = Player()

#Frames manager
frames = 0
FPS = 60
clock = pygame.time.Clock()
startTime = time.time()
  
while run:  

    #Movement code=
    player.move()

    #Drawing code
    screen.fill((0,0,0))

    pygame.draw.line(screen, (255,255,255), (125,0), (125,720), 5)
    pygame.draw.line(screen, (255,0,0), (1155,0), (1155,720), 5)

    player.draw(screen)

    if player.x > 1155:
        print(round(time.time()-startTime, 2))     

    pygame.display.flip()  #Refreshes screen

    clock.tick(60)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False

