# https://stackoverflow.com/questions/45745810/play-square-wave-scipy-and-pyaudio

# https://stackoverflow.com/questions/63980583/how-can-i-play-a-sine-square-wave-using-pygame
import pygame
import numpy as np

import time

pygame.mixer.init(size=32)

FREQ = 440

buffer = np.sin(2 * np.pi * np.arange(44100) * FREQ / 44100).astype(np.float32)
print(buffer)
sound = pygame.mixer.Sound(buffer)


# https://stackoverflow.com/questions/47704052/music21-to-get-sample-of-time-and-frequencies-in-txt-or-csv
sound.play(0) # This is async

# pygame.time.wait(int(sound.get_length() * 1000))
# time.sleep(10) # worse way to sleep not as accurate.


# https://github.com/vishnubob/python-midi

while pygame.mixer.get_busy():
    pygame.time.wait(1000)