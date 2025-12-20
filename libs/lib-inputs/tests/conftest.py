
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

    _primary_joystick: pygame.joystick.JoystickType = None

    _joysticks: list[pygame.joystick.JoystickType] = []
    
    def __init__(self, is_ci_test = os.environ.get('IS_CI_TEST', '0') == '1'):
        self.is_ci_test = is_ci_test
        pass

    def get_primary_joystick(self):
        if len(self._joysticks) == 0:
            print('no joystick devices found')
            return None
        if not self._primary_joystick:
            # use the first Xbox 360 Controller or use the first one found
            for joystick in self._joysticks:
                # js: pygame.joystick.JoystickType = joystick
                print(f"{joystick.get_name()} {joystick.get_guid()}")
                # Xbox 360 Controller 0300b9695e0400008e02000000007200
                if joystick.get_name() == "Xbox 360 Controller":
                    self._primary_joystick = joystick
                    break
        if not self._primary_joystick:
            print("no Xbox 360 Controller found defaulting to first in list")
            self._primary_joystick = self._joysticks[0]
        return self._primary_joystick


    def init_pygame(self):

        if not self.is_pygame_init:
            print("pygame init")
            pygame.init()
            # pygame.mixer.init()
            # int fonts for display
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
        else:
            print("pygame init already called. to change screensize call ...")
        
        pygame.joystick.init()
        # [<pygame.joystick.Joystick object at 0x0000021A9D01BEA0>]
        self._joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        print( self._joysticks)


        self.is_pygame_init = True
        self.font = pygame.font.SysFont("Arial" , 18 , bold = False)
        self.clock = pygame.time.Clock()





        pass

    def do_iteration(self, ih: InputHandler, callback):
        ih.clear_just_pressed()
        for event in pygame.event.get():
            print("do_iteration", event)
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

