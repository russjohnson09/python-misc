

from lib_sprites import ShipSprite, BeeSprite, ShrimpSprite, ShipExplosion, WhitePawn, ChessBoard, WhiteKing, BlackKing, WhiteQueen
import pygame

from .conftest import get_screen
FILL = (5, 5, 5)


# https://en.wikipedia.org/wiki/PlayStation_technical_specifications
# SCREEN_WIDTH = 640
# SCREEN_HEIGHT = 480
def test_main():
    # galaga_spritesheet = GalagaSpritesheet()
    # galaga_spritesheet2 = GalagaSpritesheet()

    screen = get_screen()

    clock = pygame.time.Clock()

    bg_sprites =  pygame.sprite.Group()
    board = ChessBoard()

    bg_sprites.add(board)

    player_sprites =  pygame.sprite.Group()

    # pawn1 = WhitePawn()
    # pawn1.rect.x = 65
    # pawn1.rect.y = 34

    # player_sprites.add(pawn1)

    # pawn2 = WhitePawn()
    # pawn2.rect.x = 65 + 50
    # pawn2.rect.y = 34 + 0
    
    # player_sprites.add(pawn2)


    # pawn3 = WhitePawn()
    # pawn3.rect.x = 65 + 50 * 2
    # pawn3.rect.y = 34 + 0
    
    # player_sprites.add(pawn3)

    for row_idx in range(0,8):
        for col_idx in range(0,8):
            pawn3 = WhitePawn()
            pawn3 = WhiteKing()
            pawn3 = BlackKing()
            pawn3 = WhiteQueen()
            pawn3.rect.x = 66 + 48 * col_idx
            pawn3.rect.y = 34 + 48 * row_idx
            
            player_sprites.add(pawn3)



    i = 0
    while i < (60 * 10):
        pygame.event.get()
        screen.fill(FILL)

        bg_sprites.update()
        bg_sprites.draw(screen)

        player_sprites.update()
        player_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass