import pygame
import os


_default_asset_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../assets'))

ASSET_DIR = os.environ.get('ASSET_DIR', _default_asset_dir)


# https://stackoverflow.com/questions/21080790/pygame-and-rotation-of-a-sprite
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


class Velocity:

    x = 0
    y = 0


class GalagaSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        import lib_spritesheet
        self.spritesheet = lib_spritesheet.GalagaSpritesheet()


class ShipSprite(GalagaSprite):

    # I am accidently making these static.
    # Including velocity which I'm now fixing
    tick = 0
    frame = 0
    animation = 'idle'
    # https://www.pygame.org/docs/ref/sprite.html
    image_path = "galaga_sprites.png"

    animations = {
        'idle': [],
        'red': [],
    }
    def __init__(self):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.spritesheet
        self.animations['idle'] = [spritesheet.image_at((18 * i, 0, 18, 18)) for i in range(0,7)]
        self.images = self.animations.get(self.animation)
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect: pygame.Rect = self.image.get_rect()
        # self.rect = self.rect.copy()

        # self.rect.topleft = (0,0)
        # self.rect.h = 50
        self.rect = pygame.Rect(0,0,18,18)

        self.velocity = Velocity()


    # TODO change animation
    def update(self):
        self.tick += 1

        # ticks or frames
        if self.tick % 30 == 0:
            self.frame += 1

        # self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.image = self.images[self.frame % len(self.images)]

    #     # self.pos = (0,0)




class BeeSprite(GalagaSprite):


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

        self.animations['idle'] = [spritesheet.image_at((18 * i, 18 * 5, 18, 18)) for i in range(0,8)]
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

    #     # self.pos = (0,0)



class ShrimpSprite(GalagaSprite):


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

        self.animations['idle'] = [spritesheet.image_at((18 * i, 18 * 6, 18, 18)) for i in range(0,7)]
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

    #     # self.pos = (0,0)



class ShipExplosion(GalagaSprite):


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
        
        # 16 + 2 = 18
        # 32 + 2 = 34 for the size with padding
        offset_x = 36 * 4
        self.animations['idle'] = [spritesheet.image_at((offset_x + (34 * i), 0, 34, 34)) for i in range(0,4)]

        self.animations['idle'] = [pygame.transform.scale(image, (image.height / 2, image.width / 2)) for image in self.animations['idle']]

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

    #     # self.pos = (0,0)


# https://www.spriters-resource.com/nes/chessmaster/asset/33121/
class WhitePawn(pygame.sprite.Sprite):
    # https://www.pygame.org/docs/ref/sprite.html
    def __init__(self):
        super().__init__()
        filename = os.path.join(ASSET_DIR, 'chesspieces/wikipedia/wP.png')
        self.image = pygame.image.load(filename).convert_alpha()#.convert()

        # size = self.image.get_size()
        # scale = 0.2
        # create a 2x bigger image than self.image
        # self.image = pygame.transform.scale(self.image, (int(size[0]*scale), int(size[1]*scale)))

        self.rect = self.image.get_rect()
