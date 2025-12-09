
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
