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

class Spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()#.convert()
        except Exception as e:
            raise e

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)

        return self.sheet.subsurface(rect)



class GalagaSpritesheet(Spritesheet):

    def __init__(self):
        filename = os.path.join(ASSET_DIR, 'galaga_sprites.png')
        super().__init__(filename)






class PlayerSprite(pygame.sprite.Sprite):

    tick = 0
    frame = 0
    animation = 'idle'
    # https://www.pygame.org/docs/ref/sprite.html
    image_path = "galaga_sprites.png"

    animations = {
        'idle': [],
        'red': [],
    }
    def __init__(self, spritesheet: GalagaSpritesheet):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        # self.tick = 0
        # self.frame = 0
        # image = spritesheet.image_at((0, 0, 16, 16)) # TODO multiple images for player animation
        # colorkey = (255, 255, 255)
        # images = ss.images_at((0, 0, 16, 16),(17, 0, 16,16))#, colorkey=(255, 255, 255))
        # self.images = [spritesheet.image_at((0, 0, 16, 16)), 
        #                spritesheet.image_at((16 * 1 + 1, 0, 16, 16)),
        #                spritesheet.image_at((16 * 2 + 1, 0, 16, 16))
        #                ]
        
        self.animations['idle'] = [spritesheet.image_at((18 * i, 0, 18, 18)) for i in range(0,7)]
        self.images = self.animations.get(self.animation)
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        # self.rect.h = 50


    # TODO change animation
    def update(self):
        self.tick += 1

        print(self.tick)
        # ticks or frames
        if self.tick % 30 == 0:
            self.frame += 1

        self.image = self.images[self.frame % len(self.images)]

    #     # self.pos = (0,0)