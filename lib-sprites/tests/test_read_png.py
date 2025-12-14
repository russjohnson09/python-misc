from lib_sprites import Megaman2Tileset
import pygame
import numpy
import os

from .conftest import get_screen
FILL = (5, 5, 5)
FILL = (15, 15, 15)
FILL = (255,255,255)

FPS = 120

_default_asset_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../assets'))

ASSET_DIR = os.environ.get('ASSET_DIR', _default_asset_dir)

def fps_counter(screen, clock, font):
    # fps = str(clock.get_fps())
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))


# class GenericSprite(pygame.sprite.Sprite):

#     def __init__(self):

#         self.image = surface

# mega man 2 tiles are 16 x 16 so scale up 16 and then double that for the snes / psx resolution
def _scale(
    surface: pygame.surface.Surface, 
scale = 16 * 2
) -> pygame.surface.Surface:
    return pygame.transform.scale(
            surface, 
        (surface.get_size()[0]*scale, surface.get_size()[1]*scale))


# TODO draw sprite black for no collision and red for collision
class Camera():

    # x = 10000
    # y = 100

    def __init__(self):
        self.x = 10
        self.y = 10
        pass

class CameraControl():

    left = False
    right = False
    down = False
    up = False

    def __init__(self, camera):
        self.camera = camera
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.right = True
            elif event.key == pygame.K_a:
                self.left = True
            elif event.key == pygame.K_w:
                self.up = True
            elif event.key == pygame.K_s:
                self.down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.right = False
            elif event.key == pygame.K_a:
                self.left = False
            elif event.key == pygame.K_w:
                self.up = False
            elif event.key == pygame.K_s:
                self.down = False



        pass

    def loop(self):
        if self.right:
            self.camera.x += 1
        elif self.left:
            self.camera.x += -1
        if self.up:
            self.camera.y += -1
        elif self.down:
            self.camera.y += 1


def _get_color_left(x, y, surface):
    size = surface.get_size()
    if x == 0:
        return None
    return surface.get_at((x - 1, y))

def _get_color_right(x, y, surface):
    size = surface.get_size()
    if x == (size[0] - 1):
        return None
    return surface.get_at((x + 1, y))

def _get_color_up(x, y, surface):
    size = surface.get_size()
    if x == 0:
        return None
    return surface.get_at((x, y - 1))

def _get_color_down(x, y, surface):
    size = surface.get_size()
    if y == (size[1] - 1):
        return None
    return surface.get_at((x, y + 1))




def _apply_tileset_to_color_surface(surface, tileset):
    """given a surface with colors applied create a new surface with some tileset"""

    def _is_match(color1, color2):
        rgba1 = (color1.r,color1.g,color1.b,color1.a )
        rgba2 = (color2.r,color2.g,color2.b,color2.a )
        return rgba1 == rgba2
    

    # TODO define this mapping
    ceiling = pygame.Color(255,0,0)
    ceiling_left = pygame.Color(100,0,0)
    ceiling_right = pygame.Color(50,0,0)

    ground = pygame.Color(255,255,0)
    ground_corner_left = pygame.Color(125,125,0)
    ground_corner_right = pygame.Color(100,100,0)

    sub_surface = pygame.Color(255,0,255)

    new_surface = surface.copy()

    # tileset block size
    new_surface = _scale(new_surface, 16)

    for x in range(0,surface.get_size()[0]):
        for y in range(0,surface.get_size()[1]):
            color: pygame.Color = surface.get_at((x,y))
            if color.a == 0:
                continue
            if _is_match(color, ground):
                # apply image at location
                new_surface.blit(tileset.ground, (x * 16,y * 16))
            elif _is_match(color, ground_corner_left):
                new_surface.blit(tileset.ground_corner_left, (x * 16,y * 16))


    return new_surface

def _get_new_color(x,y, surface):
    size = surface.get_size()

    ceiling = pygame.Color(255,0,0)
    ceiling_left = pygame.Color(100,0,0)
    ceiling_right = pygame.Color(50,0,0)

    ground = pygame.Color(255,255,0)
    ground_corner_left = pygame.Color(125,125,0)
    ground_corner_right = pygame.Color(100,100,0)

    sub_surface = pygame.Color(255,0,255)

    color_left = _get_color_left(x,y,surface)
    color_up =  _get_color_up(x,y,surface)
    color_down =  _get_color_down(x,y,surface)
    color_right =  _get_color_right(x,y,surface)

    if color_up is None:
        return ceiling

    # color_up: pygame.Color = surface.get_at((x,y - 1))
    # color_left: pygame.Color = surface.get_at((x,y - 1))
    # color_up: pygame.Color = surface.get_at((x,y - 1))
    # color_up: pygame.Color = surface.get_at((x,y - 1))

    if color_up.a == 0:
        if color_left is None:
            return ground
        elif color_left.a == 0:
            return ground_corner_left
        elif color_right is None:
            return ground
        elif color_right.a == 0:
            return ground_corner_right
        return ground
    else:
        if color_down is None:
            return sub_surface
        elif color_down.a == 0:
            if color_left is None:
                return ceiling
            elif color_left.a == 0:
                return ceiling_left
            elif color_right is None:
                return ceiling_right
            elif color_right.a == 0:
                return ceiling_right
            else:
                return ceiling


    

    # look up, down, left, and right.
    # first pass establishes ground and ceiling.
    # new pass establish some ground pattern.
    # for very simple tilesets it is either ground flat or ground corner.
    color = pygame.Color(0,255,0)


    return pygame.Color(0,0,0)

def _read_surface(surface: pygame.surface.Surface):

    new_surface = surface.copy()
    # surface.

    # get_at()
    size = surface.get_size()
    width = size[0]
    height = size[1]

# Note If the surface is palettized, the pixel color will be set to the most similar color in the palette.
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_at_mapped
    print(size)
    for x in range(0,width):
        for y in range(0,height):
            color: pygame.Color = surface.get_at((x,y))

            rgb = (color.r, color.g, color.b)
            alpha = color.a
            if alpha == 0:
                continue

            new_color = _get_new_color(x,y, surface)
            new_surface.set_at((x,y), new_color)
            print(x,y,new_color)

            # print(x,y,color)
            # if rgb == (0,0,0):
                # new_color = pygame.Color((0,255,0))
                # new_surface.set_at((x,y), new_color)
            # print(i)

    print(size)

    return new_surface

# FULLSCREEN=1 uv run pytest tests/test_pong.py 
def test_read_png():
    font = pygame.font.SysFont("Arial" , 8 , bold = False)

    # read in a png and write out some platform using a tileset.
    screen = get_screen()

    clock = pygame.time.Clock()

    basic_platform_image_original = pygame.image.load(
                os.path.join(ASSET_DIR, "basic_platform.png")
            ).convert_alpha()

    basic_platform_image_color = _read_surface(basic_platform_image_original)

    tileset = Megaman2Tileset()
    surface_with_tileset_applied = _apply_tileset_to_color_surface(basic_platform_image_color, tileset)

    basic_platform_image = _scale(surface_with_tileset_applied, 2)



    camera = Camera()

    camera_control = CameraControl(camera)

    platform_sprites =  pygame.sprite.Group()


    i = 0
    while i < (60 * 50):
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        for event in pygame.event.get():
            camera_control.handle_event(event)

            if event.type == pygame.QUIT:
                # self._quit = True
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                # if event.key == pygame.K_d:
                #     camera.x += 1
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     just_clicked = True

        camera_control.loop()
        pygame.event.get()
        screen.fill(FILL)


        # sprites_misc.update()
        # sprites_misc.draw(screen)

        # pygame.sprite.collide_rect(platform_sprite, camera_sprite)

        screen.blit(basic_platform_image, (-camera.x, -camera.y))

        # blit camera + 100 + 100 rect

        # check collision on sprite
       
        fps_counter(screen, clock, font)
        
        pygame.display.flip()




# https://www.reddit.com/r/pygame/comments/k7677j/how_to_make_a_basic_deltatime_system/
        clock.tick(FPS)
        # clock.tick()

        i += 1
    pass



    pass