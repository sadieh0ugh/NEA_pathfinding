import pygame
import random


ScreenWidth = 1000
ScreenHeight = 625

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

CellSize = 30
CellQuotient = 30
CellsPerSide = ScreenHeight // CellQuotient # 25 x 25 maze, uses DIV to ignore width of lines drawn, range of maze is 25 by 25
# each cell holds letters Left, Up, Right, Down - showing which walls they have
maze = [['lurd' for i in range(CellsPerSide)] for j in range(CellsPerSide)]

current = (0, 0) # start position coordinates

unvisited = [(i, j) for i in range(CellsPerSide) for j in range(CellsPerSide)]
# list of unvisited cells (i, j) being coordinates of top left corner of each cell
# initially all cells in the grid are unvisited except for the starting cell
unvisited.remove(current)

visited = [current] # at the start of execution the only square in the visited list is the starting cell


def DrawMaze(maze, surface, current):

    pygame.draw.rect(surface, white, (current[1] * CellSize, current[0] * CellSize, CellSize, CellSize))  # drawing white player
    # says position of rectangle is top left corner of current cell x 24 (cell width/height) so the rectangle fills the whole cell

    for i, line in enumerate(maze): # gives each line of the maze a count value starting at 0
        for j, element in enumerate(line): # gives each element (cell) of a line a count value
            if 'l' in element:
                pygame.draw.line(surface, purple, (j * CellSize, i * CellSize), (j * CellSize , i * CellSize + CellSize), 4)
            if 'u' in element:
                pygame.draw.line(surface, purple, (j * CellSize, i * CellSize), (j * CellSize + CellSize, i * CellSize), 5)
            if 'r' in element:
                pygame.draw.line(surface, purple, (j * CellSize + CellSize, i * CellSize), (j * CellSize + CellSize, i * CellSize + CellSize), 5)
            if 'd' in element:
                pygame.draw.line(surface, purple, (j * CellSize, i * CellSize + CellSize), (j * CellSize + CellSize, i * CellSize + CellSize), 5)


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
    font50 = pygame.font.Font("VT323-Regular.ttf", 50)
    font20 = pygame.font.Font("VT323-Regular.ttf", 20)



    pygame.mouse.set_pos(CellSize//2,CellSize//2)

    #image = pygame.image.load('blacksqaure.png')
    #creen.blit(image, [0,0])
    screenSurface = pygame.display.get_surface()

    timeIncrements = []
    Timing = False
    TimePassed = 0
    running = True
    while running:
        clock.tick(30)


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

            if e.type == pygame.MOUSEMOTION:

                    mouse = pygame.mouse.get_pos()
                    pxarray = pygame.PixelArray(screenSurface)
                    pixel = pygame.Color(pxarray[mouse[0],mouse[1]])
                    #print(pixel)
                    pxarray.close()   # must close because PixelArray locks the surface making it impossible to blit text into the explanation box
                                      # here it is forced to close each time it has been used, unlocking the screen

                    if pixel == (0, 165, 0, 236):
                        pygame.mouse.set_pos(CellSize//2,CellSize//2)
            #print("mouse press")

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    Timing = True
                    if Timing:
                        InitialCount = pygame.time.get_ticks()

            if e.type == pygame.MOUSEMOTION:
                if pixel == (0, 71, 255, 107):
                    Timing = False
                    print(timeIncrements[-1]/1000)

        if Timing:
            TimePassed = pygame.time.get_ticks() - InitialCount
            timeIncrements.append(TimePassed)

        screen.fill(black)

        timerText = font50.render(str(TimePassed / 1000), True, white)
        screen.blit(timerText, (800, 10))

        pygame.draw.rect(screen, green, (570, 570, CellSize, CellSize))

        DrawMaze(maze, screen, current)


        maze, current, visited, unvisited = NextMove(current, maze, unvisited, visited)
        #pygame.display.flip()
        #print(maze)

        #end_rect = pygame.Rect()
        #pygame.draw.rect(screen, green, end_rect)

        textSurf, textRect = textObj("Press Space to Start the timer", font20, white)
        textRect.center = (820, 70)
        screen.blit(textSurf, textRect)
        pygame.display.flip()
    pygame.quit()
    quit()

#function that renders surface for text to be displayed on
# eliminates box around text being created
def textObj(text, font, col):
    textSurface = font.render(text, True, col)
    return textSurface, textSurface.get_rect()

# lots of details required hence a lot of parameters
# msg - what button says, x,y - position of button, w,h - width, height of button
# ic - inactive colour (normal colour), ac - active (selected) colour
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)    if need to see positions easier for placing
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # if mouse position is found in range inside drawn box
        pygame.draw.rect(screen, ac,(x, y, w, h)) # then redraw box a lighter shade so it appears interactive

        #if click[0] == 1 and action != None:
         #   if action == "play":
          #      LevelSelect()



        if click[0] == 1 and action != None:
            if action == "play":
                GameLoop(maze, screen, current, visited, unvisited)

            #elif action == "tutorial":
                #Tutorial()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))  # whenever mouse isnt over box it remains normal colour

    font50 = pygame.font.Font("VT323-Regular.ttf", 50)
    textSurf, textRect = textObj(msg, font50, white)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))  # centres Start text in button 1
    screen.blit(textSurf, textRect)
    pygame.display.update()

def LevelSelect():
    running = True
    while running:
        clock.tick(15)
        screen.fill(black)

        button("Beginner", 150, 300, 200, 100, purple, selected_purple, "easy")
        button("Intermediate", 600, 300, 200, 100, purple, selected_purple, "hard")
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

def start_screen():

    running = True
    while running:

        clock.tick(15)
        screen.fill(black)

        button("Tutorial", 150, 300, 200, 100, purple, selected_purple,"tutorial")
        button("Start", 600, 300, 200, 100, purple, selected_purple,"play")

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

#start_screen()
GameLoop(maze, screen, current, visited, unvisited)
