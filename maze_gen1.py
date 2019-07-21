
# https://www.youtube.com/watch?v=_S7VqeaTBGQ

import pygame
#from CONST import *

ScreenWidth = 950
ScreenHeight = 592


#  COLOURS

white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 200, 0)
green = (71, 255, 107)
purple = (165, 0, 236)
selected_purple = (218, 128, 255)

pygame.init()
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight)) # sets dimensions of the screen (using constants)
pygame.display.set_caption("NEA Code")
clock = pygame.time.Clock()



CellsPerSide = 525 // 35
maze = [['lurd' for i in range(CellsPerSide)] for j in range(CellsPerSide)]

CurrentCell = (0, 0)

UnvisitedCells = [(i, j) for i in range(CellsPerSide) for j in range(CellsPerSide)]
UnvisitedCells.remove(CurrentCell)

visited = [CurrentCell]

def DrawMaze(maze, surface):
    for i, line in enumerate(maze):
        for j, element in enumerate(line):

            if 'l' in element:
                pygame.draw.line(surface, purple, (j * 35, i * 35), (j * 35, i * 35 + 35), 4)
            if 'u' in element:
                pygame.draw.line(surface, purple, (j * 35, i * 35), (j * 35 + 35, i * 35), 4)

            if 'r' in element:
                pygame.draw.line(surface, purple, (j * 35 + 35, i * 35), (j * 35 + 35, i * 35 + 35), 4)

            if 'd' in element:
                pygame.draw.line(surface, purple, (j * 35, i * 35 + 35), (j * 35 + 35, i * 35 + 35), 4)


running = True
while running:
    clock.tick(90)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    screen.fill(black)

    DrawMaze(maze, screen)

    pygame.display.flip()

pygame.quit()
quit()


'''

import pygame
from CONST import *

widthCell = 35
heightCell = 35

betweenCells = 5

grid = []
'''
