
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


class PygameHandler():

    _fullscreen = False
    _screen = None
    _size = (640, 480) # psx resolution

    def __init__(self, size = _size):
        self._size = size
        if self._screen is None:
            self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
        pass

    def get_size(self):
        return self._size

    def get_screen(self, refresh = False):
        if not self._screen or refresh:
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

_screen = None

def get_screen():
    print("get_screen")
    global _screen
    if _screen is None:
        _screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
    return _screen

def get_screen_nes():
    print("get_screen_nes")

    global _screen

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

def pytest_runtest_setup():
    print("pygame init")
    pygame.init()
    pygame.mixer.init()
    # screen = get_screen()
