

from lib_sprites import Blade
import pygame
import os

from .conftest import get_screen_nes as get_screen
MAX_TEST_LOOPS = int(os.environ.get('MAX_TEST_LOOPS', (60 * 60)))

FILL = (100, 100, 100)

def test_main():
    screen = get_screen()
    clock = pygame.time.Clock()

    player = Blade()

    player.bottomleft = (20,50)

    player_sprites = pygame.sprite.Group()

    player_sprites.add(player)

    mouse_sprites =  pygame.sprite.Group()
    mouse_sprite = Blade()
    mouse_sprites.add(mouse_sprite)

    just_clicked = False
    i = 0
    while i < MAX_TEST_LOOPS:
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self._quit = True
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONUP:
                just_clicked = True
        pygame.event.get()
        screen.fill(FILL)

        pos = pygame.mouse.get_pos()
        mouse_sprite.bottomleft = pos

        if just_clicked:
            just_clicked = False
            mouse_sprite.cycle()
        player_sprites.update()
        player_sprites.draw(screen)

        mouse_sprites.update()
        mouse_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass