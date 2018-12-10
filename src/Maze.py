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
        blocks = [[44, 0]]
        for i in range(40):
            for item in blocks:
                block = Block(item[0]*i, item[1])
                self.block_list.add(block)
        blocks = [[0, 44]]
        for i in range(2,20):
            for item in blocks:
                block = Block(item[0], item[1]*i)
                self.block_list.add(block)
        blocks = [[44, 836]]
        for i in range(40):
            for item in blocks:
                block = Block(item[0]*i,item[1])
                self.block_list.add(block)
        blocks = [[1716, 44]]
        for i in range(18):
            for item in blocks:
                block = Block(item[0],item[1]*i)
                self.block_list.add(block)
        for n in range(8):
            blocks = [[836, 44*n]]
            for i in range(20):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        for n in range(6):
            blocks = [[44, 88+44*n]]
            for i in range(18):
                for item in blocks:
                    block = Block(item[0]*i,item[1])
                    self.block_list.add(block)
        for n in range(9):
            blocks = [[88, 396+44*n]]
            for i in range(36):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)


class Maze2(Maze): #right maze
    def __init__(self):
        super().__init__()
        blocks = [[44, 0]]
        for i in range(40):
            for item in blocks:
                block = Block(item[0]*i, item[1])
                self.block_list.add(block)
        blocks = [[0, 44]]
        for i in range(1,18):
            for item in blocks:
                block = Block(item[0], item[1]*i)
                self.block_list.add(block)
        blocks = [[44, 836]]
        for i in range(40):
            for item in blocks:
                block = Block(item[0]*i,item[1])
                self.block_list.add(block)
        blocks = [[1716, 88]]
        for i in range(17):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(16):
            blocks = [[88, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        blocks = [[484, 44]]
        for i in range(17):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(6):
            blocks = [[572, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        blocks = [[572, 88]]
        for i in range(16):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(6):
            blocks = [[572, 528+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        for n in range(2):
            blocks = [[660, 396+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        blocks = [[968, 44]]
        for i in range(17):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(16):
            blocks = [[1056, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        for n in range(17):
            blocks = [[1408, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)

class Maze3(Maze): #left maze
    def __init__(self):
        super().__init__()
        blocks = [[44, 0]]
        for i in range(40):
            for item in blocks:
                block = Block(item[0]*i, item[1])
                self.block_list.add(block)
        blocks = [[0, 44]]
        for i in range(2,19):
            for item in blocks:
                block = Block(item[0], item[1]*i)
                self.block_list.add(block)
        blocks = [[44, 836]]
        for i in range(40):
            for item in blocks:
                block = Block(item[0]*i,item[1])
                self.block_list.add(block)
        blocks = [[1716, 88]]
        for i in range(17):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(16):
            blocks = [[88, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        blocks = [[484, 44]]
        for i in range(17):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(6):
            blocks = [[572, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        blocks = [[572, 88]]
        for i in range(16):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(6):
            blocks = [[572, 528+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        for n in range(2):
            blocks = [[660, 396+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        blocks = [[968, 44]]
        for i in range(17):
            for item in blocks:
                block = Block(item[0],item[1]+44*i)
                self.block_list.add(block)
        for n in range(16):
            blocks = [[1056, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
                    self.block_list.add(block)
        for n in range(17):
            blocks = [[1408, 88+44*n]]
            for i in range(8):
                for item in blocks:
                    block = Block(item[0]+44*i,item[1])
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
    pygame.mixer.init()
    pygame.mixer.music.load("PMGmusic.mp3")
    pygame.mixer.music.play(-1,0.0)
    screen = pygame.display.set_mode([1760, 880])

    pygame.display.set_caption('Pikachu Must Go!')
    icon = pygame.image.load('icon.png')    #Loads icon for taskbar and window
    pygame.display.set_icon(icon)
    background = pygame.image.load('icon.png')
    background = pygame.transform.scale(background, (500, 720))
    rect = background.get_rect()
    rect = rect.move((0,0))
    screen.blit(background, rect)
    player = Player(40, 40)
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

        if player.rect.x < 0:
            if current_maze_no == 0:
                current_maze_no = 2
                current_maze = mazes[current_maze_no]
                player.rect.x = 1736
            elif current_maze_no == 2:
                current_maze_no = 1
                current_maze = mazes[current_maze_no]
                player.rect.x = 1736
            else:
                current_maze_no = 0
                current_maze = mazes[current_maze_no]
                player.rect.x = 1736

        if player.rect.x > 1760:
            if current_maze_no == 0:
                current_maze_no = 1
                current_maze = mazes[current_maze_no]
                player.rect.x = 0
            elif current_maze_no == 1:
                current_maze_no = 2
                current_maze = mazes[current_maze_no]
                player.rect.x = 0
            else:
                break


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
