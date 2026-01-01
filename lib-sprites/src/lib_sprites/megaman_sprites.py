import os
import pygame


_megaman_spritesheet = None

_default_asset_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../assets'))

ASSET_DIR = os.environ.get('ASSET_DIR', _default_asset_dir)


def _image_at(spritesheet, rectangle):
    # # Load a specific image from a specific rectangle
    # def image_at(self, rectangle):
    "Loads image from x,y,x+offset,y+offset"
    rect = pygame.Rect(rectangle)

    return spritesheet.subsurface(rect)

def _get_megaman_spritesheet():
    global _megaman_spritesheet
    filename = os.path.join(ASSET_DIR, 'mm1enemysheet.gif')

    if _megaman_spritesheet is None:
        _megaman_spritesheet = pygame.image.load(filename).convert_alpha()

    print(_megaman_spritesheet, filename)
    return _megaman_spritesheet

_mega_man_2_tiles = None
def _get_mm2_tileset():
    global _mega_man_2_tiles
    filename = os.path.join(ASSET_DIR, 'mega_man_2_tiles.png')

    if _mega_man_2_tiles is None:
        _mega_man_2_tiles = pygame.image.load(filename).convert_alpha()

    return _mega_man_2_tiles


class Megaman2Tileset():

    def __init__(self):
        image = self.tileset = _get_mm2_tileset()

        ceiling = (18,893,16,16)
        self.ceiling = _image_at(image, ceiling)
        self.ceiling_left = _image_at(image,ceiling)
        self.ceiling_right = _image_at(image,ceiling)

        self.ground = _image_at(image,(18,928,16,16))
        self.ground_corner_left = _image_at(image,(18,859,16,16))
        self.ground_corner_right = _image_at(image,(35,859,16,16))
        self.sub_surface = _image_at(image,ceiling)

class MegamanSprite(pygame.sprite.Sprite):

    tick = 0
    frame = 0
    animation = 'idle'
    animations = {
        'idle': [],
    }

    SPRITESHEET_LOCATION = os.path.join(ASSET_DIR, '8bitmegaman.png')
    SPRITESHEET = None

    def update_image(self):
        spritesheet = self.spritesheet

        self.animations['idle'] = [
            _image_at(spritesheet, (101,10,24,24)),
            ]


        self.images = self.animations.get(self.animation)
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        pass

    # TODO scale see galaga
    def __init__(self):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        self.update_image()


    # TODO change animation
    def update(self):
        self.tick += 1

        # ticks or frames
        if self.tick % 30 == 0:
            self.frame += 1

        self.image = self.images[self.frame % len(self.images)]

class SpritesheetManager():

    _megaman1: pygame.sprite.Sprite = None
    _mm1enemysheet: pygame.sprite.Sprite = None

    def __init__(self):

        pass

    @property
    def megaman1(self):
        if not self._megaman1:
            self._megaman1 = pygame.image.load(os.path.join(ASSET_DIR, '8bitmegaman.png')).convert_alpha()

        return self._megaman1

    @property
    def mm1enemysheet(self):
        if not self._mm1enemysheet:
            self._mm1enemysheet = pygame.image.load(os.path.join(ASSET_DIR, 'mm1enemysheet.gif')).convert_alpha()

        return self._mm1enemysheet

sm = SpritesheetManager()

class Megaman1(MegamanSprite):

    def update_image(self):
        self.spritesheet = sm.megaman1
        spritesheet = self.spritesheet

        self.animations['idle'] = [
            _image_at(spritesheet, (101,10,24,24)),
            ]


        self.images = self.animations.get(self.animation)
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        pass
    pass

class OctopusBattery(MegamanSprite):

    OFFSET_RED = 14
    OFFSET_ORANGE = 71
    OFFSET_BLUE = 128

    tick = 0
    frame = 0
    animation = 'idle'
    # https://www.pygame.org/docs/ref/sprite.html

    animations = {
        'idle': [],
    }

    def update_image(self,  x_offset = OFFSET_RED, y_offset = 68, x_space_between_sprites = 19):
        
        spritesheet = sm.mm1enemysheet

        self.animations['idle'] = [
            _image_at(spritesheet, (x_offset ,y_offset,16,16)),
            _image_at(spritesheet, (x_offset + (x_space_between_sprites * 1),y_offset,16,16)),
            _image_at(spritesheet, (x_offset + (x_space_between_sprites * 2),y_offset,16,16))

            ]


        self.images = self.animations.get(self.animation)
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        pass

    def __init__(self, x_offset = OFFSET_RED, y_offset = 68, x_space_between_sprites = 19):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        self.update_image(x_offset, y_offset, x_space_between_sprites)


    # TODO change animation
    def update(self):
        self.tick += 1

        # ticks or frames
        if self.tick % 30 == 0:
            self.frame += 1

        self.image = self.images[self.frame % len(self.images)]



__all__ = [
    Megaman1
]