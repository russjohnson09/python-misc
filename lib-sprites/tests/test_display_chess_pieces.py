

from lib_sprites import ShipSprite, BeeSprite, ShrimpSprite, ShipExplosion, WhitePawn
import pygame

from .conftest import get_screen
FILL = (5, 5, 5)


# https://en.wikipedia.org/wiki/PlayStation_technical_specifications
# SCREEN_WIDTH = 640
# SCREEN_HEIGHT = 480
def test_main():
    # galaga_spritesheet = GalagaSpritesheet()
    # galaga_spritesheet2 = GalagaSpritesheet()

    screen = get_screen()

    clock = pygame.time.Clock()

    player_sprites =  pygame.sprite.Group()

    pawn1 = WhitePawn()
    pawn1.rect.x = 18
    pawn1.rect.y = 32
    player_sprites.add(pawn1)



    i = 0
    while i < (60 * 10):
        pygame.event.get()
        screen.fill(FILL)

        player_sprites.update()
        player_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass