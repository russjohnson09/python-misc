import os
import pygame
import numpy


_default_asset_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../assets'))

ASSET_DIR = os.environ.get('ASSET_DIR', _default_asset_dir)


def _image_at(spritesheet, rectangle):
    # # Load a specific image from a specific rectangle
    # def image_at(self, rectangle):
    "Loads image from x,y,x+offset,y+offset"
    rect = pygame.Rect(rectangle)

    return spritesheet.subsurface(rect)

class PongSpriteSheets():

    PAC_BOARD = 'pac_board.png'
    PAC_LETTERS = 'pacman_letters.png'
    spritesheets = {}

    def get_spritesheet(self, name = PAC_BOARD):
        if not self.spritesheets.get(name):
            self.spritesheets[name] = pygame.image.load(
            os.path.join(ASSET_DIR, name)
        ).convert_alpha()
        return self.spritesheets.get(name)
            
pong_sprite_sheets = PongSpriteSheets()

class PongSprite(pygame.sprite.Sprite):

    tick = 0
    frame = 0

    def __init__(self):
        super().__init__()
        self.pac_board_spritesheet = pong_sprite_sheets.get_spritesheet(PongSpriteSheets.PAC_BOARD)
        print(self.pac_board_spritesheet)
        # self.spritesheet1 = pong_sprite_sheets.get_spritesheet(PongSpriteSheets.PAC_BOARD)


class PongPaddle(PongSprite):

    def __init__(self):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.pac_board_spritesheet

        self.image = _image_at(spritesheet,(288,124,8,32))

        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

class PongGhostBall(PongSprite):

    animation_ticks_per_frame = 15

    velocity = numpy.array([1.5,1.5])
    # velocity = [4,4]

    topleft = numpy.array([50.0,50.0])
    # red ghost by default
    animations = {
        'walk_right': [],
        'walk_left': [],
    }
    # has velocity and collision detection?
    # if at top or bottom of screen bounce.
    # gradually increase in speed up to one pixel per frame or 60 pixels per second.
    def __init__(self):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.pac_board_spritesheet

        self.animation = 'walk_left'
        self.animations['walk_left'] = [
             _image_at(spritesheet,(457,65,14,14)),
             _image_at(spritesheet,(473,65,14,14))
        ]

        self.image = self.animations['walk_left'][0]

        self.rect = self.image.get_rect()
        # self.topleft = [0,0]

        # if has collison with paddle change direction.
        # this is handled by the paddle.
        # if top or bottom wall move in opposite direction.
    def update(self):
        self.tick += 1

        # ticks or frames
        if self.tick % self.animation_ticks_per_frame == 0:
            self.frame += 1
        
        # else:
            # return

        # self.topleft[0] += self.velocity[0]
        # self.topleft[1] += self.velocity[1]

        images = self.animations[self.animation]
        self.image = images[self.frame % len(images)]
        self.rect = self.image.get_rect()

        # print(self.topleft, self.velocity)
        self.topleft += self.velocity

        # self.rect.topleft =   self.topleft # (int(self.topleft[0]), int(self.topleft[1]))

        self.rect.topleft = self.topleft #[50.5,50.0]

# (66, 66)
# [66.79 66.79]
# (66, 66)
# [67.02 67.02]
# (67, 67)
# [67.25 67.25]
# (67, 67)
#         print(self.topleft)
#         print(self.rect.topleft)

        # self.rect.bottomleft = self.bottomleft
        # self.rect.bottomleft = (0,0)