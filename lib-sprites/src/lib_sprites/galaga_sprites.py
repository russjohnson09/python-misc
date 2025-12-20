import pygame
import random

class Velocity:

    x = 0
    y = 0



# I'd like maybe a 100 frame repeat surface / image
# I can add as many stars as I'd like because I'm only dealing with a single sprite.
# Output frames to images and use those.
def _add_stars(screen_size, FPS):
    star_sprites_group = pygame.sprite.Group()

    x = 0
    star_size = (2,2)
    star_gap = 10
    i = 0


    rng = random.Random(1)
    rng = random.Random(2)

    star_chance = 0.02

    # print(rng.random()) #0.13436424411240122

    # random but seeded
    # https://docs.python.org/3/library/random.html#random.seed

    # min space is 9 pixels but each square has only a 10% chance of being picked
    # while x < screen_size[0]:# size[0]:
    for x in range(5, screen_size[0], 9):
        for y in range(5, screen_size[1], 9):
            if rng.random() >=star_chance:
                continue

            color = rng.choice([
                pygame.Color(255,255,255),
                pygame.Color(255,255,255),
                pygame.Color(255,255,255),
                pygame.Color(255,255,255),
                pygame.Color(0,0,255),
                pygame.Color(0,255,255),
                pygame.Color(0,255,0),
                pygame.Color(255,0,0),
            ])
            size = rng.choice([
                (1,1),
                (1,1),
                (1,1),
                (1,1),
                (2,2),
                (2,2),
                # (3,3),
            ])
            star = Star(
                FPS=FPS,
                color=color,
                size=size
            )
            star.alpha_min = rng.randrange(50,100)
            star.rect.topleft = (x,y)
            star_sprites_group.add(star)
            # i += 1
            # star.alpha = (x * y) % 255
            star.alpha = rng.randrange(0, 255)
            star.alpha_inc = rng.choice([-3,-2,2, 3])
            # star.alpha_inc = randrange(0, 255)

            # star.alpha = i % 255
            print(f'added star ({x},{y})')
        # inc_x = rng.randrange(50, 193)
        # print(inc_x)
        # x += inc_x

    return star_sprites_group




# Call pygame.Surface()pygame object for representing images to create a new image object. The Surface will be cleared to all black. The only required arguments are the sizes. With no additional arguments, the Surface will be created in a format that best matches the display Surface.
# I can use transparency, galaga would have just made the color used darker
class Star(pygame.sprite.Sprite):
    """single pixel color that fades and brightens over time"""

    alpha_min = 20
    alpha = 255
    alpha_inc = -2

    frame = 0
    _surface: pygame.Surface
    _base_color: pygame.Color
    _tick = 0

    def __init__(self,
        FPS,
        animation_speed = 60,
        color = pygame.Color(255,255,255),
        size = (1,1),
    ):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        self._ticks_per_frame = (FPS / animation_speed) # 60 fps

        # create a 1x1 surface and have it be white
        self._surface = pygame.Surface(size)
        self._surface.fill(color)

        # self._populate_images()
        self.image = self._surface

        self.rect = self.image.get_rect()


    def update(self):
        self._tick += 1
        if self._tick % self._ticks_per_frame != 0:
            return
        # self.frame += 1
        # self.frame = self.frame % len(self._images)

        self.alpha += self.alpha_inc

        if self.alpha < self.alpha_min:
            self.alpha = self.alpha_min
            self.alpha_inc = -(self.alpha_inc)
        elif self.alpha > 255:
            self.alpha = 255
            self.alpha_inc = -(self.alpha_inc)

        # self.image.get_alpha
        self.image.set_alpha(self.alpha)
        # self.image = self._images[self.frame]
        pass




class StarrySky(pygame.sprite.Sprite):

    topleft = (0,0)
    _sprite_group: pygame.sprite.Group = None

    def __init__(self, 
    FPS: int,
    screen: pygame.Surface, # screen to copy from
    sprite_group: pygame.sprite.Group = None
    ):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        size = screen.get_size()
        self._min_topleft = (0, -size[1])
        self._max_topleft = (0, size[1])
        self.topleft = self._min_topleft

        self.image = screen.copy()
        self.image.fill((0,0,0,0))

        self.rect = self.image.get_rect()

        if sprite_group is None:
            sprite_group = _add_stars(screen.get_size(), FPS)
        self._sprite_group = sprite_group



    def update(self):
        self.image.fill((0,0,0,0))
        self._sprite_group.update()
        self._sprite_group.draw(self.image)

        self.topleft = (self.topleft[0], self.topleft[1] + 1)

        if self.topleft[1] > self._max_topleft[1]:
            self.topleft = self._min_topleft

        self.rect.topleft = self.topleft

        pass

class GalagaBgSpriteGroup(pygame.sprite.Group):
    def __init__(self, FPS: int, screen):
        # I should pull in some singleton class for sprite management here.
        super().__init__()
        
        starry_sky_sprite = StarrySky(
            FPS,
            screen
        )
        starry_sky_sprite.topleft = (0,0)
        starry_sky_sprite2 = StarrySky(
            FPS,
            screen
        )

        self.add(starry_sky_sprite)
        self.add(starry_sky_sprite2)

class GalagaSprite(pygame.sprite.Sprite):
    topleft = (0,0)

    def __init__(self):
        super().__init__()

        import lib_spritesheet
        self.spritesheet = lib_spritesheet.GalagaSpritesheet()


class BeeSprite(GalagaSprite):
    # https://www.pygame.org/docs/ref/sprite.html


    tick = 0
    frame = 0

    images = []
    
    # animations = {
    #     'idle': [],
    # }
    def __init__(self):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.spritesheet

        self.images = [spritesheet.image_at((18 * i, 18 * 5, 18, 18)) for i in range(0,8)]   

        self.image = self.images[0] # current image
        # self.image = pygame.image.load(self.image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()

        self.rect.topleft = (0,0)


    # TODO change animation
    def update(self):
        self.rect.topleft = self.topleft



class ShipSprite(GalagaSprite):

    # I am accidently making these static.
    # Including velocity which I'm now fixing
    # tick = 0
    # frame = 0
    # animation = 'idle'
    # https://www.pygame.org/docs/ref/sprite.html
    image_path = "galaga_sprites.png"

    topleft = (0,0)

    def __init__(self, scale = 1):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.spritesheet

        # self.animations['idle'] = [spritesheet.image_at((18 * i, 0, 18, 18)) for i in range(0,7)]

        def _scale_image(img, scale: int):
            size = img.get_size()
            return pygame.transform.scale(img, (size[0] * scale, size[1] * scale))

        self.images = [
            _scale_image(spritesheet.image_at((18 * i, 0, 18, 18)), scale) for i in range(0,7)
            ]
        # self.images = self.animations.get(self.animation)

        self.image = self.images[6] # current image

        self.rect: pygame.Rect = self.image.get_rect()


    # TODO change animation
    def update(self):
        self.rect.topleft = self.topleft

