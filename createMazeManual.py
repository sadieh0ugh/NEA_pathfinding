import pygame
from CONST import *

pygame.init()

screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption('Maze Manual')
clock = pygame.time.Clock()
done = False

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(16, 16, 13, 13)

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
    "WWWWWWWWWWWWWWWWWEWWWWWWWWWWWWWWWWWWW"
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

    screen.fill(white)
    for wall in walls:
        pygame.draw.rect(screen, black, wall.rect)

    pygame.draw.rect(screen, orange, player.rect)
    pygame.draw.rect(screen, green, end_rect)
    pygame.display.flip()
    pygame.display.update()

