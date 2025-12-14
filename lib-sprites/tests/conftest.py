
import pygame
import os

_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../'))
_default_asset_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))

os.environ['ASSET_DIR'] = _default_asset_dir

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

SCREEN_WIDTH_NES = 320
SCREEN_HEIGHT_NES = 240

# SCREEN_WIDTH_NES = 160
# SCREEN_HEIGHT_NES = 120

# SCREEN_WIDTH = SCREEN_WIDTH / 4
# SCREEN_HEIGHT = SCREEN_HEIGHT / 4

_is_init = False


def do_init():
    global _is_init
    print("do_init")
    if _is_init:
        print("already init")
        return

    pygame.init()
    # pygame.mixer.init()
    # print("pygame init")
    # pygame.init()
    # pygame.mixer.init()

    _is_init = True

_screen = None




# tests\test_starry_night_and_player.py Windows fatal exception: access violation

# Current thread 0x00001b68 (most recent call first):
#   File "C:\Users\russ\python-misc\lib-sprites\tests\conftest.py", line 72 in get_screen
#   File "C:\Users\russ\python-misc\lib-sprites\tests\conftest.py", line 78 in do_fullscreen
class PygameHandler():

    _fullscreen = False
    _screen = None
    _size = (640, 480) # psx resolution

    def __init__(self, size = _size):
        self._size = size
        do_init()
        self._clock = pygame.time.Clock()
        self._font = pygame.font.SysFont("Arial" , 8 , bold = False)

        # segmentation fault?
        # if self._screen is None:
        #     self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
        pass

    def get_size(self):
        return self._size

    def get_clock(self):
        return self._clock

    def _fps_counter(self):
        # fps = str(clock.get_fps())
        fps = str(int(self._clock.get_fps()))

        fps_t = self._font.render(fps , 1, pygame.Color("RED"))

        self._screen.blit(fps_t,(0,0))

    def debug(self):
        self._fps_counter()



# https://github.com/pygame-community/pygame-ce/issues/2737
# If you're trying to run code that switches between SCALED and not-scaled, I think it would work to quit and re-initialize the video system while doing it. pygame.display.quit() and pygame.display.init(). Haven't tested though.
# I cannot seem to reproduce this on Ubuntu, perhaps this is a windows only issue
# This is in a whole stream of renderer semantics issues, and all the earliest reports were on Linux, so that's surprising. Are you using an old system SDL? It's an SDL version thing.
    def get_screen(self, refresh = False):
        global _screen
        if _screen is not None:
            print("screen already set")
            self._screen = _screen

        if not self._screen or refresh: # I'm not experiencing a segmentation fault but running these in github it seems like display.set_mode should only run once?
            
            if self._screen:
                print('reinit')
                pygame.display.quit()
                pygame.display.init()
            
            if self._fullscreen:
                self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 
                pygame.FULLSCREEN | pygame.SCALED)
            else:
                self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 
                pygame.RESIZABLE | pygame.SCALED)
        return self._screen

    def do_fullscreen(self):
        self._fullscreen = not self._fullscreen
        return self.get_screen(True)





def get_screen():
    do_init()


    global _screen
    if _screen is None:
        _screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
    return _screen

def get_screen_nes():
    print("pygame init")
    do_init()

    global _screen
    # https://stackoverflow.com/questions/68364418/pygame-weird-effects-on-the-screen-segmentation-fault-and-crash
    if os.environ.get('FULLSCREEN') == '1':
        _screen = pygame.display.set_mode((SCREEN_WIDTH_NES, SCREEN_HEIGHT_NES), 
                                        pygame.FULLSCREEN | pygame.SCALED

                                        )
    else:
        _screen = pygame.display.set_mode((SCREEN_WIDTH_NES, SCREEN_HEIGHT_NES), 
                                        pygame.RESIZABLE | pygame.SCALED

                                        )
    
    return _screen

# https://stackoverflow.com/questions/34466027/what-is-conftest-py-for-in-pytest

# for some reason it seems like this wasn't being called.
# not calling pygame.init can lead to a segmentation fault that is hard to debug
# def pytest_runtest_setup():
#     print("pygame init")
#     pygame.init()
#     pygame.mixer.init()
#     # screen = get_screen()
