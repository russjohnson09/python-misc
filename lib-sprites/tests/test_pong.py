

from lib_sprites import PongGhostBall, PongPaddle
import pygame
import numpy

from .conftest import get_screen_nes as get_screen
FILL = (5, 5, 5)
FILL = (15, 15, 15)
# FILL = (100, 100, 100)

FPS = 60
# FPS = 100

# Single server. As the server I can see both players but can't control them.
# Each player / client sends tcp requests to update their locations and that applies to their paddle.


def fps_counter(screen, clock, font):
    fps = str(clock.get_fps())
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))

# FULLSCREEN=1 uv run pytest tests/test_pong.py 
def test_pong():
    player_turn = 0

    # galaga_spritesheet = GalagaSpritesheet()
    # galaga_spritesheet2 = GalagaSpritesheet()

    screen = get_screen()
    font = pygame.font.SysFont("Arial" , 18 , bold = True)



    # score counter.

    clock = pygame.time.Clock()

    #multiple balls?
    ball_sprites =  pygame.sprite.Group()

    player_sprites = pygame.sprite.Group()

    ball = PongGhostBall()
    ball_sprites.add(ball)

    ball.velocity = numpy.array([0.23,0.23])
    ball.velocity = numpy.array([1.23,1.23])

    # server can update the player position if has focus and up down / w s.


    i = 0
    while i < (60 * 10):
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self._quit = True
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     just_clicked = True
        pygame.event.get()
        screen.fill(FILL)

        pos =  pygame.mouse.get_pos()

        # mouse player can move in any direction
        # keyboard player can only move up and down.

        # mouse_sprite.rect.x = pos[0]
        # mouse_sprite.rect.y = pos[1]
        

        # bg_sprites.update()
        # bg_sprites.draw(screen)

        player_sprites.update()
        player_sprites.draw(screen)

        ball_sprites.update()
        ball_sprites.draw(screen)

        # column_numbers.update()
        # column_numbers.draw(screen)

        # mouse_sprites.update()
        # mouse_sprites.draw(screen)

        # pieces_on_board.update()
        # pieces_on_board.draw(screen)

        # found = _check_collisions(just_clicked,mouse_sprite,column_numbers, player_turn)

        
        fps_counter(screen, clock, font)
        
        pygame.display.flip()




# https://www.reddit.com/r/pygame/comments/k7677j/how_to_make_a_basic_deltatime_system/
        clock.tick(FPS)
        # clock.tick()

        i += 1
    pass



    pass