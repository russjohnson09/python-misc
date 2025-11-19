

from lib_sounds import MMX5StageStart
import pygame

from .conftest import get_screen
FILL = (5, 5, 5)


def test_main():
    screen = get_screen()

    clock = pygame.time.Clock()

    
    sound: pygame.mixer.Sound = MMX5StageStart()


    sound.play()

    i = 0
    while i < (60 * 3):
        pygame.event.get()
        screen.fill(FILL)



        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass