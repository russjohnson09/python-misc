from lib_sprites import OctopusBattery, ConnectFourBoard as ConnectFourBoardSprite, ConnectFourNumbers

import pygame


FILL = (100, 100, 100)

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

# _root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))
# _default_asset_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))
# os.environ['ASSET_DIR'] = _default_asset_dir

def _init_pygame():
    pygame.init()
    pygame.mixer.init()
    # if _screen is None:
    _screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 
                                      pygame.RESIZABLE | pygame.SCALED

                                      )
    return _screen


def _has_win_horizontal(found, player, board):
    row_idx, col_idx = found

    count = 1
    while True:
        col_idx += 1
        if col_idx > 6:
            break
        print(row_idx, col_idx)
        piece = board[row_idx][col_idx]
        if piece != player:
            break
        count += 1

    row_idx, col_idx = found
    while True:
        col_idx -= 1
        if col_idx < 0:
            break
        piece = board[row_idx][col_idx]
        if piece != player:
            break
        count += 1


    return count == 4

def _has_win_vertical(found, player, board):

    row_idx, col_idx = found

    count = 1
    while True:
        row_idx += 1
        if row_idx > 5:
            break
        print(row_idx, col_idx)
        piece = board[row_idx][col_idx]
        if piece != player:
            break
        count += 1

    row_idx, col_idx = found
    while True:
        row_idx -= 1
        if row_idx < 0:
            break
        piece = board[row_idx][col_idx]
        if piece != player:
            break
        count += 1


    return count == 4


def _has_diag_top_left(found, player, board):
    count = 1

    row_idx, col_idx = found


    while True:
        row_idx += 1
        col_idx += 1

        if col_idx > 6 or row_idx > 5:
            break
        if player != board[row_idx][col_idx]:
            break
        count += 1

    row_idx, col_idx = found

    while True:
        row_idx += -1
        col_idx += -1
        if row_idx < 0 or col_idx < 0:
            break
        if player != board[row_idx][col_idx]:
            break
        count += 1

    return count == 4

def _has_diag_top_right(found, player, board):
    count = 1

    row_idx, col_idx = found


    while True:
        row_idx += -1
        col_idx += 1

        if col_idx > 6 or row_idx < 0:
            break
        if player != board[row_idx][col_idx]:
            break
        count += 1
        
    row_idx, col_idx = found

    while True:
        row_idx += 1
        col_idx += -1
        if row_idx > 5 or col_idx < 0:
            break
        if player != board[row_idx][col_idx]:
            break
        count += 1

    return count == 4

class ConnectFourBoard():

    winner = False
    player_turn = 0

    board = [
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None]
        ]
    
    just_clicked = False
    bg_sprites = None
    column_numbers = None
    # sprite group
    pieces_on_board = None
    mouse_sprite = None # OctopusBattery(OctopusBattery.OFFSET_BLUE)
    mouse_sprites =  None

    def _get_piece(self):
        if self.player_turn == 0:
            return OctopusBattery(OctopusBattery.OFFSET_BLUE)
        else:
            return OctopusBattery(OctopusBattery.OFFSET_RED)
    
    def _add_piece(self, found):
        (row_idx, col_idx) = found
        piece = self._get_piece()
        self.pieces_on_board.add(piece)

        piece.rect.topleft = (col_idx * 24 + 14, row_idx * 24 + 20)

        if found:
            self.winner = self._has_winner(found)

        player_turn = self.player_turn
        player_turn += 1
        self.player_turn = player_turn % 2

    def drop(self, col_idx):
        row_idx = 5

        while row_idx > -1:
            item_val = self.board[row_idx][col_idx]

            if item_val is None:
                self.board[row_idx][col_idx] = self.player_turn

                self._add_piece((row_idx, col_idx))
                return (row_idx, col_idx)
            
            row_idx -= 1
        return False

    def __init__(self):

        self.bg_sprites =  pygame.sprite.Group()
        self.column_numbers =  pygame.sprite.Group()
        # sprite group
        self.pieces_on_board = pygame.sprite.Group()
        self.mouse_sprite = None # OctopusBattery(OctopusBattery.OFFSET_BLUE)
        self.mouse_sprites =  pygame.sprite.Group()
        self.screen = _init_pygame()


        self.board = [
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None]
        ]


        self.mouse_sprite = OctopusBattery(OctopusBattery.OFFSET_BLUE)
        self.clock = pygame.time.Clock()


        self.mouse_sprites.add(self.mouse_sprite)

        bg_sprites = self.bg_sprites
        column_numbers = self.column_numbers
        board = ConnectFourBoardSprite()
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

    
    def _has_winner(self, found):
        return  _has_win_horizontal(found, self.player_turn, self.board) \
            or _has_win_vertical(found, self.player_turn, self.board) \
            or _has_diag_top_left(found, self.player_turn, self.board) \
            or _has_diag_top_right(found, self.player_turn, self.board)


    def _check_collisions(self):
        if self.winner is not False:
            return
        mouse_sprite = self.mouse_sprite
        column_numbers = self.column_numbers

        if not self.just_clicked:
            return False
        self.just_clicked = False
        blocks_hit_list = pygame.sprite.spritecollide(mouse_sprite, column_numbers, dokill=False)
        if blocks_hit_list:
            hit_column = blocks_hit_list[0]

            col_idx = hit_column.idx

            found = self.drop(col_idx)


            return found

    def loop(self):
        clock = self.clock
        screen = self.screen
        bg_sprites = self.bg_sprites
        column_numbers = self.column_numbers
        # player_sprites = self.player_sprites
        

        pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self._quit = True
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.just_clicked = True
        
        screen.fill(FILL)

        pos =  pygame.mouse.get_pos()
        self.mouse_sprite.rect.x = pos[0]
        self.mouse_sprite.rect.y = pos[1]
        

        bg_sprites.update()
        bg_sprites.draw(screen)

        column_numbers.update()
        column_numbers.draw(screen)

        self.mouse_sprites.update()
        self.mouse_sprites.draw(screen)

        self.pieces_on_board.update()
        self.pieces_on_board.draw(screen)

        found = self._check_collisions()

        if found:
            player_turn = self.player_turn

            if player_turn == 0:
                self.mouse_sprite.update_image(OctopusBattery.OFFSET_BLUE)
            else:
                self.mouse_sprite.update_image(OctopusBattery.OFFSET_RED)

        pygame.display.flip()
        clock.tick(60)
        return True