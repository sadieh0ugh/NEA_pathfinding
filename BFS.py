import queue
import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 200, 0)
green = (71, 255, 107)
purple = (165, 0, 236)
selected_purple = (218, 128, 255)

class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

        #print(pos[0],pos[1])

class PathRect(object):

    def __init__(self, pos):

        pathrects.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
       # print(pos[0],pos[1])




screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption('BFS')
clock = pygame.time.Clock()
walls = []
pathrects = []
def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze


def createMaze2():
    global end_rect
    global start_rect
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    x = y = 0
    for row in maze:
        for col in row:
            if col == "#":
                Wall((x,y))
            if col == "X":
                end_rect = pygame.Rect(x, y, 16, 16)
            if col == "O":
                start_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 0


    return maze


def printMaze(maze, path=""):
    global path_rect
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x


    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))


    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:

                cross = "+ "
                print(cross, end="")

                PathRect((i*16,j*16))

            else:
                print(col + " ", end="")
        print()







def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True



def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
    #PathRect((i,j))

    if maze[j][i] == "X":

        print("Found: " + moves)
        printMaze(maze, moves)

        return True



    return False
    return i


# MAIN ALGORITHM



nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze2()

while not findEnd(maze, add):
    add = nums.get() # gets first value in queue
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):  # path generate is valid
            nums.put(put)
            # add to queue


running = True
while running:
    clock.tick(90)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    screen.fill(black)
    for wall in walls:
        pygame.draw.rect(screen, purple, wall.rect)


    for rect in pathrects:
        pygame.draw.rect(screen, selected_purple, rect.rect)

    pygame.draw.rect(screen, green, end_rect)

    pygame.draw.rect(screen, white, start_rect)


    pygame.display.update()





