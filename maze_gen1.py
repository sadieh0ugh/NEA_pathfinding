
import pygame
import random


ScreenWidth = 950
ScreenHeight = 529


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

current = (0, 0)

unvisited = [(i, j) for i in range(CellsPerSide) for j in range(CellsPerSide)]
unvisited.remove(current)

visited = [current]

def DrawMaze(maze, surface, current):

    pygame.draw.rect(surface, white, (current[1] * 35, current[0] * 35, 35, 35))

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

def NextMove(current, maze, unvisited, visited):

    Neighbours = []

    if current[0] + 1 < len(maze) and (current[0] + 1, current[1]) in unvisited:
        Neighbours.append((current[0] + 1, current[1]))

    if current[1] + 1 < len(maze) and (current[0], current[1] + 1) in unvisited:
        Neighbours.append((current[0], current[1] + 1))

    if current[0] - 1 >= 0 and (current[0] - 1, current[1]) in unvisited:
        Neighbours.append((current[0] - 1, current[1]))

    if current[1] - 1 >= 0 and (current[0], current[1] - 1) in unvisited:
        Neighbours.append((current[0], current[1] - 1))


    if len(Neighbours) > 0:

        Next_Position = random.choice(Neighbours)

        if current[0] == Next_Position[0]:
            if Next_Position[1] > current[1]:
                direction = 'r'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('r', '')
                maze[Next_Position[0]][Next_Position[1]] = maze[Next_Position[0]][Next_Position[1]].replace('l', '')

            else:
                direction = 'l'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('l', '')
                maze[Next_Position[0]][Next_Position[1]] = maze[Next_Position[0]][Next_Position[1]].replace('r', '')

        else:
            if Next_Position[0] > current[0]:
                direction = 'd'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('d', '')
                maze[Next_Position[0]][Next_Position[1]] = maze[Next_Position[0]][Next_Position[1]].replace('u', '')

            else:
                direction = 'u'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('u', '')
                maze[Next_Position[0]][Next_Position[1]] = maze[Next_Position[0]][Next_Position[1]].replace('d', '')

        current = Next_Position

        if current not in visited:
            visited.append(current)

        if current in unvisited:
            unvisited.remove(current)
    else:
        if len(visited) > 1:
            visited = visited[:-1]
            current = visited[-1]

        else:
            current = (0, 0)

    return maze, current, visited, unvisited





running = True
while running:
    clock.tick(90)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    screen.fill(black)

    DrawMaze(maze, screen, current)

    maze, current, visited, unvisited = NextMove(current, maze, unvisited, visited)
    pygame.display.flip()

pygame.quit()
quit()


