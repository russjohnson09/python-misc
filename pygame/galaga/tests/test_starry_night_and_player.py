

from lib_sprites import GalagaBgSpriteGroup, ShipSprite, BeeSprite, Missle as MissleSprite
from lib_inputs import InputHandler
from lib_sounds import AndSoundBoard, FuturisticSoundboard, FUTURISTIC_SOUNDS

import pygame
import numpy
import os

# from .conftest import get_screen_nes as get_screen
from .conftest import pygame_handler
FILL = (5, 5, 5)
FILL = (15, 15, 15)

FPS = int(os.environ.get('FPS', '120'))
# FPS = int(os.environ.get('FPS', '300'))
MAX_TEST_LOOPS = int(os.environ.get('MAX_TEST_LOOPS', (60 * 60)))



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
        #         pygame.mixer.set_num_channels(1)
# https://stackoverflow.com/questions/38028970/how-to-assign-sounds-to-channels-in-pygame
        self._andSoundBoard = AndSoundBoard()

        self._future = FuturisticSoundboard()

        self._came: pygame.mixer.SoundType = pygame.mixer.Sound(self._andSoundBoard.get_sound_bytes("came"))

        print(FUTURISTIC_SOUNDS.MINI_LASER_ATTACK.value)
        self._missle =  self._future.get_sound(FUTURISTIC_SOUNDS.MINI_LASER_ATTACK)
        self._enemy_hit =  self._future.get_sound(FUTURISTIC_SOUNDS.MINI_HIT)

        
        pass

    def _play_sound(self, sound: pygame.mixer.SoundType):
        # channel: pygame.mixer.ChannelType = pygame.mixer.find_channel(True) # If no available channel find the one that has played the longest
        channel: pygame.mixer.ChannelType = pygame.mixer.find_channel(False)
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
        return self._ih.south_just_pressed or self._ih.west
    
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
    # def kill(self):
    #     print("kill")
        # replace with an explosion
        # play an explosion sound.

        # super().kill()

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

# namco that one spaceship game had some good parallax scrolling.
def test_starry_night():

    ih = InputHandler(pygame)

    screen = pygame_handler.get_screen()

    ih.joystick = pygame_handler.get_primary_joystick()

    sound_handler = SoundHandler()

    player = Player(input_handler=ih, sound_handler=sound_handler)



    player.topleft = (10, 480 - 50)


    player_attacks_group = player.attacks_group

    missle = Missle()
    missle.topleft = (50,50)
    player_attacks_group.add(missle)

    clock = pygame_handler.clock

    bg_sprite_group = GalagaBgSpriteGroup(FPS, screen)


    enemy_sprite_group = pygame.sprite.Group()


    bee_sprite = Bee(sound_handler=sound_handler)


    enemy_sprite_group.add(bee_sprite)


    def _check_collisions():
        for enemy in enemy_sprite_group:
            player_attacks_hit_list = pygame.sprite.spritecollide(enemy, player_attacks_group, dokill=True)#, dokill=False)
            if len(player_attacks_hit_list) > 0:
                print(player_attacks_hit_list)
                enemy.hit() # do_kill removes from the player_attacks_group but not the original sprite
        # for missle in player_attacks_group:
        #     # missle.kill()
        #     enemies_hit = pygame.sprite.spritecollide(missle, enemy_sprite_group, dokill=True)
        #     # if len(enemies_hit) > 0:
        #     #     print("kill missle enemy hit")
        #     #     missle.kill()


    estimated_delta = 60.0 / FPS

    i = 0
    
    def _is_finished(i):
        return pygame_handler.is_ci_test and i < MAX_TEST_LOOPS

    while not _is_finished(i):
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        ih.clear_just_pressed()
        for event in pygame.event.get():
            player.handle_event(event)
            if event.type == pygame.QUIT:
                # self._quit = True
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_f:
                    screen = pygame_handler.do_fullscreen()

        
        screen.fill((0,0,0,0))

        bg_sprite_group.update()
        bg_sprite_group.draw(screen) # instead of drawing to screen draw to subsurface and then position that?

        enemy_sprite_group.update()
        enemy_sprite_group.draw(screen)

        player_attacks_group.update()
        player_attacks_group.draw(screen)
        
        player.update_and_draw(estimated_delta, screen)


        # lib-sprites\tests\test_mouse.py
        _check_collisions()

        # player_group.draw(screen)
        # next draw player sprite

        pygame_handler.debug()


        pygame.display.flip()

        clock.tick(FPS)


        i += 1
