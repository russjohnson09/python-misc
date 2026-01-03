

from .pygame_handler import PygameHandler

from russ_font import FontHelper
from lib_inputs import InputHandler

import pygame
import pandas as pd

import os

screen_size =  (640, 480) # psx resolution
# screen_size =  (320, 240)

ph = PygameHandler(screen_size=screen_size)
ph.FPS = 120 # default is 60 but we would like 120

# set fill to red based on the technologic fill 
ph.FILL = FontHelper.TECHNOLOGIC_SCREEN_BACKGROUND_COLOR


# pandas is overkill for just reading a csv file but it is also pretty easy to use so...

def _get_words():
    df = pd.read_csv(os.path.dirname(__file__) + '/technologic_words.csv', keep_default_na=False)

    dict_output = df.to_dict(orient="index")

    
    words = []
    for key in list(dict_output.keys()):
        row = dict_output[key]
        word_upper = row['word'].upper()
        start = int(row['start'] or 0)
        end = int(row['end'] or 0)
        words.append({
            'word': word_upper,
            'start': start,
            'end': end,
        })

    return words


def _start_technologic():


    screen = ph.screen


    # main_sound = ph.get_sound("09.-Technologic.flac")
    ph.load_music("&.mp3")

    ph.load_music("09.-Technologic.flac")

    font_helper = FontHelper(ph)

    # font = ph.font

    # font = pygame.font.SysFont("Arial" , 8 , bold = False)

    max_loops = os.environ.get('RUSS_MAX_LOOPS', None)
    if max_loops is not None:
        max_loops = int(max_loops)


    text = 'test'


    word_idx = 0

    words = _get_words()
    ih = InputHandler(pygame)
    ih.joystick = ph.get_primary_joystick()




    i = 0
    while not ph.quit:

        if max_loops is not None and max_loops < i:
            return
        
        ph.hide_mouse()

        ih.clear_just_pressed()

        for event in ph.get_event():
            ih.handle_event(event)

        if ih.west_just_pressed:
            pygame.mixer.music.play()
            word_idx = 0
            text = words[word_idx]['word']

        if ih.south_just_pressed:
            word_idx += 1
            word_idx = word_idx % len(words)
            text = words[word_idx]['word']


        ph.fill()
        

        # if pygame.mixer.music.get_busy() and word_key_idx is not None:
        #     # current_play_pos = pygame.time.get_ticks()
        #     current_play_pos = pygame.mixer.music.get_pos()
        # # if word_key_idx is not None:
        #     timing = word_keys[word_key_idx]
        #     if current_play_pos > timing:
        #         text = technologic_word_timing[word_keys[word_key_idx]]
        #         word_key_idx += 1
        #         if word_key_idx >= len(word_keys):
        #             word_key_idx = None


        # test font in this loop
        font_helper.draw_technologic(text)


        ph.display_flip()

        ph.clock_tick()
        i += 1

        font_helper.draw_technologic('')



def technologic():

    print("start technologic game")
    print("start technologic game")
    print("start technologic game")
    

    _start_technologic()