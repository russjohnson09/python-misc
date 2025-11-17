

from lib_sprites import GalagaSpritesheet, PlayerSprite
import pygame

from .conftest import get_screen
FILL = (5, 5, 5)



def test_main():
    galaga_spritesheet = GalagaSpritesheet()

    screen = get_screen()

    clock = pygame.time.Clock()

    game_sprites = pygame.sprite.Group()

    player = PlayerSprite(galaga_spritesheet)
    game_sprites.add(player)

    i = 0
    while i < (60 * 10):
        pygame.event.get()
        screen.fill(FILL)

        game_sprites.update()
        game_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass