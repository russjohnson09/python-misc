import pygame
import time
pygame.init()

pygame.mixer.music.load("twinkle-twinkle-little-star.mid")


print("loaded now playing")
pygame.mixer.music.play()


# while pygame.mixer.music.get_busy():
#     pygame.time.wait(1000)

while pygame.mixer.get_busy():
    pygame.time.wait(1000)
# time.sleep(10)