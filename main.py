import pygame
from pygame.locals import *

#Initialize pygame
pygame.init()

#Set window size
win = pygame.display.set_mode((550,550))

#Set window caption
pygame.display.set_caption("Tic Tac Toe")

rectangle1 = pygame.draw.rect(win,(255,255,255), (25,25,150,150))
rectangle2 = pygame.draw.rect(win,(255,255,255), (200,25,150,150))
rectangle3 = pygame.draw.rect(win,(255,255,255), (375,25,150,150))

rectangle4 = pygame.draw.rect(win,(255,255,255), (25,200,150,150))
rectangle5 = pygame.draw.rect(win,(255,255,255), (200,200,150,150))
rectangle6 = pygame.draw.rect(win,(255,255,255), (375,200,150,150))

rectangle7 = pygame.draw.rect(win,(255,255,255), (25,375,150,150))
rectangle8 = pygame.draw.rect(win,(255,255,255), (200,375,150,150))
rectangle9 = pygame.draw.rect(win,(255,255,255), (375,375,150,150))
            


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()