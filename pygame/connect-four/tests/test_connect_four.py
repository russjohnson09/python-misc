
from connect_four import ConnectFourBoard
from lib_sprites import OctopusBattery, ConnectFourBoard as ConnectFourBoardSprite, ConnectFourNumbers
import pygame

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



# Blade Game Boy Color
# https://www.youtube.com/watch?v=KzDjQclLPnI
# https://www.spriters-resource.com/game_boy_gbc/blade/asset/92395/

def test_main():

    connect_four_board = ConnectFourBoard()






    i = 0
    while i < (60 * 10):
        if not connect_four_board.loop():
            return
        i += 1
    # thread and call exit on connect_four_board
    # time.sleep(10)

    # connect_four_board.exit()
    pass