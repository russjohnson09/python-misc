import os
import pygame
from .constants import ASSET_DIR
from .utils import load_sound_segment

import enum

_SFX2020 = os.path.abspath(os.path.join(ASSET_DIR, '300futuristicsfx/SFX2020/'))

# https://stackoverflow.com/questions/52624736/type-annotations-for-enum-attribute
class FUTURISTIC_SOUNDS(enum.Enum):
    MINI_LASER_ATTACK = {
        'location': f'{_SFX2020}/MiniLaserAttack3.wav',
        'start': 0,
        'end': 0.05
    }
    MINI_HIT = {
        'location': f'{_SFX2020}/MiniHit.wav',
        'start': 0,
        'end': 0.3
    }


class FuturisticSoundboard():
    # assets\300futuristicsfx\SFX2020\MiniLaserAttack3.wav
    def __init__(self):
        # filename = os.path.join(ASSET_DIR, f'&.mp3')
        # sound = pygame.mixer.Sound(filename)
        # raw: bytes = sound.get_raw()
        # byte_array =  bytearray(raw)
        # self.byte_array = byte_array
        pass

    def get_sound(self, sound_name_enum: FUTURISTIC_SOUNDS) -> pygame.mixer.SoundType:
        val = sound_name_enum.value
        main_sound = pygame.mixer.Sound(val.get('location'))

        if val.get('start') is not None and val.get('end') is not None:
            main_sound = load_sound_segment(main_sound,  val.get('start'),  val.get('end'))
        return  pygame.mixer.Sound(main_sound)