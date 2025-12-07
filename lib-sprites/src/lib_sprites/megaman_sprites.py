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


class MegamanSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # import lib_spritesheet
        # self.spritesheet = lib_spritesheet.GalagaSpritesheet()
         # image location

        self.spritesheet = _get_megaman_spritesheet()


class OctopusBattery(MegamanSprite):


    tick = 0
    frame = 0
    animation = 'idle'
    # https://www.pygame.org/docs/ref/sprite.html

    animations = {
        'idle': [],
    }
    def __init__(self):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.spritesheet

        self.animations['idle'] = [_image_at(spritesheet,(18 * i, 18 * 5, 18, 18)) for i in range(0,8)]
        self.images = self.animations.get(self.animation)
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        # self.rect.h = 50


    # TODO change animation
    def update(self):
        self.tick += 1

        # ticks or frames
        if self.tick % 30 == 0:
            self.frame += 1

        self.image = self.images[self.frame % len(self.images)]
