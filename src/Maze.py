import contextlib
with contextlib.redirect_stdout(None):
    from pygame.locals import *
    import pygame
import time

class Player(pygame.sprite.Sprite):
    x = 44
    y = 44
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def update(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.Maze, False)

        for block in block_hit_list:
        		if self.change_x > 0:
        			self.rect.right = block.rect.left
        		else:
        			self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.Maze, False)

        for block in block_hit_list:
            		if self.change_y > 0:
            			self.rect.bottom = block.rect.top
            		else:
            			self.rect.top = block.rect.bottom


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(image)

    def can_move(self, delta_pos, wall_map, count=1):
        old_pos = self.rect.center
        self.rect.centerx = self.rect.centerx + delta_pos[0]
        self.rect.centery = self.rect.centery + delta_pos[0]
        result = bool(pygame.sprite.collide_mask(self, wall_map))
        if count:
            result &= not self.can_move(delta_pos, wall_map, count - 1)
        self.rect.center = old_pos
        return not result


class Maze(pygame.sprite.Sprite):
    def __init__(self):
       self.M = 15
       self.N = 15
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,
                     1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,
                     1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,
                     1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,
                     1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,
                     1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 44 , by * 44))

           bx = bx + 1
           if bx > self.M-1:
               bx = 0
               by = by + 1

class App:
    width, height = 800, 600
    hbox, vbox = 20, 20
    #screen = pg.display.set_mode((width, height))

    windowWidth = 1000
    windowHeight = 800
    player = 0

    pygame.init()

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self._bg_surf = None
        self.character = None
        self.bg = None

        self.player = Player()
        self.maze = Maze()


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pikachu Must Go')
        self._running = True
        self.character = pygame.image.load("player.png").convert()
        self.bg = pygame.image.load("block.png").convert()
        img = pygame.image.load('bg.png')
        #a = pygame.image.load('icon.png')
        #pygame.display.set_icon(a)
        self._image_surf = GameObject(self.character)

        self._block_surf = GameObject(self.bg)

    def on_event(self, event):

        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf.image,(self.player.x,self.player.y), self._image_surf.rect)
        self.maze.draw(self._display_surf, self._block_surf.image)
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()


            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


def intro():
    print("Welcome to the Python game: Pikachu Must Go!")
    time.sleep(3)
    print("Pikachu is lost in a maze")
    time.sleep(3)
    print("As a kind Allegheny student, you can help him to get home!")
    time.sleep(5)
    print("It would be great if he can get home as soon as possible :)")
    time.sleep(3)


def pikachu_is_lost():
    print("Where is your Gator Pride???")
    time.sleep(3)
    print("Pikachu is now lost in this maze forever...")
    quit()


def main():
    start_time = time.time()
    theApp = App()
    #all_sprite_list.update()
    theApp.on_execute()
    pygame.quit()
    elapsed_time = time.time() - start_time
    time.sleep(2)
    print("It took you ", elapsed_time, " seconds to reach the end of Maze")


# def end_message():

if __name__ == "__main__" :
    intro()
    inp = input ("Are you ready for this? (Type 'y' for ready) ")
    if inp != "y":
        pikachu_is_lost()
    else:
        main()
        #end_message()
