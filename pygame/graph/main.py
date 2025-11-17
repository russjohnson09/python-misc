import pygame
import os

from path import SinPath
import numpy

from typing import Any, Generator, List, Optional, Callable, Tuple
Event = Generator[None, None, None]
Callback = Callable[[], Any]
Colour = Tuple[int, int, int]

FPS = os.environ.get('FPS', 60)

RED = (255, 0, 0)  # RGB values for red
WHITE = (255, 255, 255) # RGB values for white background
BLACK = (0, 0, 0) # RGB values for white background

FILL = (100, 100, 100) # RGB values for white background
FILL = (20, 20, 20) # RGB values for white background
FILL = (5, 5, 5) # RGB values for white background



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def _init():

    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("Red Square Example")

#  640x480 psone
def get_screen(screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT) -> pygame.surface.Surface:
    # screen_width = 800
    # screen_height = 600
    # screen = pygame.display.set_mode((screen_width, screen_height))
    # screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.SCALED)

    return screen


def go_full_screen(screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT) -> pygame.surface.Surface:
    return pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)



class GalagaSprites(pygame.sprite.Sprite):

    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Game():

    # screen: pygame.surface.Surface
    # player: Player
    sprites: pygame.sprite.Group

    def __init__(self, 
                 sprites: pygame.sprite.Group,
                 frames_per_second: int
                 ):

        # self.screen = screen
        self.sprites = sprites
        # self.sprites.add(self.player)
        self.frames_per_second = frames_per_second
        self.delta = 60.0 / self.frames_per_second # at 120 fps move at half speed per tick

    # FPS here
    def main_loop(self, events: List[pygame.Event]):
            
        for event in events:  # Process all events in the queue
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_RETURN:  # Check if Enter was pressed
                    # Check if the Alt key is also pressed (KMOD_ALT)
                    if event.mod & pygame.KMOD_ALT: 
                        print("Alt + Enter detected!")
                        # Add your desired action here, e.g., toggle fullscreen
                        pygame.display.toggle_fullscreen()
        # self.player.rect.x += (1.0 * self.delta)



        return True



def draw_sin(surface: pygame.surface.Surface):
    import math
    import time

    line_color = RED

    frequency = 5
    amplitude = 50
    overallY = 300
    # https://stackoverflow.com/questions/67874803/generating-and-drawing-sin-wave-using-pygame
    no_pts = surface.get_width()

    # no_pts = window.get_width()
    for i in range(no_pts):
        x = i/no_pts * 2 * math.pi
        y = (amplitude * math.cos(x * frequency)) + overallY

        if i > 0:
            pygame.draw.aaline(surface, line_color,  prev_pt, (i, y))
        prev_pt = (i, y)


# time based graph spiral


def draw_points(
        surface: pygame.surface.Surface, 
                points: list[tuple[int,int]],
                offset: numpy.array = numpy.array((0,0))):

    line_color = RED

    prev_pt: tuple[int,int] = None
    for point in points:
        # print(point, offset)
        point_real = point + offset
        # point_real = numpy.array(point) + numpy.array(offset) # points should already be a numpy array?
        if not prev_pt is None:
            # print(point)
            pygame.draw.aaline(surface, line_color,  prev_pt, point_real)
        
        prev_pt = point_real


def main_loop_outer(countdown):


    
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
    running = True

    screen.fill(FILL)

    sin_path = SinPath()


    # draw_sin(screen)


    pygame.display.flip() # Or pygame.display.update()

    while running:
        if countdown is not None:
            pygame.display.set_caption(f"Countdown: {countdown}")
            countdown -= 1
            if countdown < 0:
                return
        
        


        running = game.main_loop(pygame.event.get())

        draw_points(surface=screen,points=sin_path.points, offset=(0,100))


        # game_sprites.update()
        # game_sprites.draw(screen)

        # draw_sin(screen)
        pygame.display.flip() # Or pygame.display.update()
        # screen.update() # https://www.pygame.org/docs/ref/display.html#pygame.display.update partial screen update

        # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
        clock.tick(FPS)


# https://pyga.me/docs/ref/display.html#pygame.display.set_window_position
# switch to pygame-ce???
# https://www.reddit.com/r/pygame/comments/1ajih56/pygame_or_pygamece/
# pygame-ce 2.5.6 (SDL 2.32.10, Python 3.13.9)                                                                                                                                             
def main(countdown = None):


    _init()
    main_loop_outer(countdown)

    pygame.quit()


