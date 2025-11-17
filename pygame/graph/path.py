import math
from typing import Any, Generator, List, Optional, Callable, Tuple

import numpy as np
# cos is the inverse of sin?

# overallY - I think that is a shift? or is that x?
# I'm not going to include overallY and just put that in the SinPath
# yeild if not at ...
# For yeild can I do 
# https://docs.python.org/3/library/typing.html#type-aliases
def sin_path(frequency = 0.01, amplitude = 50.0, end_x = 640) -> list[np.array]:

    # overallY = 300
    # https://stackoverflow.com/questions/67874803/generating-and-drawing-sin-wave-using-pygame
    # no_pts = surface.get_width()

    # one point per pixel.
    # or just have it be speed and length?

    # no_pts = window.get_width()

    step = 1
    points = []
    for i in range(0, 100000, step):
        # x = i * 2.0 * math.pi
        x = i
        y = (amplitude * math.sin(x * frequency))
        points.append(np.array((x,y)))
        if x > end_x:
            break
        # prev_pt = (i, y)

    print(len(points)) # 642
    return points

class SinPath():

    points: list[np.array]

    def __init__(self):
        print('SinPath')
        self.points = sin_path()
        pass

    
    def get_point(self, t: int):
        # loop
        return self.points[t % len(self.points)]

    