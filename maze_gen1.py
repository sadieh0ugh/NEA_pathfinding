import pygame
import random
from ExplanationAndQuiz import *

ScreenWidth = 1100
ScreenHeight = 605

#  Colours

white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 200, 0)
green = (71, 255, 107)
purple = (165, 0, 236)
selected_purple = (218, 128, 255)
textcol = (204, 153, 255)

pygame.init()

screen = pygame.display.set_mode((ScreenWidth,ScreenHeight)) # sets dimensions of the screen (using constants)
pygame.display.set_caption("NEA Code")
clock = pygame.time.Clock()

font50 = pygame.font.Font("VT323-Regular.ttf", 50)
font35 = pygame.font.Font("VT323-Regular.ttf", 35)
font27 = pygame.font.Font("NotoMono-Regular.ttf", 20)
font20 = pygame.font.Font("VT323-Regular.ttf", 20)

def Drawmaze(mazeLURD, surface, current, CellSize):

    pygame.draw.rect(surface, white, (current[1] * CellSize, current[0] * CellSize, CellSize, CellSize))
    # says position of rectangle is top left corner of the current cell x given cell size (cell width/height) so the rectangle fills the whole cell

    for x, line in enumerate(mazeLURD): # gives each line of the mazeLURD a count value starting at 0
        for y, element in enumerate(line): # gives each element (cell) of a line a count value
            # checks through every cell (element) and detects the letters held within the placeholder string in multi-dimensional array

            if 'l' in element:
                # means 'l' is present in the string so the cell still has its left wall so it is drawn
                pygame.draw.line(surface, purple, (y* CellSize, x* CellSize), (y* CellSize , x* CellSize + CellSize), 4)

            if 'u' in element:
                # means 'u' is present in the string so the cell still has its upper wall so it is drawn
                pygame.draw.line(surface, purple, (y* CellSize, x* CellSize), (y* CellSize + CellSize, x* CellSize), 5)

            if 'r' in element:
                # means 'r' is present in the string so the cell still has its right wall so it is drawn
                pygame.draw.line(surface, purple, (y* CellSize + CellSize, x* CellSize), (y* CellSize + CellSize, x* CellSize + CellSize), 5)

            if 'd' in element:
                # means 'd' is present in the string so the cell still has its bottom wall so it is drawn
                pygame.draw.line(surface, purple, (y* CellSize, x* CellSize + CellSize), (y* CellSize + CellSize, x* CellSize + CellSize), 5)

'''Function that finds all the possible movements to neighbours of the current cell being checked.
   One of these neighbours is selected at random then the mazeLURD is manipulated to draw path to new cell'''
def NextMove(current, mazeLURD, unvisited, visited, surface, size):

    # array that holds all the possible movements of the current cell
    Neighbours = []

    '''if the next square from the row (x) is not over the width of the mazeLURD
      and the neighbour cell being checked is contained within the unvisited list
      then the square next along the line from current cell is a possible neighbour'''

    if current[0] + 1 < len(mazeLURD) and (current[0] + 1, current[1]) in unvisited:
        Neighbours.append((current[0] + 1, current[1]))

    '''if the next square from the column (y) is not over the height of the mazeLURD
      and the neighbour cell being checked is contained within the unvisited list
      then the square below the current cell is a possible neighbour'''

    if current[1] + 1 < len(mazeLURD) and (current[0], current[1] + 1) in unvisited:
        Neighbours.append((current[0], current[1] + 1))

    '''if the previous square from the row (x) has the x placement coordinate of 0 or more (the left side of mazeLURD and above)
    # and the neighbour cell being checked is contained within the unvisited list
    # then the square before the current cell is a possible neighbour'''

    if current[0] - 1 >= 0 and (current[0] - 1, current[1]) in unvisited:
        Neighbours.append((current[0] - 1, current[1]))

    '''if the previous square from the column (y) has the y placement coordinate of 0 or more (the top of the mazeLURD of more)
    # and the neighbour cell being checked is contained within the unvisited list
    # then the square above the current cell is a possible neighbour'''

    if current[1] - 1 >= 0 and (current[0], current[1] - 1) in unvisited:
        Neighbours.append((current[0], current[1] - 1))
    
    
    # if there is at least one possible movement 
    if len(Neighbours) > 0:
        
        # choose the next square (x, y) randomly from the list of possible moves
        Next_Position = random.choice(Neighbours)

        if current[0] == Next_Position[0]: # if x coordinate of current cell and the selected nex cell is the same
                                           # this means they are in the same row 
            if Next_Position[1] > current[1]: # if the y coordinate of the selected next cell is greater than the current cell
                direction = 'r'               # it means the next cell chosen is to the right of the current
                mazeLURD[current[0]][current[1]] = mazeLURD[current[0]][current[1]].replace('r', '')
                # for the current cell remove the 'r' from the string so the right wall for this cell isnt drawn
                mazeLURD[Next_Position[0]][Next_Position[1]] = mazeLURD[Next_Position[0]][Next_Position[1]].replace('l', '')
                # when the next cell chose is to the right, remove the 'l' from the string so the left wall for this cell isnt drawn

            else: # not right
                direction = 'l'
                mazeLURD[current[0]][current[1]] = mazeLURD[current[0]][current[1]].replace('l', '')
                # for the current cell remove the 'l' from the string so the left wall for this cell isnt drawn
                mazeLURD[Next_Position[0]][Next_Position[1]] = mazeLURD[Next_Position[0]][Next_Position[1]].replace('r', '')
                # when the next cell chose is to the left, remove the 'r' from the string so the right wall for this cell isnt drawn

        else: # means the x coordinates of the current cell and selected next cell are not the same 
              # therefore their y coordinates must be the same, so they are in the same column 
            if Next_Position[0] > current[0]: # if the x coordinate of the the selected next square is greater than the current cell
                direction = 'd'               # it means the next cell chosen is below the current square
                mazeLURD[current[0]][current[1]] = mazeLURD[current[0]][current[1]].replace('d', '')
                # for the current cell remove the 'd' from the string so the bottom wall for this cell isnt drawn
                mazeLURD[Next_Position[0]][Next_Position[1]] = mazeLURD[Next_Position[0]][Next_Position[1]].replace('u', '')
                # when the next cell chose is below, remove the 'u' from the string so the upper wall for this cell isnt drawn

            else:
                direction = 'u'
                mazeLURD[current[0]][current[1]] = mazeLURD[current[0]][current[1]].replace('u', '')
                # for the current cell remove the 'u' from the string so the upper wall for this cell isnt drawn
                mazeLURD[Next_Position[0]][Next_Position[1]] = mazeLURD[Next_Position[0]][Next_Position[1]].replace('d', '')
                # when the next cell chose is above, remove the 'd' from the string so the bottom wall for this cell isnt drawn

        # set the position of the current cell to the next cell that was selected at random
        current = Next_Position

        if current not in visited:
            visited.append(current)

        if current in unvisited:
            unvisited.remove(current)

    # if list Neighbours contains no items, there are no possible movements
    else:
        if len(visited) > 1: # if visited list holds more than just (0,0)
            visited = visited[:-1]  # remove last element to go back one step as the algorithm has found a dead end
            current = visited[-1]   # now set current cell to be the new last element

        else: # all elements are visited and white square has found its way back to start square
            current = (0, 0)

    return mazeLURD, current, visited, unvisited

def GameLoop(mazeLURD, screen, current, CellSize):

    pygame.mouse.set_pos(CellSize // 2, CellSize // 2)

    InitialCount = pygame.time.get_ticks()
    screenSurface = pygame.display.get_surface()

    finishedTime = 0
    timeIncrements = []
    Timing = False
    TimePassed = 0
    running = True

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
                pixel = pygame.Color(pxarray[mouse[0], mouse[1]])
                # print(pixel)
                pxarray.close()  # must close because PixelArray locks the surface making it impossible to blit text into the explanation box
                # here it is forced to close each time it has been used, unlocking the screen

                if pixel == (0, 165, 0, 236):
                    pygame.mouse.set_pos(CellSize // 2, CellSize // 2)
                # print("mouse press")

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    Timing = True
                    if Timing:
                        InitialCount = pygame.time.get_ticks()

            if e.type == pygame.MOUSEMOTION:
                if pixel == (0, 71, 255, 107):
                    Timing = False
                    finishedTime = timeIncrements[-1] / 1000
                    running = False

                    #textSurf, textRect = textObj("You completed the maze in: " + str(timeIncrements[-1] / 1000) + " seconds", font20, white)
                    #textRect.center = (820, 300)
                    #screen.blit(textSurf, textRect)
                    #pygame.display.flip()



        if Timing:
            TimePassed = pygame.time.get_ticks() - InitialCount
            timeIncrements.append(TimePassed)


        screen.fill(black)
        Drawmaze(mazeLURD, screen, current, CellSize)
        timerText = font50.render(str(TimePassed / 1000), True, white)
        screen.blit(timerText, (800, 10))

        textSurf, textRect = textObj("Press Space to Start", font20, white)
        textRect.center = (820, 70)
        screen.blit(textSurf, textRect)



        pygame.draw.rect(screen, green, (540, 540, CellSize, CellSize))
        textSurf, textRect = textObj("End", font20, black)
        textRect.center = (560, 570)
        screen.blit(textSurf, textRect)

        pygame.display.flip()

    print(finishedTime)
    pygame.quit()
    quit()


def ExplanationAndQuiz():
    CellSize = 45
    CellQuotient = 45
    CellsPerSide = ScreenHeight // CellQuotient  # 25 x 25 mazeLURD, uses DIV to ignore width of lines drawn, range of mazeLURD is 25 by 25
    # each cell holds letters Left, Up, Right, Down - showing which walls they have

    mazeLURD = [['lurd' for x in range(CellsPerSide)] for y in range(CellsPerSide)]

    current = (0, 0)  # start position count

    unvisited = [(x, y) for x in range(CellsPerSide) for y in range(CellsPerSide)]
    # list of unvisited cells (i, j) being position count of each cell
    # initially all cells in the grid are unvisited except for the starting cell

    unvisited.remove(current)

    visited = [current]  # at the start of execution the only square in the visited list is the starting cell

    box2 = pygame.image.load('box2.png')

    countNpress = 0
    running = True
    while running:
        clock.tick(15)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_n:
                Npress = True
                countNpress += 1

        screen.fill(black)

        pygame.draw.rect(screen, green, (540, 540, CellSize, CellSize))

        Drawmaze(mazeLURD, screen, current, CellSize)  # when first called, draws a grid

        mazeLURD, current, visited, unvisited = NextMove(current, mazeLURD, unvisited, visited, surface=screen, size=CellSize)


        if countNpress == 0:
            blitMultiLines(screen, textIntroduction, (605, 10), font27)

            pygame.display.flip()


        if countNpress >= 1:
            blitMultiLines(screen, textAlgorithm1, (605, 10), font27)
            screen.blit(box2, (605, 100))
            pygame.display.flip()

        if countNpress >= 2:
            blitMultiLines(screen, textAlgorithm2, (730, 80), font27)
            pygame.display.flip()


        if countNpress == 10:
            GameLoop(mazeLURD, screen, current, CellSize)

        pygame.display.flip()
    start_screen()
    return mazeLURD, screen, current, CellSize

def blitMultiLines(surface, text, pos, font, colour=selected_purple):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    maxWidth, maxHeight = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            wordSurf = font.render(word, 0, colour)
            wordWidth, wordHeight = wordSurf.get_size()
            if x + wordWidth >= maxWidth:
                x = pos[0]
                y += wordHeight
            surface.blit(wordSurf, (x, y))
            x += wordWidth + space
        x = pos[0]
        y += wordHeight


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
    click1 = pygame.mouse.get_pressed()
    click2 = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # if mouse position is found in range inside drawn box
        pygame.draw.rect(screen, ac,(x, y, w, h)) # then redraw box a lighter shade so it appears interactive

        if click1[0] == 1 and action != None:
            if action == "play":
                ExplanationAndQuiz()

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
ExplanationAndQuiz()
