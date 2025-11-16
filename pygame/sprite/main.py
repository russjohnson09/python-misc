import pygame
import time
import os
import spritesheet

from typing import Any, Generator, List, Optional, Callable, Tuple
Event = Generator[None, None, None]
Callback = Callable[[], Any]
Colour = Tuple[int, int, int]

FPS = os.environ.get('FPS', 60)

RED = (255, 0, 0)  # RGB values for red
WHITE = (255, 255, 255) # RGB values for white background
BLACK = (0, 0, 0) # RGB values for white background
FILL = (5, 5, 5) # RGB values for white background

FILL = (100, 100, 100) # RGB values for white background




def _init():

    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("Red Square Example")

#  640x480 psone
def get_screen(screen_width = 640, screen_height = 480) -> pygame.surface.Surface:
    # screen_width = 800
    # screen_height = 600
    # screen = pygame.display.set_mode((screen_width, screen_height))
    # screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.SCALED)

    return screen



class GalagaSprites(pygame.sprite.Sprite):

    # 
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


# https://www.pygame.org/wiki/Spritesheet
# https://stackoverflow.com/questions/40774276/python-display-sprites
class Player(pygame.sprite.Sprite):
    # https://www.pygame.org/docs/ref/sprite.html
    image_path = "galaga_sprites.png"
    def __init__(self, x, y):
        # I should pull in some singleton class for sprite management here.


        super().__init__()
        self.tick = 0
        self.frame = 0
        ss = spritesheet.spritesheet('galaga_sprites.png')
        # image = ss.image_at((0, 0, 16, 16)) # TODO multiple images for player animation
        # colorkey = (255, 255, 255)
        # images = ss.images_at((0, 0, 16, 16),(17, 0, 16,16))#, colorkey=(255, 255, 255))
        self.images = [ss.image_at((0, 0, 16, 16)), 
                       ss.image_at((16 * 1 + 1, 0, 16, 16)),
                       ss.image_at((16 * 2 + 1, 0, 16, 16))
                       ]
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.rect.h = 50


        # self.pos = (0,0)
        # self.x = 0
        # self.y = 0

    def update(self):
        # print('update')

        self.tick += 1

        if self.tick % 60 == 0:    
            self.frame += 1

        # TODO multiple animations and animation frames
        self.image = self.images[self.frame % len(self.images)]

        # self.pos = (0,0)




class Game():

    # screen: pygame.surface.Surface
    # player: Player
    sprites: pygame.sprite.Group

    def __init__(self, 
                #  screen: pygame.surface.Surface, 
                #  player: Player,
                 sprites: pygame.sprite.Group,
                 frames_per_second: int
                 ):

        # self.screen = screen
        self.player = Player(0,0)
        self.sprites = sprites
        self.sprites.add(self.player)
        self.frames_per_second = frames_per_second
        self.delta = 60.0 / self.frames_per_second # at 120 fps move at half speed per tick

    # FPS here
    def main_loop(self, events: List[pygame.Event]):
            
        for event in events:  # Process all events in the queue
            if event.type == pygame.QUIT:
                return False


        # self.player.x += (1.0 * self.delta)

        self.player.rect.x += (1.0 * self.delta)
        # self.player.update()



        return True


# https://pyga.me/docs/ref/display.html#pygame.display.set_window_position
# switch to pygame-ce???
# https://www.reddit.com/r/pygame/comments/1ajih56/pygame_or_pygamece/
# pygame-ce 2.5.6 (SDL 2.32.10, Python 3.13.9)                                                                                                                                             
def main():


    
    screen = get_screen()

    # ss = spritesheet.spritesheet('galaga_sprites.png')

    # player = Player(0,0)

    game_sprites = pygame.sprite.Group()

    # initialize with screen (probably not necessary?)
    # and a game sprite group. The game handles the main loop,
    # but not the drawing on the actual screen if possible to separate these two
    game = Game(game_sprites, frames_per_second=FPS)

# https://github.com/pygame/pygame/issues/1525
# https://www.gamedev.net/forums/topic/428022-sdl-window-resize-glitch/
    pygame.display.flip() # Or pygame.display.update()

    clock = pygame.time.Clock()

    i = 0
    running = True



    while running:
        i += 1
        # print(i)
        if i > 555:
            return
        
        screen.fill(FILL)


        running = game.main_loop(pygame.event.get())

        game_sprites.update()
        game_sprites.draw(screen)

        pygame.display.flip() # Or pygame.display.update()
        # screen.update() # https://www.pygame.org/docs/ref/display.html#pygame.display.update partial screen update

        # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
        clock.tick(FPS)

    return


_init()

main()

pygame.quit()
