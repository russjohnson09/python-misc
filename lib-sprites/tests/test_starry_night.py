

from lib_sprites import PongGhostBall, PongPaddle
import pygame
import numpy

# from .conftest import get_screen_nes as get_screen
from .conftest import get_screen
from .conftest import PygameHandler
FILL = (5, 5, 5)
FILL = (15, 15, 15)

FPS = 120

pygame_handler = PygameHandler()

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

# Call pygame.Surface()pygame object for representing images to create a new image object. The Surface will be cleared to all black. The only required arguments are the sizes. With no additional arguments, the Surface will be created in a format that best matches the display Surface.
# I can use transparency, galaga would have just made the color used darker
class Star(pygame.sprite.Sprite):
    """single pixel color that fades and brightens over time"""

    alpha = 255
    alpha_inc = -2

    frame = 0
    _surface: pygame.Surface
    _base_color: pygame.Color
    _tick = 0
    # _images = [

    # ]
    ticks_per_frame = (FPS / 60) # 60 fps


    # def _populate_images(self):
    #     for i in range(0, 10):
    #         # new_color = pygame.Color(self._base_color.r, self._base_color.g, self._base_color.b)


    #         # new_color.a = i * 10

    #         image = self._surface.copy()
    #         image.set_alpha(i * 20)
    #         # image.fill(new_color)
    #         self._images.append(image)
    #     pass

    def __init__(self, 
    color = pygame.Color(255,255,255),
    size = (1,1)
    ):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        self._base_color = color

        # create a 1x1 surface and have it be white
        self._surface = pygame.Surface(size)
        self._surface.fill(color)

        # self._populate_images()
        self.image = self._surface

        self.rect = self.image.get_rect()


    def update(self):
        self._tick += 1
        if self._tick % self.ticks_per_frame != 0:
            return
        # self.frame += 1
        # self.frame = self.frame % len(self._images)

        self.alpha += self.alpha_inc

        if self.alpha < 0:
            self.alpha = 0
            self.alpha_inc = -(self.alpha_inc)
        elif self.alpha > 255:
            self.alpha = 255
            self.alpha_inc = -(self.alpha_inc)

        # self.image.get_alpha
        self.image.set_alpha(self.alpha)
        # self.image = self._images[self.frame]
        pass

FPS = 120

# Single server. As the server I can see both players but can't control them.
# Each player / client sends tcp requests to update their locations and that applies to their paddle.

def fps_counter(screen, clock, font):
    # fps = str(clock.get_fps())
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))


def _add_stars(star_sprites_group, screen_size):
    x = 0
    star_size = (2,2)
    star_gap = 10
    i = 0

    for x in range(0, screen_size[0], 50):# size[0]:
        print(x)
        for y in range(0, screen_size[1], 100):
            star = Star()
            star.rect.topleft = (x,y)
            star_sprites_group.add(star)
            i += 1
            star.alpha = (x * y) % 255
            # star.alpha = i % 255
            print(f'added star ({x},{y})')

    pass

def test_starry_night():


    screen = pygame_handler.get_screen()
    size = pygame_handler.get_size()

    font = pygame.font.SysFont("Arial" , 8 , bold = False)

    # score counter.

    clock = pygame.time.Clock()

    star_sprites_group = pygame.sprite.Group()

    _add_stars(star_sprites_group, size)



    # star sprite count 4800 slows down to about 30fps
    print(f"star sprite count {len(star_sprites_group)}")



    i = 0
    while i < (60 * 50):
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self._quit = True
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     just_clicked = True
        screen.fill(FILL)


        star_sprites_group.update()
        star_sprites_group.draw(screen)

        fps_counter(screen, clock, font)
        pygame.display.flip()

        clock.tick(FPS)
        i += 1
