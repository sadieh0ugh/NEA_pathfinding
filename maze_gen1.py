import time
import pygame
import random


ScreenWidth = 950
ScreenHeight = 604

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


CellsPerSide = 500 // 21 # 25 x 25 maze, uses DIV to ignore width of lines drawn, range of maze is 25 by 25
# each cell holds letters Left, Up, Right, Down - showing which walls they have
maze = [['lurd' for i in range(CellsPerSide)] for j in range(CellsPerSide)]

current = (0, 0) # start position coordinates

unvisited = [(i, j) for i in range(CellsPerSide) for j in range(CellsPerSide)]
# list of unvisited cells (i, j) being coordinates of top left corner of each cell
# initially all cells in the grid are unvisited except for the starting cell
unvisited.remove(current)

visited = [current] # at the start of execution the only square in the visited list is the starting cell


def DrawMaze(maze, surface, current):

    global ls1
    global le1


    pygame.draw.rect(surface, white, (current[1] * 25, current[0] * 25, 25, 25))  # drawing white player
    # says position of rectangle is top left corner of current cell x 24 (cell width/height) so the rectangle fills the whole cell

    for i, line in enumerate(maze): # gives each line of the maze a count value starting at 0
        for j, element in enumerate(line): # gives each element (cell) of a line a count value
            if 'l' in element:
                ls1 = j * 25
                ls2 = i * 25
                le1 = j * 25
                le2 = i * 25 + 25

                pygame.draw.line(surface, purple, (ls1, ls2), (le1, le2), 4)
            if 'u' in element:
                pygame.draw.line(surface, purple, (j * 25, i * 25), (j * 25 + 25, i * 25), 4)
            if 'r' in element:
                pygame.draw.line(surface, purple, (j * 25 + 25, i * 25), (j * 25 + 25, i * 25 + 25), 4)
            if 'd' in element:
                pygame.draw.line(surface, purple, (j * 25, i * 25 + 25), (j * 25 + 25, i * 25 + 25), 4)





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








def GameLoop(maze,screen,current,visited,unvisited):

    running = True
    pygame.mouse.set_pos(10,10)

    #image = pygame.image.load('blacksqaure.png')
    #creen.blit(image, [0,0])

    screenSurface = pygame.display.get_surface()
    while running:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

            if e.type == pygame.MOUSEMOTION:

                    mouse = pygame.mouse.get_pos()
                    pxarray = pygame.PixelArray(screenSurface)
                    pixel = pygame.Color(pxarray[mouse[0],mouse[1]])
                    print(pixel)

                    if pixel == (0, 165, 0, 236):
                        pygame.mouse.set_pos(10,10)



            #print("mouse press")





        screen.fill(black)


        DrawMaze(maze, screen, current)


        maze, current, visited, unvisited = NextMove(current, maze, unvisited, visited)
        #pygame.display.flip()
        #print(maze)


        pygame.display.update()
    pygame.quit()
    quit()
    #textmaze = []
    #Text(maze, textmaze)
    #print(textmaze)
    #print(maze)


GameLoop(maze, screen, current, visited, unvisited)


