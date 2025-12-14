

from lib_spritesheet import GalagaSpritesheet
import pygame

from .conftest import get_screen
FILL = (5, 5, 5)


class MockSprite(pygame.sprite.Sprite):


    tick = 0
    frame = 0
    animation = 'idle'
    # https://www.pygame.org/docs/ref/sprite.html

    animations = {
        'idle': [],
    }
    def __init__(self, spritesheet: GalagaSpritesheet):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        sheet: pygame.image = spritesheet.sheet
       
        
        self.image = spritesheet.image_at((0,0, sheet.get_width(),sheet.get_height()))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        # self.rect.h = 50


    # # TODO change animation
    # def update(self):
    #     self.tick += 1

    #     # ticks or frames
    #     if self.tick % 30 == 0:
    #         self.frame += 1

    #     self.image = self.images[self.frame % len(self.images)]

    # #     # self.pos = (0,0)


def test_main():
    galaga_spritesheet = GalagaSpritesheet()
    sprite = MockSprite(galaga_spritesheet)

    screen = get_screen()

    clock = pygame.time.Clock()

    spritesheet_group =  pygame.sprite.Group()

    spritesheet_group.add(sprite)



    i = 0
    while i < (60 * 3):
        pygame.event.get()
        screen.fill(FILL)

        spritesheet_group.update()
        spritesheet_group.draw(screen)


        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass