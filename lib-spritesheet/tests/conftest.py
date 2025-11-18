
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# SCREEN_WIDTH = SCREEN_WIDTH / 4
# SCREEN_HEIGHT = SCREEN_HEIGHT / 4

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
