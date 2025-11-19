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



