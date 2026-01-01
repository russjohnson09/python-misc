
import pygame
import os

_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))
_default_asset_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))

os.environ['ASSET_DIR'] = _default_asset_dir



class PygameHandler():
    _joysticks: list[pygame.joystick.JoystickType] = []
    _primary_joystick: pygame.joystick.JoystickType = None

    debug_mode = True

    quit = False

    FPS = 60

    FILL = (0,0,0)

    
    _screen = None

    _fullscreen = False
    
    size = (640, 480) # psx resolution

    def load_music(self, location):
        pygame.mixer.music.load(os.path.join(_default_asset_dir, location))

    def get_sound(self, location):

        return pygame.mixer.Sound(os.path.join(_default_asset_dir, location))

    def __init__(self, screen_size = size):
        self.size = screen_size

        pygame.init()

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial" , 8 , bold = False)

        pass

    def _fps_counter(self):
        # fps = str(clock.get_fps())
        fps = str(int(self.clock.get_fps()))

        fps_t = self.font.render(fps , 1, pygame.Color("RED"))

        self.screen.blit(fps_t,(0,0))


    def get_primary_joystick(self):
        # this fetching of joysticks could probably be handled by some util in lib_inputs as well.
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
    
    def clock_tick(self):
        self.clock.tick(self.FPS)

    def display_flip(self):
        if self.debug_mode:
            self._debug()

        pygame.display.flip()

    def fill(self):
        self.screen.fill(self.FILL)

    def hide_mouse(self):
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

    def _basic_event_handler(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
            return
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
                return
            if event.key == pygame.K_f: 
                self._screen = self.do_fullscreen()
        
    def get_event(self):
        # event = iter(pygame.event.get())

        for event in pygame.event.get():
            self._basic_event_handler(event)
            yield event

        return None


    def _debug(self):
        self._fps_counter()


    @property
    def screen(self):

        return self.get_screen()

# https://github.com/pygame-community/pygame-ce/issues/2737
# If you're trying to run code that switches between SCALED and not-scaled, I think it would work to quit and re-initialize the video system while doing it. pygame.display.quit() and pygame.display.init(). Haven't tested though.
# I cannot seem to reproduce this on Ubuntu, perhaps this is a windows only issue
# This is in a whole stream of renderer semantics issues, and all the earliest reports were on Linux, so that's surprising. Are you using an old system SDL? It's an SDL version thing.
    def get_screen(self, refresh = False):
        _screen = self._screen

        if not self._screen or refresh: # I'm not experiencing a segmentation fault but running these in github it seems like display.set_mode should only run once?
            
            if self._screen:
                print('reinit')
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

