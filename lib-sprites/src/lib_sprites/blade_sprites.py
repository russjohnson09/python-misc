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
    animation = 'uppercut'
    bottomleft = (0,0)
    # https://www.pygame.org/docs/ref/sprite.html

    animations = {
        'idle': [],
        'walk': [],
        'uppercut': [],
        'punch': [],
    }


    def cycle(self):
        animations_list = list(self.animations.keys())
        print(animations_list)

        i = 0
        for idx, x in enumerate(animations_list):
            if self.animation == x:
                i = idx

        i += 1
        i = i % len(animations_list)
        self.animation = animations_list[i]
        self.images = self.animations.get(self.animation)
        print(self.animation, i)

    def update_image(self):
        spritesheet = self.spritesheet

        # Add some padding so that I can use top left consistently between animations?
        # or anchor bottom left?
        self.animations['idle'] = [
            _image_at(spritesheet, (16,16,24,38)),
            _image_at(spritesheet, (42,16,24,38)),
            _image_at(spritesheet, (68,16,24,38)),
            _image_at(spritesheet, (42,16,24,38)), # mid point on the way back to frame 0

            ]
        
        self.animations['punch'] = [
            _image_at(spritesheet, (16,149,29,38)),
            _image_at(spritesheet, (47,149,37,38)),

            ]
        
        # make the size 48,48
        
        mid_walk =  (19,60,20,38)
        right_step = (41,61,21,38)
        left_step = (64,61,24,38)

        self.animations['walk'] = [
            _image_at(spritesheet,mid_walk),
            _image_at(spritesheet,right_step),
            _image_at(spritesheet,mid_walk),

            _image_at(spritesheet,left_step),

            # _image_at(spritesheet, (41,61,21,38)),

            ]
        
        start_uppercut = (16,246,36,32)
        mid_uppercut = (54,231,29,47)
        end_uppercut = (85,239,30,39)
        self.animations['uppercut'] = [
            _image_at(spritesheet,start_uppercut),
            _image_at(spritesheet,mid_uppercut),
            _image_at(spritesheet,end_uppercut),


            ]


        self.images = self.animations.get(self.animation)
        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,0)
        pass

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
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.bottomleft
        # self.rect.bottomleft = (0,0)
