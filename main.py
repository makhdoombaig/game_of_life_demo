import pygame
import numpy as np
import base

width= 1000
height=720
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 15
offset = 1

Grid = base.Grid(width,height, scaler, offset)
Grid.random()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    Grid.Rules(off_color=white, on_color=blue1, surface=screen, pause=pause)
    pygame.display.update()

pygame.quit()
