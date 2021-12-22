import pygame
from pygame.locals import *

#Initialize pygame
pygame.init()

#Set window size
win = pygame.display.set_mode((500,500))

#Set window caption
pygame.display.set_caption("Tic Tac Toe")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()