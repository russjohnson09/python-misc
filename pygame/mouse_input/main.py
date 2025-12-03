import pygame
import os
_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../'))
_default_asset_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))

os.environ['ASSET_DIR'] = _default_asset_dir



from lib_sprites import ShipSprite, BeeSprite, ShrimpSprite, ShipExplosion, WhitePawn, ChessBoard, WhiteKing, BlackKing, WhiteQueen


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WHITE = (255,255,255)
FILL = (5, 5, 5)


# pygame.mixer.init defaults
frequency: int = 44100

# The size argument represents how many bits are used for each audio sample. If the value is negative then signed sample values will be used. Positive values mean unsigned audio samples will be used. An invalid value raises an exception.
size: int = -16
channels: int = 2
buffer: int = 512



class Game():

    _loop_count_keypress = 0

    _word = ''
    _mouse_position = (0,0)

    _quit = False

    _clock: pygame.time.Clock
    # _screen: pygame.display
    _screen: pygame.Surface

    _font: pygame.font.SysFont

    player_sprites =  pygame.sprite.Group()
    # enemy_sprites = pygame.sprite.Group()
    # non_collision_sprites = pygame.sprite.Group()

    player1: ShipSprite


    def _pygame_init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        # pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        pygame.event.set_grab(True)


    def __init__(self, fps = 60):
        self._pygame_init()
        self.fps = fps
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
        self._clock = pygame.time.Clock()

        # self._font = pygame.font.SysFont(None, 30, bold=True)
        self._font = pygame.font.SysFont(None, 180, bold=True)

        # self._font = pygame.font.SysFont('Arial', 30, bold=True)
        self.player1 = WhitePawn()

        self.player_sprites.add(self.player1)


        pass

    def start(self):
        i = 0
        while i < (60 * 15):
            self.loop()
            i += 1
            if self._quit:
                return
            

    def _handle_mouse_motion_event(self, event: pygame.event):

        # mouse moved <Event(1024-MouseMotion {'pos': (292, 194), 'rel': (22, -5), 'buttons': (0, 0, 0), 'touch': False, 'window': None})>
        # print("mouse moved", event)
        # print("mouse position", pygame.mouse.get_pos())
        # print("event", event.pos)
        # print("event", event.rel)

        self._mouse_position = event.pos


        # self._mouse_position =

    # https://v1.windows93.net/
    def handle_event(self, event: pygame.event):
        pygame.event.set_grab(True)

        if event.type == pygame.MOUSEMOTION:
            return self._handle_mouse_motion_event(event)
        elif event.type == pygame.QUIT:
            self._quit = True
            return
        elif event.type == pygame.KEYDOWN:
            print('keydown', event.key)
            self._loop_count_keypress = 0
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                self._word += chr(event.key)
                self._word = self._word.upper()
            elif event.key == pygame.K_c:
                # https://www.pygame.org/docs/ref/key.html#module-pygame.key
                # pygame.key.get_pressed()
                # self._word += event.event_name
                self._word += chr(event.key)
                self._word = self._word.upper()
            elif event.key == pygame.K_ESCAPE:
                self._quit = True
                return
        #     elif event.key == pygame.K_r:
        #         andSoundBoard.play('right')
        #     elif event.key == pygame.K_w:
        #         andSoundBoard.play('wrong')
        # #     if event.key == pygame.K_RETURN:  # Check if Enter was pressed
        # #         print('play note')
        # #         piano.play_note(note='A4')

        return True
    

# https://www.reddit.com/r/pygame/comments/5p2icq/mouseget_rel_doesnt_work_with_set_grabtrue_and/
    def loop(self):
        pygame.event.set_grab(True)

        self._loop_count_keypress += 1

        if self._loop_count_keypress > 30: # .5 seconds for 60 FPS
            self._word = ''
        
        for event in pygame.event.get():
            self.handle_event(event)


        self._screen.fill(FILL)

        if self._quit:
            return False



        # text_surface: pygame.Surface = self._font.render('Hello, Pygame!', True, WHITE)
        text_surface: pygame.Surface = self._font.render(self._word, True, WHITE)

        # https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
        # https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale
        # text_surface.transform.scale(text_surface, 10,10, text_surface)
        # https://www.pygame.org/docs/ref/transform.html#pygame.transform.smoothscale_by
        # text_surface = pygame.transform.smoothscale_by(text_surface, 0.2)
        text_surface = pygame.transform.smoothscale_by(text_surface, (0.2,0.2))

        text_surface2: pygame.Surface = self._font.render(str(self._mouse_position), True, WHITE)
        text_surface2 = pygame.transform.smoothscale_by(text_surface2, (0.2,0.2))

        x, y = (0,0)
        self._screen.blit(text_surface2, (x, y))   

    # https://www.youtube.com/watch?v=ndtFoWWBAoE
        x, y = (300,300)
        self._screen.blit(text_surface, (x, y))

        self.player1.rect.x = self._mouse_position[0]
        self.player1.rect.y = self._mouse_position[1]

        self.player_sprites.update()
        self.player_sprites.draw(self._screen)

        # update display
        pygame.display.flip()
        self._clock.tick(self.fps)

# uv run pytest tests/test_came.py
def main():
    game = Game()
    game.start()
