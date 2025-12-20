
import pygame
import os
from lib_inputs import InputHandler


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

FILL = (5, 5, 5)

class TestHandler():
    screen = None
    is_ci_test = False
    is_pygame_init = False
    tick = 0
    
    def __init__(self, is_ci_test = os.environ.get('IS_CI_TEST', '0') == '1'):
        self.is_ci_test = is_ci_test
        pass

    def init_pygame(self):

        if not self.is_pygame_init:
            print("pygame init")
            pygame.init()
            # pygame.mixer.init()
            # int fonts for display
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
        else:
            print("pygame init already called. to change screensize call ...")
        
        self.is_pygame_init = True
        self.font = pygame.font.SysFont("Arial" , 18 , bold = False)
        self.clock = pygame.time.Clock()




        pass

    def do_iteration(self, ih: InputHandler, callback):
        ih.clear_just_pressed()
        for event in pygame.event.get():
            ih.handle_event(event)

            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        
        self.screen.fill(FILL)

        callback()

        pygame.display.flip()

        self.clock.tick(60)
        self.tick += 1
        return True
    pass

test_handler = TestHandler()

# https://stackoverflow.com/questions/34466027/what-is-conftest-py-for-in-pytest

# for some reason it seems like this wasn't being called.
# not calling pygame.init can lead to a segmentation fault that is hard to debug

# called between each test
def pytest_runtest_setup():
    print("")
    print("pytest_runtest_setup")
    test_handler.init_pygame()

