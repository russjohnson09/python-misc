

from lib_sprites import GalagaBgSpriteGroup, ShipSprite, BeeSprite
from lib_inputs import InputHandler
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


class PlayerInput():

    def __init__(self, ih: InputHandler):
        self._ih = ih
        pass

    def handle_event(self, event):
        self._ih.handle_event(event)
    
    def get_direction(self):
        x = 0
        y = 0
        if self._ih.left:
            x = -1
        elif self._ih.right:
            x = 1
        
        return (x,y)

class Player():


    speed = 5.0

    topleft = (0,0)

    def __init__(self,
    ih

    ):
        self.topleft = (0,0)
        self._input = PlayerInput(ih)
        self._player_sprite = ShipSprite(2)
        self._player_group = pygame.sprite.Group()

        self._player_group.add(self._player_sprite)

        pass
    
    def handle_event(self, event):
        return self._input.handle_event(event)

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
        pass


# namco that one spaceship game had some good parallax scrolling.
def test_starry_night():

    ih = InputHandler(pygame)

    screen = pygame_handler.get_screen()

    ih.joystick = pygame_handler.get_primary_joystick()

    player = Player(ih)

    player.topleft = (10, 480 - 50)


    player_attacks_group = pygame.sprite.Group()



    clock = pygame_handler.clock

    bg_sprite_group = GalagaBgSpriteGroup(FPS, screen)


    enemy_sprite_group = pygame.sprite.Group()


    bee_sprite = BeeSprite()
    enemy_sprite_group.add(bee_sprite)



    estimated_delta = 60.0 / FPS

    i = 0
    while i < MAX_TEST_LOOPS:
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

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
        
        player.update_and_draw(estimated_delta, screen)

        # player_group.draw(screen)
        # next draw player sprite

        pygame_handler.debug()


        pygame.display.flip()

        clock.tick(FPS)
        i += 1
