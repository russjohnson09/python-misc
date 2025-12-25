import pygame

def _get_nearest_byte(bytes_per_second, seconds, bytes_per_sample = 4):
    """ get nearest valid byte for sound sample"""
    # bytes_per_sample = abs(pygame.mixer.get_init()[1]) // 8 * pygame.mixer.get_init()[2]
    # print(f"{bytes_per_sample}") # 4 bytes per sample?
    bytes = int(bytes_per_second * seconds)
    padding_needed = bytes % bytes_per_sample

    return bytes + padding_needed

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



    new_byte_array = byte_array[start_byte:end_byte]



    return new_byte_array

def load_sound_segment(snd: pygame.mixer.Sound | bytearray,
                        start_seconds,
                        end_seconds,
        frequency: int = 44100,

        # The size argument represents how many bits are used for each audio sample. If the value is negative then signed sample values will be used. Positive values mean unsigned audio samples will be used. An invalid value raises an exception.
        size: int = -16,
        channels: int = 2
                        ) ->  pygame.mixer.Sound:

    return _load_sound_segment(
            snd,
            start_seconds=start_seconds,
            end_seconds=end_seconds,
            frequency=frequency,
            size=size,
            channels=channels
    )
