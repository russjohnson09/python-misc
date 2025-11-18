
import pygame
import os


_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))
_default_asset_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))

os.environ['ASSET_DIR'] = _default_asset_dir

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

SCREEN_WIDTH = SCREEN_WIDTH / 4
SCREEN_HEIGHT = SCREEN_HEIGHT / 4

_screen = None

def get_screen():
    global _screen
    if _screen is None:
        _screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
    return _screen

# https://stackoverflow.com/questions/34466027/what-is-conftest-py-for-in-pytest

def pytest_runtest_setup():
    pygame.init()
    pygame.mixer.init()
    screen = get_screen()
