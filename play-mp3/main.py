import pygame
import time


pygame.init()

# >   pygame.mixer.init()
# E   pygame.error: ALSA: Couldn't open audio device: No such file or directory
pygame.mixer.init()


file_path = "mmx5_stage_start.mp3"  # Replace with your actual file path
pygame.mixer.music.load(file_path)

pygame.mixer.set_reserved(1) 
pygame.mixer.set_reserved(2) 
pygame.mixer.set_reserved(3) 
# pygame.mixer.set_reserved(4) 
# pygame.mixer.set_reserved(5) 
# pygame.mixer.set_reserved(6) 
# pygame.mixer.set_reserved(7) 
# pygame.mixer.set_reserved(8) 
# pygame.mixer.set_reserved(9) 

print("loaded file")
pygame.mixer.music.play(0)  # Play once


# channel = pygame.mixer.Channel(0)
# channel.play(sound2)

sound_effect = pygame.mixer.Sound('snare-drum-3-94292.mp3')
# sound_effect2 = pygame.mixer.Sound('snare-drum-3-94292.mp3')
channel = pygame.mixer.Channel(0)

# unfortunately it looks like playback speed isn't included
i = 0
while i < 10:
    print("start")
    # sound_effect.play() # This is async??
    # channel.play(sound_effect)
    # pygame.mixer.init(frequency=mp3.info.sample_rate)

    channel = sound_effect.play()
    print(f"end effect channel: {channel}")
    i += 1
    while channel.get_busy(): # main mixer is not busy
        # sound_effect2.play() # This is async??
        pygame.time.wait(50)
    # pygame.time.wait(1000)
    # while pygame.mixer.get_busy(): # main mixer is not busy
    #     pygame.time.wait(1000)

print("playing")
while pygame.mixer.get_busy(): # main mixer is not busy
    pygame.time.wait(1000)

while pygame.mixer.music.get_busy(): # music mixer is busy
    pygame.time.wait(1000)



print("done")
# time.sleep(10)