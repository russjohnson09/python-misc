

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

    print(dict_output)
    # tests\test_font.py {0: {'start': 1000, 'text': 'PRESS'}, 1: {'start': 2000, 'text': ''}, 2: {'start': 3000, 'text': 'ZIP'}}
    
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


def _start_spelling_game():

    ph.load_music("&.mp3")
    ph.load_music("09.-Technologic.flac")

    font_helper = FontHelper(ph)

    # font = ph.font

    # font = pygame.font.SysFont("Arial" , 8 , bold = False)

    max_loops = os.environ.get('RUSS_MAX_LOOPS', None)
    if max_loops is not None:
        max_loops = int(max_loops)


    text = 'test'


    words = _get_words()

    print(words)


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

            if event.type == pygame.KEYDOWN:
                print(event.key)

            # print(event)
            # do my own custom handling
            continue



        ph.fill()

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
    

    _start_spelling_game()