#23/12/2021
#Player code
#Coded by:
#Bandar - bandi72006

#===================== PLAYER CODE =====================

import pygame


class Player:
    def __init__(self):
        self.x = 75 
        self.y = 300
        
        self.isPressed = False

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            if self.isPressed == False:
                self.x += 20
                self.isPressed = True
        else:
            self.isPressed = False
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x,self.y,30,30))
