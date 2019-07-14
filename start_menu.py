import pygame
from CONST import *

screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('START SCREEN')
clock = pygame.time.Clock()
pygame.init()

# function that renders surface for text to be displayed on
# eliminates box around text being created
def textObj(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# lots of details required hence a lot of parameters
# msg - what button says, x,y - position of button, w,h - width, height of button
# ic - inactive colour (normal colour), ac - active (selected) colour
def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    #print(mouse)    if need to see positions easier for placing

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # if mouse position is found in range inside drawn box
        pygame.draw.rect(screen, ac,(x, y, w, h))  # then redraw box a lighter shade so it appears interactive
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))  # whenever mouse isnt over box it remains normal colour

    mainFont = pygame.font.Font("VT323-Regular.ttf", 50)
    textSurf, textRect = textObj(msg, mainFont)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))  # centres Start text in button 1
    screen.blit(textSurf, textRect)
    pygame.display.update()


def start_screen():

    running = True
    while running:

        clock.tick(15)
        screen.fill(black)

        button("Tutorial", 150, 300, 200, 100, purple, selected_purple)
        button("Start", 600, 300, 200, 100, purple, selected_purple)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

start_screen()