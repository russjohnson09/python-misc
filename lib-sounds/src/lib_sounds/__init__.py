import pygame
import os
import wave

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



def _get_nearest_byte(bytes_per_second, seconds, bytes_per_sample = 4):
    """ get nearest valid byte for sound sample"""
    # bytes_per_sample = abs(pygame.mixer.get_init()[1]) // 8 * pygame.mixer.get_init()[2]
    # print(f"{bytes_per_sample}") # 4 bytes per sample?
    bytes = int(bytes_per_second * seconds)
    padding_needed = bytes % bytes_per_sample

    return bytes + padding_needed


# TODO defaults here should be a shared default which is also passed to the pygame.mixer
# or pull the current values from pygame.mixer??
def _load_sound_segment(snd: pygame.mixer.Sound | bytearray,
                        start_seconds,
                        end_seconds,
        frequency: int = 44100,

        # The size argument represents how many bits are used for each audio sample. If the value is negative then signed sample values will be used. Positive values mean unsigned audio samples will be used. An invalid value raises an exception.
        size: int = -16,
        channels: int = 2
                        ) -> bytearray:
    
    bytes_per_second = int(frequency * channels * abs(size / 8))
    # start_seconds = 5.282
    # end_seconds = 5.955

    # is the start position invalid??
    # start_byte = int(bytes_per_second * start_seconds) # make sure these start and end on some even number?
    # end_byte = int(bytes_per_second * end_seconds)

    start_byte = _get_nearest_byte(bytes_per_second, start_seconds)
    end_byte = _get_nearest_byte(bytes_per_second, end_seconds)

    if isinstance(snd, pygame.mixer.SoundType):
        raw: bytes = snd.get_raw()
        byte_array =  bytearray(raw)
    else:
        byte_array = snd



    print(f"{start_byte}:{end_byte}:{end_byte-start_byte}")
    # return pygame.mixer.Sound(byte_array[start_byte:end_byte])



    # bytes_per_sample = frequency
    # bytes_per_sample = frequency

    # new_sound_byte_array = byte_array[5462750:5547950]


    # end_byte += padding_needed

    # print(f"{start_byte}:{end_byte}:{end_byte-start_byte}")


    new_byte_array = byte_array[start_byte:end_byte]



    return new_byte_array
    # return pygame.mixer.Sound()


class AndSoundBoard():
    soundboard_mappings = {
        'came': [5.282,5.955],
        'right': [30.328,30.966],
        'and': [30.968,31.451],
        'wrong': [31.540,32.221],
    }
    def __init__(self):
        filename = os.path.join(ASSET_DIR, f'&.mp3')
        # super().__init__(filename)
        sound = pygame.mixer.Sound(filename)
        raw: bytes = sound.get_raw()
        byte_array =  bytearray(raw)
        self.byte_array = byte_array
        # self.sound = _load_sound_segment(sound,
        #                 start_seconds =  5.282,
        #                 end_seconds =  5.955,
        #                                  )

    # https://stackoverflow.com/questions/68756636/how-to-play-an-audio-file-starting-at-a-specific-time-in-pygame
    def play(self, name):
        start_seconds =  0
        end_seconds =  None
        start_seconds, end_seconds = self.soundboard_mappings.get(name, [None,None])
        # self.soundboard_mappings.get(name, {}).get('end_seconds')

        # if name == 'came':
        #     start_seconds =  5.282
        #     end_seconds =  5.955
        
        if end_seconds is None:
            return
        print(len(self.byte_array), start_seconds, end_seconds, name)
        sound_bytes = _load_sound_segment(self.byte_array, start_seconds, end_seconds)
        sfile = wave.open(f'{name}.wav', 'w')
        frequency: int = 44100
        channels: int = 2
        sfile.setframerate(frequency)
        sfile.setnchannels(channels)
        sfile.setsampwidth(2) # what is sample width? size / 8?
        sfile.writeframesraw(sound_bytes)
        pygame.mixer.Sound(sound_bytes).play()
        # snd.play()

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
