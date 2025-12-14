

from lib_sprites import PongGhostBall, PongPaddle
import pygame
import numpy

from .conftest import get_screen_nes as get_screen
FILL = (5, 5, 5)
FILL = (15, 15, 15)
# FILL = (100, 100, 100)

# FPS = 60
# FPS = 100
# https://blubberquark.tumblr.com/post/185013752945/using-moderngl-for-post-processing-shaders-with

# https://www.reddit.com/r/Pacman/comments/1cg2ogp/does_anyone_know_the_pixel_per_frame_speeds_of/
# All speeds are measured in pixels/frame unless stated otherwise. Pac-Man runs at 60.606061 Hz. 
# The game board is 224 pixels wide and 248 pixels tall, and is made up of square tiles that are 8 pixels across. 
# Importantly, Pac-Man stops moving for 1 frame to eat a dot, meaning he moves roughly* 10% slower while eating. 
# Also to note is that Pac-Man can physically cut corners through input buffering while ghosts cannot. 
# This makes him appear to corner faster, but his movement speed actually does not increase, 
# he is just traveling less distance. 
# I am not sure how much faster cornering makes him as a relative percentage, nor exactly how many pixels cornering shaves off. My apologies.




FPS = 120

# Single server. As the server I can see both players but can't control them.
# Each player / client sends tcp requests to update their locations and that applies to their paddle.


def fps_counter(screen, clock, font):
    # fps = str(clock.get_fps())
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))

# FULLSCREEN=1 uv run pytest tests/test_pong.py 
def test_pong():
    # galaga_spritesheet = GalagaSpritesheet()
    # galaga_spritesheet2 = GalagaSpritesheet()

    screen = get_screen()
    font = pygame.font.SysFont("Arial" , 8 , bold = False)

    # score counter.

    clock = pygame.time.Clock()

    #multiple balls?
    ball_sprites =  pygame.sprite.Group()

    player_sprites = pygame.sprite.Group()
    paddle = PongPaddle()
    player_sprites.add(paddle)

    ball = PongGhostBall()
    ball_sprites.add(ball)

    ball.velocity = numpy.array([0.23,0.23])
    ball.velocity = numpy.array([1.23,1.23])

    # server can update the player position if has focus and up down / w s.


    i = 0
    while i < (60 * 50):
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
        # pygame.event.get()
        screen.fill(FILL)

        pos =  pygame.mouse.get_pos()

        # paddle.topleft = paddle.pos
        paddle.rect.topleft = pos
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

        for ball_sprite in ball_sprites:

            players_hit = pygame.sprite.spritecollide(ball_sprite, player_sprites, dokill=False)
            for player in players_hit:
                ball_sprite.hit_paddle(player)


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