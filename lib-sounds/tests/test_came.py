

from lib_sounds import Came, AndSoundBoard
import pygame
import wave
import math

from .conftest import get_screen
FILL = (5, 5, 5)

# pygame.mixer.init defaults
frequency: int = 44100

# The size argument represents how many bits are used for each audio sample. If the value is negative then signed sample values will be used. Positive values mean unsigned audio samples will be used. An invalid value raises an exception.
size: int = -16
channels: int = 2
buffer: int = 512
# devicename: Optional[str] = None,
# allowedchanges: int = 5,

# https://www.pygame.org/wiki/SoundGeneration?action=view&id=14732
# https://stackoverflow.com/questions/7816294/simple-pygame-audio-at-a-frequency
def _save_sound(snd: pygame.mixer.SoundType):
        # create a sound from NumPy array of file
    # snd = pygame.mixer.Sound(my_sound_source)

    # open new wave file
    sfile = wave.open('pure_tone.wav', 'w')

    

    # pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

    # SAMPLINGFREQ 
    # set the parameters
    sfile.setframerate(frequency)
    sfile.setnchannels(channels)
    sfile.setsampwidth(2) # what is sample width?

    # write raw PyGame sound buffer to wave file
    # sfile.writeframesraw(snd.get_buffer().raw)
    raw: bytes = snd.get_raw()
    byte_array =  bytearray(raw)


    # 194 seconds at 44100 freq, size -16, 2 channels

    # 44100 * 194 = 8_555_400
    # 8_555_400 * 2 = 17_110_800
    # which is half of 34,280,736. 16 bits means 2 bytes. right??

    # https://stackoverflow.com/questions/46204077/determining-bit-depth-of-a-wav-file

    bytes_per_second = int(frequency * channels * abs(size / 8))

    # bytes_per_second=705600

    start_seconds = 5.282
    end_seconds = 5.955

    start_byte = int(bytes_per_second * start_seconds)
    end_byte = int(bytes_per_second * end_seconds)


    # 34,280,736
    print(len(byte_array))
    print(f"bytes_per_second={bytes_per_second}")
    print(f"{start_byte}:{end_byte}")
    # sfile.writeframesraw(byte_array) # edit this file and save to assets
    sfile.writeframesraw(byte_array[start_byte:end_byte]) # edit this file and save to assets
    # sfile.writeframesraw(byte_array[math.floor(34_280_000/2):34_280_000]) # edit this file and save to assets


    # close file
    sfile.close()

def _load_sound_segment(snd: pygame.mixer.Sound,
                        start_seconds =  5.282,
                        end_seconds =  5.955,
        frequency: int = 44100,

        # The size argument represents how many bits are used for each audio sample. If the value is negative then signed sample values will be used. Positive values mean unsigned audio samples will be used. An invalid value raises an exception.
        size: int = -16,
        channels: int = 2
                        ):
    
    bytes_per_second = int(frequency * channels * abs(size / 8))
    # start_seconds = 5.282
    # end_seconds = 5.955

    start_byte = int(bytes_per_second * start_seconds)
    end_byte = int(bytes_per_second * end_seconds)
    raw: bytes = snd.get_raw()
    byte_array =  bytearray(raw)



    return pygame.mixer.Sound(byte_array[start_byte:end_byte])


# uv run pytest tests/test_came.py
def test_came():
    screen = get_screen()

    clock = pygame.time.Clock()

    
    andSoundBoard = AndSoundBoard()
    came = Came()

    # sound.play()
    # came.play()
    # _save_sound(came.sound)

    # new_sound = _load_sound_segment(came.sound)

    # new_sound.play()

    # came.play()

    # andSoundBoard.play('came')
    andSoundBoard.play('came')
    # andSoundBoard.play('and')
    # andSoundBoard.play('right')
    # andSoundBoard.play('wrong')

    i = 0
    while i < (60 * 15):
        for event in pygame.event.get():  # Process all events in the queue

            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                print('keydown', event.key)
                if event.key == pygame.K_c:
                    andSoundBoard.play('came')
                elif event.key == pygame.K_a:
                    andSoundBoard.play('and')
                elif event.key == pygame.K_r:
                    andSoundBoard.play('right')
                elif event.key == pygame.K_w:
                    andSoundBoard.play('wrong')
            #     if event.key == pygame.K_RETURN:  # Check if Enter was pressed
            #         print('play note')
            #         piano.play_note(note='A4')
            
        screen.fill(FILL)



        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass