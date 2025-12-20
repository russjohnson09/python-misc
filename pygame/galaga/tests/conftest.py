
import pygame
import os


_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))
_default_asset_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))

os.environ['ASSET_DIR'] = os.environ.get('ASSET_DIR', _default_asset_dir)

# tests\test_starry_night_and_player.py Windows fatal exception: access violation

# Current thread 0x00001b68 (most recent call first):
#   File "C:\Users\russ\python-misc\lib-sprites\tests\conftest.py", line 72 in get_screen
#   File "C:\Users\russ\python-misc\lib-sprites\tests\conftest.py", line 78 in do_fullscreen
class PygameHandler():

    _fullscreen = False
    _screen = None
    size = (640, 480) # psx resolution

    _is_init = False

    clock = None

    def init_pygame(self):
        if self._is_init:
            return
        print('PygameHandler.init_pygame')

        self._is_init = True
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial" , 8 , bold = False)

    def __init__(self):
        pass


    def _fps_counter(self):
        fps = str(int(self.clock.get_fps()))

        fps_t = self.font.render(fps , 1, pygame.Color("RED"))

        self._screen.blit(fps_t,(0,0))

    def debug(self):
        self._fps_counter()



# https://github.com/pygame-community/pygame-ce/issues/2737
# If you're trying to run code that switches between SCALED and not-scaled, I think it would work to quit and re-initialize the video system while doing it. pygame.display.quit() and pygame.display.init(). Haven't tested though.
# I cannot seem to reproduce this on Ubuntu, perhaps this is a windows only issue
# This is in a whole stream of renderer semantics issues, and all the earliest reports were on Linux, so that's surprising. Are you using an old system SDL? It's an SDL version thing.
    def get_screen(self, refresh = False):
        if not self._is_init:
            self.init_pygame()
        if not self._screen or refresh: # I'm not experiencing a segmentation fault but running these in github it seems like display.set_mode should only run once?
            
            if self._screen:
                print('reinit display')
                pygame.display.quit()
                pygame.display.init()
            
            if self._fullscreen:
                self._screen = pygame.display.set_mode(self.size, 
                pygame.FULLSCREEN | pygame.SCALED)
            else:
                self._screen = pygame.display.set_mode(self.size, 
                pygame.RESIZABLE | pygame.SCALED)
        return self._screen

    def do_fullscreen(self):
        self._fullscreen = not self._fullscreen
        return self.get_screen(True)



def get_screen():
    pygame_handler.get_screen()

# https://stackoverflow.com/questions/34466027/what-is-conftest-py-for-in-pytest

pygame_handler = PygameHandler()

def pytest_runtest_setup():
    pygame_handler.init_pygame()

