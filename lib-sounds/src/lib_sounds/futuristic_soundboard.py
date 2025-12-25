import os
import pygame
from .constants import ASSET_DIR

import enum

_SFX2020 = os.path.abspath(os.path.join(ASSET_DIR, '300futuristicsfx/SFX2020/'))

class FUTURISTIC_SOUNDS(enum.Enum):
    MINI_LASER_ATTACK = f'{_SFX2020}/MiniLaserAttack3.wav'


class FuturisticSoundboard():

    MINI_LASER_ATTACK = f'{_SFX2020}/MiniLaserAttack3.wav'

    # assets\300futuristicsfx\SFX2020\MiniLaserAttack3.wav
    def __init__(self):
        # filename = os.path.join(ASSET_DIR, f'&.mp3')
        # sound = pygame.mixer.Sound(filename)
        # raw: bytes = sound.get_raw()
        # byte_array =  bytearray(raw)
        # self.byte_array = byte_array
        pass

    def get_sound(self, name: FUTURISTIC_SOUNDS) -> pygame.mixer.SoundType:
        return pygame.mixer.Sound(name)
