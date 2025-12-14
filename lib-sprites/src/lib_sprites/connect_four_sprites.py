import os
import pygame



_default_asset_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../assets'))

ASSET_DIR = os.environ.get('ASSET_DIR', _default_asset_dir)


def _image_at(spritesheet, rectangle):
    # # Load a specific image from a specific rectangle
    # def image_at(self, rectangle):
    "Loads image from x,y,x+offset,y+offset"
    rect = pygame.Rect(rectangle)

    return spritesheet.subsurface(rect)

_chess_spritesheet = None
def _get_chessboard_spritesheet():
    global _chess_spritesheet
    filename = os.path.join(ASSET_DIR, 'NES - The Chessmaster - Miscellaneous - Chess Board.png')

    if _chess_spritesheet is None:
        _chess_spritesheet = pygame.image.load(filename).convert_alpha()

    return _chess_spritesheet


class ChessSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.spritesheet = _get_chessboard_spritesheet()


class ConnectFourBoard(ChessSprite):

    def __init__(self):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.spritesheet

        self.image = _image_at(spritesheet,(23,65,177,144))

        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

class ConnectFourNumbers(ChessSprite):

    ONE = (25,194,6,6)
    TWO = (25,170,6,6)
    THREE = (25,146,6,6)
    FOUR = (25,122,6,6)
    FIVE = (25,98,6,6)
    SIX = (25,74,6,6)
    SEVEN = (25,50,6,6)


    idx_array = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN]

    idx = 0



    def __init__(self, rect = ONE):
        # I should pull in some singleton class for sprite management here.
        super().__init__()

        spritesheet = self.spritesheet
        self.image = _image_at(spritesheet,rect)

        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

        self.idx = 0
        for rect_item in self.idx_array:
            if rect_item == rect:
                break
            self.idx += 1
