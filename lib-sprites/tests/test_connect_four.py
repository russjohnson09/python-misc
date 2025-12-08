

from lib_sprites import ShipSprite, BeeSprite, ShrimpSprite, ShipExplosion, WhitePawn, \
    ChessBoard, WhiteKing, BlackKing, WhiteQueen, Windows31Mouse, OctopusBattery, ConnectFourBoard, ConnectFourNumbers
import pygame

from .conftest import get_screen_nes as get_screen
FILL = (5, 5, 5)
FILL = (15, 15, 15)
FILL = (100, 100, 100)


# https://en.wikipedia.org/wiki/PlayStation_technical_specifications
# SCREEN_WIDTH = 640
# SCREEN_HEIGHT = 480

# 7 columns and 6 rows
# chess board is 8 by 8

# I need circles and a way to identify which column the player is dropping their piece
# lib-sprites\tests\test_mouse.py
# first off circle sprites

# red pacman ghost and pacman.

def test_main():
    # galaga_spritesheet = GalagaSpritesheet()
    # galaga_spritesheet2 = GalagaSpritesheet()

    screen = get_screen()



    clock = pygame.time.Clock()

    bg_sprites =  pygame.sprite.Group()
    column_numbers =  pygame.sprite.Group()

    # TODO have ConnectFourBoard handle the top numbers
    board = ConnectFourBoard()
    one = ConnectFourNumbers(ConnectFourNumbers.ONE)
    two = ConnectFourNumbers(ConnectFourNumbers.TWO)
    three = ConnectFourNumbers(ConnectFourNumbers.THREE)
    four = ConnectFourNumbers(ConnectFourNumbers.FOUR)
    five = ConnectFourNumbers(ConnectFourNumbers.FIVE)
    six = ConnectFourNumbers(ConnectFourNumbers.SIX)
    seven = ConnectFourNumbers(ConnectFourNumbers.SEVEN)

    board.rect.x = 0
    board.rect.y = 16
    
    number_padding = 24
    number_y_pos = 5
    number_x_pos = 20
    one.rect.topleft = (number_x_pos + 0,number_y_pos)
    two.rect.topleft = (number_x_pos + 1 * number_padding,number_y_pos)
    three.rect.topleft =  (number_x_pos + 2 * number_padding,number_y_pos)
    four.rect.topleft =  (number_x_pos+ 3 * number_padding,number_y_pos)
    five.rect.topleft =  (number_x_pos+ 4 * number_padding,number_y_pos)
    six.rect.topleft =  (number_x_pos+ 5 * number_padding,number_y_pos)
    seven.rect.topleft =  (number_x_pos+ 6 * number_padding,number_y_pos)

    bg_sprites.add(board)

    column_numbers.add(one)
    column_numbers.add(two)
    column_numbers.add(three)
    column_numbers.add(four)
    column_numbers.add(five)
    column_numbers.add(six)
    column_numbers.add(seven)

    player_sprites =  pygame.sprite.Group()

    mouse_sprites =  pygame.sprite.Group()

    for row_idx in range(0,8):
        for col_idx in range(0,8):
            pawn3 = WhitePawn()
            pawn3 = WhiteKing()
            pawn3 = BlackKing()
            pawn3 = WhiteQueen()
            pawn3.rect.x = 66 + 48 * col_idx
            pawn3.rect.y = 34 + 48 * row_idx
            
            player_sprites.add(pawn3)

    mouse_sprite = OctopusBattery(OctopusBattery.OFFSET_BLUE)
    mouse_sprites.add(mouse_sprite)

    def _check_collisions():
        for player in player_sprites:
            player.is_highlighted = False
        for mouse_sprite in mouse_sprites:
            blocks_hit_list = pygame.sprite.spritecollide(mouse_sprite, player_sprites, dokill=False)

            if blocks_hit_list:
                # ps: pygame.sprite.Sprite = player_sprite
                # ps.kill()  # TODO replace with explosion
               
                for block in blocks_hit_list:
                    # mouse collision  <WhiteQueen Sprite(in 1 groups)>

                    # print("mouse collision ", block)
                    block.is_highlighted = True
                    # block.highlight()
                    break # only include the first collision

    i = 0
    while i < (60 * 10):
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        # pygame.event.set_grab(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self._quit = True
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.event.get()
        screen.fill(FILL)

        pos =  pygame.mouse.get_pos()
        mouse_sprite.rect.x = pos[0]
        mouse_sprite.rect.y = pos[1]
        

        bg_sprites.update()
        bg_sprites.draw(screen)

        player_sprites.update()
        player_sprites.draw(screen)

        column_numbers.update()
        column_numbers.draw(screen)

        mouse_sprites.update()
        mouse_sprites.draw(screen)

        _check_collisions()

        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass