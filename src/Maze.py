import contextlib
with contextlib.redirect_stdout(None):
    from pygame.locals import *
    import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.image.load("block.png").convert()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("player.png").convert()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self, blocks):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Maze(object):
    block_list = None
    enemy_sprites = None

    def __init__(self):
        self.block_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Maze1(Maze):
    """This creates all the blocks in maze 1"""
    def __init__(self):
        super().__init__()
        blocks = [[0, 0],
                 [0, 44],
                 [0, 88],
                 [0, 44*3],
                 [0, 44*4],
                 [0, 44*5],
                 [44, 0]
                ]
        for item in blocks:
            block = Block(item[0], item[1])
            self.block_list.add(block)


class Maze2(Maze):
    def __init__(self):
        super().__init__()

        blocks = []

        for item in blocks:
            block = Block(item[0], item[1])
            self.block_list.add(block)


class Maze3(Maze):
    def __init__(self):
        super().__init__()

        blocks = []

        for item in blocks:
            block = Block(item[0], item[1])
            self.block_list.add(block)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                block = Block(x, y)
                self.block_list.add(block)

        for x in range(150, 700, 100):
            block = Block(x, 200)
            self.block_list.add(block)


def intro():
    print("Welcome to the Python game: Pikachu Must Go!")
    time.sleep(2)
    print("Pikachu is lost in a maze")
    time.sleep(2)
    print("As a kind Allegheny student, you can help him to get home!")
    time.sleep(3)
    print("It would be great if he can get home as soon as possible :)")
    time.sleep(2)


def pikachu_is_lost():
    print("Where is your Gator Pride???")
    time.sleep(2)
    print("Pikachu is now lost in this maze forever...")
    quit()


def main():
    pygame.init()

    screen = pygame.display.set_mode([880, 880])

    pygame.display.set_caption('Maze Runner')

    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    mazes = []

    maze = Maze1()
    mazes.append(maze)

    maze = Maze2()
    mazes.append(maze)

    maze = Maze3()
    mazes.append(maze)

    current_maze_no = 0
    current_maze = mazes[current_maze_no]

    clock = pygame.time.Clock()

    done = False

    start_time = time.time()

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        player.move(current_maze.block_list)

        if player.rect.x < -15:
            if current_maze_no == 0:
                current_maze_no = 2
                current_maze = mazes[current_maze_no]
                player.rect.x = 790
            elif current_maze_no == 2:
                current_maze_no = 1
                current_maze = mazes[current_maze_no]
                player.rect.x = 790
            else:
                current_maze_no = 0
                current_maze = mazes[current_maze_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_maze_no == 0:
                current_maze_no = 1
                current_maze = mazes[current_maze_no]
                player.rect.x = 0
            elif current_maze_no == 1:
                current_maze_no = 2
                current_maze = mazes[current_maze_no]
                player.rect.x = 0
            else:
                current_maze_no = 0
                current_maze = mazes[current_maze_no]
                player.rect.x = 0

        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_maze.block_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    elapsed_time = time.time() - start_time
    time.sleep(2)
    print("It took you ", elapsed_time, " seconds to reach the end of Maze")


# def end_message():

if __name__ == "__main__":
    intro()
    inp = input ("Are you ready for this? (Type 'y' for ready) ")
    if inp != "y":
        pikachu_is_lost()
    else:
        main()
        #end_message()
