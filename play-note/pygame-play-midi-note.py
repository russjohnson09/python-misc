# https://stackoverflow.com/questions/15863534/playing-note-with-pygame-midi
import pygame.midi
import time

# https://github.com/supercollider/supercollider/issues/1922
# https://coolsoft.altervista.org/en/virtualmidisynth/faq#faq12
def _print_device_info():
    pygame.midi.init()

    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print(
            "%2i: interface :%s:, name :%s:, opened :%s:  %s"
            % (i, interf, name, opened, in_out)
        )

_print_device_info()
player = pygame.midi.Output(0)
# player = pygame.midi.Output(1)

# Unable to open Midi OutputDevice=0: b"PortMidi: `Host error'"
# Traceback (most recent call last):
# player.set_instrument(0)

player.note_on(64, 127)
time.sleep(1)
player.note_off(64, 127)
del player
pygame.midi.quit()