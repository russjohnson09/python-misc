import os
import pygame


_sheet1 = None

_default_asset_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../assets'))

ASSET_DIR = os.environ.get('ASSET_DIR', _default_asset_dir)

def _image_at(spritesheet, rectangle):
    # # Load a specific image from a specific rectangle
    # def image_at(self, rectangle):
    "Loads image from x,y,x+offset,y+offset"
    rect = pygame.Rect(rectangle)

    return spritesheet.subsurface(rect)

def _get_sheet1():
    global _sheet1
    filename = os.path.join(ASSET_DIR, 'Game Boy _ GBC - Blade - Playable Characters - Blade.png')

    if _sheet1 is None:
        _sheet1 = pygame.image.load(filename).convert_alpha()

    return _sheet1


class BladeSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # import lib_spritesheet
        # self.spritesheet = lib_spritesheet.GalagaSpritesheet()
         # image location

        self.spritesheet = _get_sheet1()


class Blade(BladeSprite):


    tick = 0
    frame = 0
    animation = 'idle'
    # https://www.pygame.org/docs/ref/sprite.html

    animations = {
        'idle': [],
    }

    def update_image(self):
        spritesheet = self.spritesheet

        # Size is 24 / 38 ?
        self.animations['idle'] = [
            _image_at(spritesheet, (16,16,24,38)),
            _image_at(spritesheet, (42,17,24,37)),
            _image_at(spritesheet, (68,18,24,36)),

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
