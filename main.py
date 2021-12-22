import pygame
from pygame.locals import *

#Initialize pygame
pygame.init()

#Set window size
win = pygame.display.set_mode((550,550))

#Set window caption
pygame.display.set_caption("Tic Tac Toe")

rectangle1 = pygame.draw.rect(win,(255,255,255), (25,25,150,150))
pos1_free = True
rectangle2 = pygame.draw.rect(win,(255,255,255), (200,25,150,150))
pos2_free = True
rectangle3 = pygame.draw.rect(win,(255,255,255), (375,25,150,150))
pos3_free = True
rectangle4 = pygame.draw.rect(win,(255,255,255), (25,200,150,150))
pos4_free = True
rectangle5 = pygame.draw.rect(win,(255,255,255), (200,200,150,150))
pos5_free = True
rectangle6 = pygame.draw.rect(win,(255,255,255), (375,200,150,150))
pos6_free = True
rectangle7 = pygame.draw.rect(win,(255,255,255), (25,375,150,150))
pos7_free = True
rectangle8 = pygame.draw.rect(win,(255,255,255), (200,375,150,150))
pos8_free = True
rectangle9 = pygame.draw.rect(win,(255,255,255), (375,375,150,150))
pos9_free = True
            
player1 = True

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
                print(event.key == pygame.K_SPACE)
                if event.key == pygame.K_SPACE:
                    rectangle1 = pygame.draw.rect(win,(255,255,255), (25,25,150,150))
                    pos1_free = True
                    rectangle2 = pygame.draw.rect(win,(255,255,255), (200,25,150,150))
                    pos2_free = True
                    rectangle3 = pygame.draw.rect(win,(255,255,255), (375,25,150,150))
                    pos3_free = True
                    rectangle4 = pygame.draw.rect(win,(255,255,255), (25,200,150,150))
                    pos4_free = True
                    rectangle5 = pygame.draw.rect(win,(255,255,255), (200,200,150,150))
                    pos5_free = True
                    rectangle6 = pygame.draw.rect(win,(255,255,255), (375,200,150,150))
                    pos6_free = True
                    rectangle7 = pygame.draw.rect(win,(255,255,255), (25,375,150,150))
                    pos7_free = True
                    rectangle8 = pygame.draw.rect(win,(255,255,255), (200,375,150,150))
                    pos8_free = True
                    rectangle9 = pygame.draw.rect(win,(255,255,255), (375,375,150,150))
                    pos9_free = True
                
                    player1 = True
        if event.type == pygame.MOUSEBUTTONUP:
            #Get curr mouse position 
            pos = pygame.mouse.get_pos()

            if rectangle1.collidepoint(pos) and pos1_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(50,50,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(100,100),50)
                pos1_free = False
                player1 = not(player1)  
            if rectangle2.collidepoint(pos) and pos2_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(225,50,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(275,100),50)
                pos2_free = False
                player1 = not(player1)
            if rectangle3.collidepoint(pos) and pos3_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(400,50,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(450,100),50)
                pos3_free = False
                player1 = not(player1)
            if rectangle4.collidepoint(pos) and pos4_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(50,225,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(100,275),50)
                pos4_free = False
                player1 = not(player1)
            if rectangle5.collidepoint(pos) and pos5_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(225,225,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(275,275),50)
                pos5_free = False
                player1 = not(player1)
            if rectangle6.collidepoint(pos) and pos6_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(400,225,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(450,275),50)
                pos6_free = False
                player1 = not(player1)
            if rectangle7.collidepoint(pos) and pos7_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(50,400,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(100,450),50)
                pos7_free = False
                player1 = not(player1)
            if rectangle8.collidepoint(pos) and pos8_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(225,400,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(275,450),50)
                pos8_free = False
                player1 = not(player1)
            if rectangle9.collidepoint(pos) and pos9_free:
                if player1:
                    pygame.draw.rect(win,(255,0,0),(400,400,100,100))
                else:
                    pygame.draw.circle(win,(0,255,0),(450,450),50)
                pos9_free = False
                player1 = not(player1)
    pygame.display.update()

pygame.quit()