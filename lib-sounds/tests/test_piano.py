

from lib_sounds import Piano
import pygame

from .conftest import get_screen
FILL = (5, 5, 5)


def test_piano():
    screen = get_screen()

    clock = pygame.time.Clock()

    
    piano = Piano()

    # piano.play_note(note='A4')


    # sound.play()

    i = 0
    while i < (60 * 3):
        for event in pygame.event.get():  # Process all events in the queue

            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                print('keydown', event.key)
                if event.key == pygame.K_k:
                    print('play note')
                    piano.play_note(note='A4')
                if event.key == pygame.K_RETURN:  # Check if Enter was pressed
                    print('play note')
                    piano.play_note(note='A4')
            
        screen.fill(FILL)



        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass