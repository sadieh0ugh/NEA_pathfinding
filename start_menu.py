import pygame
from CONST import *

'''
def TextObj(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
'''
pygame.init()

screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption('START SCREEN')
clock = pygame.time.Clock()

running = True
while running:

    clock.tick(15)
    screen.fill(black)
    #pygame.draw.rect(screen, purple, (150, 300, 200, 100))
    pygame.draw.rect(screen, purple, (600, 300, 200, 100))
    pygame.display.update()

    mouse = pygame.mouse.get_pos()
   # print(mouse)
    if 150 + 200 > mouse[0] > 150 and 300 + 100 > mouse[1] > 300:
        pygame.draw.rect(screen, selected_purple, (150, 300, 200, 100))
    else:
        pygame.draw.rect(screen, purple, (150, 300, 200, 100))

    if 600 + 200 > mouse[0] > 600 and 300 + 100 > mouse[1] > 300:
        pygame.draw.rect(screen, selected_purple, (600, 300, 200, 100))
    else:
        pygame.draw.rect(screen, purple, (600, 300, 200, 100))

    fontMain = pygame.font.Font('VT323-Regular.ttf', 50)

    text = fontMain.render("Start", True, white, purple)

    textRect = text.get_rect()
    textRect.center = ((150+(200/2)), (300+(100/2)))

    screen.blit(text, textRect)

    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False


