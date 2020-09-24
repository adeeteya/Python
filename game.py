import pygame,sys,os
from pygame.locals import *#imports all the constans like colour
red=[0,0,255]#red,green,blue
pygame.init()
DISPLAYSURF=pygame.display.set_mode((400,300))
pygame.display.set_caption('First Pygame Program')
screen=pygame.display.get_surface()
screen.fill(red)
pygame.display.flip()
while True:
    #main loop of the game
    for event in pygame.event.get():
        print(event)
        if(event.type==QUIT):
            pygame.quit()
            sys.exit()
        pygame.display.update()
