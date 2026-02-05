

from lib_sprites import GalagaBgSpriteGroup, ShipSprite, BeeSprite, Missle as MissleSprite
from lib_inputs import InputHandler
from lib_sounds import AndSoundBoard, FuturisticSoundboard, FUTURISTIC_SOUNDS

import datetime
import time
import pygame
import numpy
import os

#   C:\Users\russj\dev\python-misc\pygame\galaga\tests\test_starry_night_and_player.py:237: DeprecationWarning: Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread. To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.

# https://imageio.readthedocs.io/en/stable/examples.html#optimizing-a-gif-using-pygifsicle
# import imageio
import imageio.v2 as imageio

# from .conftest import get_screen_nes as get_screen
from .conftest import pygame_handler
FILL = (5, 5, 5)
FILL = (15, 15, 15)

# FPS = int(os.environ.get('FPS', '60'))
FPS = int(os.environ.get('FPS', '120'))


MAX_TEST_LOOPS = int(os.environ.get('MAX_TEST_LOOPS', (60 * 60)))
ALLOW_AUTOFIRE = os.environ.get('ALLOW_AUTOFIRE', '0') == '1'
RECORDING = os.environ.get('RECORDING', '0') == '1'
MAX_BEE_COUNT = int(os.environ.get('MAX_BEE_COUNT', '-1'))

start_ms = int(1000 * time.time())

recording_dir = f"recording/{start_ms}" #.replace(' ', '-')
recording_dir = os.path.abspath(recording_dir)
if not os.path.exists(recording_dir):
    os.makedirs(recording_dir)
# Single server. As the server I can see both players but can't control them.
# Each player / client sends tcp requests to update their locations and that applies to their paddle.




# https://github.com/SuperNReal/jumpy/blob/main/my_code.py


# https://stackoverflow.com/questions/39712307/is-there-a-way-with-pygame-to-get-keyboard-input-when-the-window-is-minimized
# 

class SoundHandler():
    """Limit the number of channels. If one channel is used up the sound effect is cut short."""

    _came: pygame.mixer.SoundType
    _missle: pygame.mixer.SoundType

    def __init__(self):
        pygame.mixer.set_num_channels(3)
# https://stackoverflow.com/questions/38028970/how-to-assign-sounds-to-channels-in-pygame
        self._andSoundBoard = AndSoundBoard()

        self._future = FuturisticSoundboard()

        self._came: pygame.mixer.SoundType = pygame.mixer.Sound(self._andSoundBoard.get_sound_bytes("came"))

        if os.environ.get('IS_CI_TEST') == '1':
            self._missle =  self._came
            self._enemy_hit =  self._came
        else:
            self._missle =  self._future.get_sound(FUTURISTIC_SOUNDS.MINI_LASER_ATTACK)
            self._enemy_hit =  self._future.get_sound(FUTURISTIC_SOUNDS.MINI_HIT)

        
        pass

    def _play_sound(self, sound: pygame.mixer.SoundType):
        channel: pygame.mixer.ChannelType = pygame.mixer.find_channel(True) # If no available channel find the one that has played the longest
        # channel: pygame.mixer.ChannelType = pygame.mixer.find_channel(False)
        if channel is None:
            return
        channel.play(sound)

    def play_missle_shot(self):

        # self._play_sound(self._came)

        self._play_sound(self._missle)

        pass

    def play_explosion(self):
        
        print("play_explosion")
        self._play_sound(self._enemy_hit)

        pass


class PlayerInput():

    def __init__(self, ih: InputHandler):
        self._ih = ih
        pass

    def handle_event(self, event):
        self._ih.handle_event(event)

    def fire_just_pressed(self):
        return self._ih.south_just_pressed or (self._ih.west and ALLOW_AUTOFIRE)
    
    def get_direction(self):
        x = 0
        y = 0
        if self._ih.left:
            x = -1
        elif self._ih.right:
            x = 1
        
        return (x,y)

class Player():

    sound_handler: SoundHandler
    attacks_group: pygame.sprite.Group = None # pygame.sprite.Group()
    speed = 5.0

    topleft = (0,0)

    def __init__(self,
    input_handler,
    sound_handler

    ):
        self.attacks_group = pygame.sprite.Group()
        self.topleft = (0,0)
        self.sound_handler = sound_handler
        self._input = PlayerInput(input_handler)
        self._player_sprite = ShipSprite(2)
        self._player_group = pygame.sprite.Group()

        self._player_group.add(self._player_sprite)

        rect: pygame.rect.RectType = self._player_sprite.rect

        self._x_offset_center = int((rect.width / 2) - 4)

        pass

    def _spawn_attack(self):
        missle = Missle()

        missle.topleft = (self.topleft[0] + self._x_offset_center,
                          self.topleft[1])
        self.attacks_group.add(missle)

        self.sound_handler.play_missle_shot()
    
       

    def handle_event(self, event):
        self._input.handle_event(event)

    def update_and_draw(self, delta, screen):
        """
        delta: time in seconds assuming that the FPS is capped out, so if you don't reach the max framerate things are going to slow down for you.
        """
        self._player_sprite.topleft = self.topleft

        direction = self._input.get_direction()
        self.topleft = (
            self.topleft[0] + (direction[0] * self.speed * delta), 
            self.topleft[1] + (direction[1] * self.speed * delta), 
        )


        self._player_group.update()
        self._player_group.draw(screen)


        if self._input.fire_just_pressed():
            self._spawn_attack()
        pass

class Bee(BeeSprite):

    sound_handler: SoundHandler
    velocity = (0.5,0.5)

    def __init__(self, scale = 2, FPS = 120, sound_handler = None):
        self.sound_handler = sound_handler
        super().__init__(scale=scale, FPS=FPS)

    def update(self):

        if self.topleft[0] > 300:
            self.velocity = (-0.5,-0.25)
        elif self.topleft[0] < 10:
            self.velocity = (0.5,0.25)

        self.topleft = (self.topleft[0] + self.velocity[0], self.topleft[1] + self.velocity[1])

        super().update()

    def hit(self):
        if self.sound_handler:
            self.sound_handler.play_explosion()
        self.kill()
        pass

class Missle(MissleSprite):

    velocity = (0,-10)

    def __init__(self, scale = 2, FPS = 120):
        super().__init__(scale=scale, FPS=FPS)

    def update(self):
        self.topleft = (self.topleft[0] + self.velocity[0], self.topleft[1] + self.velocity[1])
        if self.topleft[1] < 0:
            # print("kill missle")
            # https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.kill
            self.kill()
        super().update()

def test_starry_night():
    recorded_files_orig = _starry_night_main()
    # png_filenames = [os.path.abspath(os.path.join(recording_dir, f)) for f in os.listdir(recording_dir) if os.path.isfile(os.path.join(recording_dir, f))]

    recorded_files = []
    for i in range(0,len(recorded_files_orig)):
        recorded_files.append(recorded_files_orig[i])

        # if i % 2 == 0:
            # recorded_files.append(recorded_files_orig[i])
    if len(recorded_files) == 0:
        return
    # print("png recording to gif", recording_dir, png_filenames)
    images = []
    for filename in recorded_files:
        images.append(imageio.imread(filename))

    # tests/test_starry_night_and_player.py::test_starry_night
#   C:\Users\russj\dev\python-misc\pygame\galaga\.venv\Lib\site-packages\imageio\plugins\pillow.py:410: DeprecationWarning: The keyword `fps` is no longer supported. Use `duration`(in ms) instead, e.g. `fps=50` == `duration=20` (1000 * 1/50).
    duration = int(1000 * (1.0/FPS))
    print('duration', duration)
    # imageio.mimsave(f'recording/{start_ms}.gif', images, duration=duration)
    # imageio.mimsave(f'recording/{start_ms}.gif', images, duration=(10))
    # imageio.mimsave(f'recording/{start_ms}.gif', images, duration=duration)
    # imageio.mimsave(f'recording/{start_ms}.gif', images, fps=FPS)

    # duration=[1000, 3000, 1000], loop=0
    # imageio.mimsave(f'recording/{start_ms}.gif', images, duration=10)

    # duration = [10 for f in recorded_files]
    duration = [20 for f in recorded_files]
    # print(duration)
# https://imageio.readthedocs.io/en/v2.9.0/userapi.html#imageio.mimwrite
    imageio.mimwrite(f'recording/{start_ms}.gif', images, 
                     duration=duration, 
                     
                     loop=0)



def _starry_night_main():

    recorded_files = []

# namco that one spaceship game had some good parallax scrolling.

    ih = InputHandler(pygame)

    screen = pygame_handler.get_screen()

    ih.joystick = pygame_handler.get_primary_joystick()

    sound_handler = SoundHandler()







    missle = Missle()
    missle.topleft = (50,50)
    clock = pygame_handler.clock

    bg_sprite_group = GalagaBgSpriteGroup(FPS, screen)


    enemy_sprite_group = pygame.sprite.Group()




    def _check_collisions():
        pass


    estimated_delta = 60.0 / FPS

    i = 0
    
    def _is_finished(i):
        return pygame_handler.is_ci_test and i > MAX_TEST_LOOPS

    while not _is_finished(i):
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        ih.clear_just_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self._quit = True
                return recorded_files
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return recorded_files
                elif event.key == pygame.K_f:
                    screen = pygame_handler.do_fullscreen()

        
        screen.fill((0,0,0,0))

        bg_sprite_group.update()
        bg_sprite_group.draw(screen) # instead of drawing to screen draw to subsurface and then position that?

        enemy_sprite_group.update()
        enemy_sprite_group.draw(screen)


        # lib-sprites\tests\test_mouse.py
        _check_collisions()

        # player_group.draw(screen)
        # next draw player sprite

        # if recording save a png


        # RECORDING=1 uv run pytest ./tests/test_starry_night.py -s
        def _save_surface(screen: pygame.surface.Surface, filename):
            # https://www.pygame.org/docs/ref/image.html#pygame.image.save

            recorded_files.append(filename)
            pygame.image.save(screen, filename)




        

        # if i == 0:
        #     _save_surface(screen=screen, filename="test.bmp")

        #     # recording_dir = f"recording/{datetime.datetime.now()}".replace(' ', '-')
        #     # recording_dir = f"recording/{int(1000 * time.time())}" #.replace(' ', '-')

        #     # _save_surface(screen=screen, filename=f"recording/test.bmp")
        #     # _save_surface(screen=screen, filename=f"{recording_dir}/test.bmp")

        #     pass


        if RECORDING:
            # _save_surface(screen=screen, filename=f"{recording_dir}/{i}.bmp")
            _save_surface(screen=screen, filename=f"{recording_dir}/{i}.png")





        if os.environ.get('DEBUG_FPS', '0') == '1':
            pygame_handler.debug()


        pygame.display.flip()

        clock.tick(FPS)


        i += 1


    return recorded_files