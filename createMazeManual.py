import pygame
import time
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

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)

    def move(self, dx , dy):

        if dx != 0:
            self.move_single_axis(dx, 0)

        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left

                if dx < 0:
                    self.rect.left = wall.rect.right

                if dy > 0:
                    self.rect.bottom = wall.rect.top

                if dy < 0:
                    self.rect.top = wall.rect.bottom

class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption('Maze Manual')
clock = pygame.time.Clock()


walls = []

player = Player()

level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W W   W   W          W       W      W",
    "W   W W W   WWWWWW W W WWWWW W WW W W",
    "WWWWW W WWWWW      W W W     W  WWW W",
    "W     W W     W    W W W W  WWW   W W",
    "W WWWWW W WWWWW WWWW WWW WWWW WWW W W",
    "W     W W W      W W W          W W W",
    "WWW WWW   W W  W W W W WWW WWWWWW W W",
    "W       WWW WWWW W W W   W W      W W",
    "W WWW WWW WWW    W W WWW W   WWWW W W",
    "W  W  W     W WWWW W     W W W W  W W",
    "WW W WW W W      W WWW W W W W WWWWWW",
    "W  W    W WWWWWWWW     W WWW W      W",
    "WWWWWWWWW W      WWWWWWW W W WWWWWW W",
    "W      W  W WWWW   W W     W W    W W",
    "W WWW WWWWW W      W W WWW W W WWWW W",
    "W   W W     W WWWW W W W     W W    W",
    "WWW W WWW WW   W W W   WWWWWWW WW W W",
    "W W W   W W  WWW   WWW W        W W W",
    "W W WWW WWW WW WW WW   WWW WWWW W W W",
    "W   W W   W W        W W W      WWW W",
    "W WWW WWW W W WWWWW WW W W WWWW     W",
    "W       W   W     W    W W W  WWWW WW",
    "W W W W WW WWW  W WWWWWW   W   W    W",
    "W WWW W  W W WWWW        W W WWW WWWW",
    "W W      W   W    WWW WWWW W W W  W W",
    "W W WW WWWWWWWWWWWW W W  W W W WW W W",
    "W W  W W   W   W    W W WW      W W W",
    "W WW WWW W W W WWW WW W W  WWWW W W W",
    "W  W     W   W   W W  W WW W  W W   W",
    "W WW WWWWWWWWWWW W WWWW  WWW  W WWWWW",
    "W  W W     W     W            W     W",
    "WWWW   WWWWW WWWWWWWWWW W  WW WWWW WW",
    "W    W W  W        W    WWWW  W     W",
    "W WWWW WW W WWWWWW W WWWW  WWWWWWWWWW",
    "W    W    W        W                W",
    "WWWWWWWWWWWWWWWWWWEWWWWWWWWWWWWWWWWWW"
]

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0


# function that renders surface for text to be displayed on
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

        if click[0] == 1 and action != None:
            if action == "play":
                GameLoop()
            #elif action == "tutorial":
                #Tutorial()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))  # whenever mouse isnt over box it remains normal colour

    mainFont = pygame.font.Font("VT323-Regular.ttf", 50)
    textSurf, textRect = textObj(msg, mainFont, white)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))  # centres Start text in button 1
    screen.blit(textSurf, textRect)
    pygame.display.update()


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

def Win():
    smallFont = pygame.font.Font("VT323-Regular.ttf", 35)
    clock.tick(90)
    textSurf, textRect = textObj("You Win!", smallFont, white)
    textRect.center = (769, 100)
    screen.blit(textSurf, textRect)
    pygame.display.update()

def GameLoop():
    mainFont = pygame.font.Font("VT323-Regular.ttf", 50)
    smallFont = pygame.font.Font("VT323-Regular.ttf", 35)

    running = True
    while running:
        clock.tick(90)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)

        if player.rect.colliderect(end_rect):
            Win()


        screen.fill(black)
        for wall in walls:
            pygame.draw.rect(screen, purple, wall.rect)



        #textRect.center = (770, 25)

        pygame.draw.rect(screen, white, player.rect)
        pygame.draw.rect(screen, green, end_rect)

        # pygame.display.flip()


        textSurf, textRect = textObj("Explanation Box:", mainFont, purple)
        textRect.center = (770, 25)  # centres Start text in button 1
        screen.blit(textSurf, textRect)

        textSurf, textRect = textObj("Get to the Green Square", smallFont, white)
        textRect.center = (769, 70)
        screen.blit(textSurf, textRect)
        pygame.display.update()




start_screen()