import pygame
import os


_default_asset_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../assets'))

ASSET_DIR = os.environ.get('ASSET_DIR', _default_asset_dir)

# https://stackoverflow.com/questions/21080790/pygame-and-rotation-of-a-sprite
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


class Sound(pygame.mixer.Sound):

    # Load a specific image from a specific rectangle
    def play(self):
        channel = super().play()
        print(f"end effect channel: {channel}")
        return channel



class MMX5StageStart(Sound):

    def __init__(self):
        filename = os.path.join(ASSET_DIR, 'mmx5_stage_start.mp3')
        super().__init__(filename)


class PianoNote(Sound):
    def __init__(self, note='A4'):
        filename = os.path.join(ASSET_DIR, f'UprightPianoKW-small-SFZ+FLAC-20190703/UprightPianoKW-small-SFZ+FLAC-20190703/samples/A4vH.flac')
        super().__init__(filename)

# UprightPianoKW-small-SFZ+FLAC-20190703
class Piano():


    def play_note(self, note='A4'):
        piano_note = PianoNote(note=note)

        return piano_note.play()



# TODO defaults here should be a shared default which is also passed to the pygame.mixer
# or pull the current values from pygame.mixer??
def _load_sound_segment(snd: pygame.mixer.Sound | bytearray,
                        start_seconds,
                        end_seconds,
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

    if isinstance(snd, pygame.mixer.SoundType):
        raw: bytes = snd.get_raw()
        byte_array =  bytearray(raw)
    else:
        byte_array = snd




    return pygame.mixer.Sound(byte_array[start_byte:end_byte])


class AndSoundBoard():
    soundboard_mappings = {
        
    }
    def __init__(self):
        filename = os.path.join(ASSET_DIR, f'&.mp3')
        # super().__init__(filename)
        sound = pygame.mixer.Sound(filename)
        raw: bytes = sound.get_raw()
        byte_array =  bytearray(raw)
        self.byte_array = byte_array
        self.sound = _load_sound_segment(sound,
                        start_seconds =  5.282,
                        end_seconds =  5.955,
                                         )

    # https://stackoverflow.com/questions/68756636/how-to-play-an-audio-file-starting-at-a-specific-time-in-pygame
    def play(self, name):
        start_seconds =  0
        end_seconds =  None
        self.soundboard_mappings.get(name, {}).get('start_seconds')
        self.soundboard_mappings.get(name, {}).get('end_seconds')

        # if name == 'came':
        #     start_seconds =  5.282
        #     end_seconds =  5.955
        
        if end_seconds is None:
            return
        snd = _load_sound_segment(self.byte_array, start_seconds, end_seconds)
        snd.play()

# mixer.music.play(start=1.3)
# Came

# I probably want the file not being there to be handled gracefully.
# Log an error so that I can correct missing sounds but music is going to be some of the bigger assets.
# https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.play
# https://www.pygame.org/docs/ref/mixer.html?highlight=sound#pygame.mixer.Sound
# Sound(buffer=buffer) -> Sound
# I can probably clip the start and end as a buffer?
# pygame.mixer.music.set_pos()

# https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound
class Came():
    def __init__(self):
        filename = os.path.join(ASSET_DIR, f'&.mp3')
        # super().__init__(filename)
        sound = pygame.mixer.Sound(filename)
        self.sound = _load_sound_segment(sound,
                        start_seconds =  5.282,
                        end_seconds =  5.955,
                                         )

    # https://stackoverflow.com/questions/68756636/how-to-play-an-audio-file-starting-at-a-specific-time-in-pygame
    def play(self):
        self.sound.play()
        # pygame.mixer.music.play()
        # print(self.sound.get_raw())
        # super().play(loops, start, fade_ms)
