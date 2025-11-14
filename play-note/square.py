import numpy as np
from scipy import signal
import pygame

print('start')

exit(0)

# --- Configuration ---
sample_rate = 44100  # samples per second
duration = 2         # seconds
frequency = 440      # Hz (A4 note)
peak_amplitude = 0.5 # between 0 and 1, adjust for volume
duty_cycle = 0.5     # 0.5 for a perfect square wave (50% on, 50% off)

# --- Generate the square wave ---
# Create a time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate the square wave using scipy.signal.square
# The output will be between -1 and 1
square_wave = signal.square(2 * np.pi * frequency * t, duty=duty_cycle)

# Scale the amplitude and convert to 16-bit integers for Pygame
# Pygame's sndarray expects 16-bit signed integers
audio_data = (square_wave * 32767 * peak_amplitude).astype(np.int16)

# --- Play the sound ---
pygame.mixer.init(sample_rate, -16, 1)  # Initialize mixer (frequency, bits, channels)
sound = pygame.sndarray.make_sound(audio_data)
sound.play()

# Keep the program running long enough for the sound to play
pygame.time.delay(int(duration * 1000))

# Clean up
pygame.quit()