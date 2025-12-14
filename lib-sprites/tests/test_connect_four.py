

from lib_sprites import ShipSprite, BeeSprite, ShrimpSprite, ShipExplosion, WhitePawn, \
    ChessBoard, WhiteKing, BlackKing, WhiteQueen, Windows31Mouse, OctopusBattery, ConnectFourBoard, ConnectFourNumbers
import pygame
import os

from .conftest import get_screen_nes as get_screen

MAX_TEST_LOOPS = int(os.environ.get('MAX_TEST_LOOPS', (60 * 60)))

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

connect_four_board = [
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None]
]


# Blade Game Boy Color
# https://www.youtube.com/watch?v=KzDjQclLPnI
# https://www.spriters-resource.com/game_boy_gbc/blade/asset/92395/
def _check_collisions(just_clicked, mouse_sprite, column_numbers, player_turn):
    
    if not just_clicked:
        return False
    print("check collisions")
    print(just_clicked)
    just_clicked = False
    blocks_hit_list = pygame.sprite.spritecollide(mouse_sprite, column_numbers, dokill=False)
    if blocks_hit_list:
        hit_column = blocks_hit_list[0]

        col_idx = hit_column.idx
        print(col_idx)


        row_idx = 5

        found = False
        while row_idx > -1:
            item_val = connect_four_board[row_idx][col_idx]

            if item_val is None:
                connect_four_board[row_idx][col_idx] = player_turn
                found = True

                break
            
            row_idx -= 1

        print(connect_four_board, found)

        if found:
            return (row_idx, col_idx)
        return found

        # idx = 0
        # for column in column_numbers:
        #     print(hit_column, column)
        #     if hit_column == column:
        #         break
        #     idx += 1
        
        # print(idx)

        # for block in blocks_hit_list:
        #     print(block)
        #     # mouse collision  <WhiteQueen Sprite(in 1 groups)>

        #     # print("mouse collision ", block)
        #     # block.is_highlighted = True
        #     # block.highlight()
        #     break


def test_main():
    player_turn = 0

    # galaga_spritesheet = GalagaSpritesheet()
    # galaga_spritesheet2 = GalagaSpritesheet()

    screen = get_screen()



    clock = pygame.time.Clock()

    bg_sprites =  pygame.sprite.Group()
    column_numbers =  pygame.sprite.Group()
    pieces_on_board = pygame.sprite.Group()

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


    mouse_sprite = OctopusBattery(OctopusBattery.OFFSET_BLUE)
    mouse_sprites.add(mouse_sprite)


    just_clicked = False
    i = 0
    while i < MAX_TEST_LOOPS:
        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self._quit = True
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONUP:
                just_clicked = True
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

        pieces_on_board.update()
        pieces_on_board.draw(screen)

        found = _check_collisions(just_clicked,mouse_sprite,column_numbers, player_turn)

        if found:
            (row_idx, col_idx) = found

            if player_turn == 0:
                piece = OctopusBattery(OctopusBattery.OFFSET_BLUE)
                pieces_on_board.add(piece)
            else:
                piece = OctopusBattery(OctopusBattery.OFFSET_RED)
                pieces_on_board.add(piece)

            piece.rect.topleft = (col_idx * 24 + 14, row_idx * 24 + 20)

            
            player_turn += 1
            player_turn = player_turn % 2


            if player_turn == 0:
                mouse_sprite.update_image(OctopusBattery.OFFSET_BLUE)
            else:
                mouse_sprite.update_image(OctopusBattery.OFFSET_RED)
        just_clicked = False

        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass