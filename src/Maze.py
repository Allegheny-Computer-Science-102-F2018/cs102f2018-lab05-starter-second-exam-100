from pygame.locals import *
import pygame

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

class Maze(pygame.sprite.Sprite):
    def __init__(self):
       self.M = 10
       self.N = 8
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,1,
                     1,0,1,0,0,0,0,0,0,1,
                     1,0,1,1,1,1,1,1,0,1,
                     1,0,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,]

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

    #pygame.init()
    #all_sprite_list = pygame.sprite.Group()
    #all_sprite_list.add(Player)
    #all_sprite_list.add(Maze)

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self._bg_surf = None

        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pikachu Must Go')
        self._running = True
        self._image_surf = pygame.image.load("player.png").convert()
        self._block_surf = pygame.image.load("block.png").convert()
        img = pygame.image.load('bg.png')

        a = pygame.image.load('icon.png')
        pygame.display.set_icon(a)

    def on_event(self, event):

        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf)
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


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
    all_sprite_list.update()
    pygame.quit()
