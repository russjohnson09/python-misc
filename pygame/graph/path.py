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
        x = i * 2.0
        y = (amplitude * math.sin(x * frequency))
        points.append(np.array((x,y)))
        if x > end_x:
            break
        # prev_pt = (i, y)

    return points

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return np.array((qx, qy))

# https://www.reddit.com/r/learnpython/comments/1e8os0i/rotating_a_vertex_using_numpy/
# https://numpy.org/doc/2.1/reference/generated/numpy.roll.html

# https://stackoverflow.com/questions/57602828/how-to-rotate-square-numpy-array-of-2-dimensional-by-45-degree-in-python
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.rotate.html

class SinPath():

    speed: float = 1.0
    _tick: float = 0.0
    points: list[np.array]

    offset: np.array

    def __init__(self, offset, frequency = 0.01, amplitude = 50.0, speed = 1.0, rotation_degrees = 0.0):
        self.points = sin_path(frequency, amplitude)
        if rotation_degrees != 0.0:
            rotation_radians = rotation_degrees * (math.pi / 180.0)
            # https://stackoverflow.com/questions/10973766/understanding-the-map-function
            self.points = [rotate((0,0), point, rotation_radians) for point in self.points]
        self.offset = offset
        self.speed = speed
        pass

    def _do_tick(self):
        self._tick += self.speed
    
    def get_next_point(self):
        # loop
        idx = math.floor(self._tick)
        point = self.points[idx % len(self.points)] + self.offset
        # if increment_tick:
        self._do_tick()
        
        return point

    