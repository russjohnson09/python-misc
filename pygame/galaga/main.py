import pygame
import time
from typing import Any, Generator, List, Optional, Callable, Tuple
import lib_sprites

print(lib_sprites)
Event = Generator[None, None, None]
Callback = Callable[[], Any]
Colour = Tuple[int, int, int]


RED = (255, 0, 0)  # RGB values for red
WHITE = (255, 255, 255) # RGB values for white background
BLACK = (0, 0, 0) # RGB values for white background


# https://www.reddit.com/r/pygame/comments/144ihia/asynchronous_event_handling_example/
# https://github.com/rbaltrusch/pygame_examples/blob/master/code/async_events/main.py
class Delay:
    """
    Iterable delay class that can be used in an asynchronous event to delay for an amount of time.
    Can be used like this to asynchronously delay by 1 second: yield from Delay(1)
        Note: this is equivalent to the following: for _ in Delay(1): yield
    An optional wait_callback can be specified, which will be called each tick while delaying.
    """

    def __init__(self, duration: float, wait_callback: Optional[Callback] = None):
        self.duration = duration
        self.wait_callback = wait_callback
        self.start_time = time.time()

    def __iter__(self):
        while time.time() - self.start_time < self.duration:
            if self.wait_callback:
                self.wait_callback()
            yield

class EventQueue:
    """
    Encapsulates the asynchronous event handling by handling a single generated
    result per event per tick.
    """

    def __init__(self):
        self._events: List[Event] = []

    def update(self) -> None:
        """Updates the event queue"""
        expired_events: List[Event] = []
        for event in self._events:
            try:
                next(event)
            except StopIteration:
                expired_events.append(event)
        self._events = [x for x in self._events if x not in expired_events]

    def append(self, event: Event) -> None:
        """Appends the specified event to the event queue"""
        self._events.append(event)




def _init():

    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("Red Square Example")

def get_screen(screen_width = 800, screen_height = 600):
    # screen_width = 800
    # screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen


# https://www.reddit.com/r/pygame/comments/144ihia/asynchronous_event_handling_example/
def sound_loop() -> Event:
    file_path = "mmx5_stage_start.mp3"  # Replace with your actual file path
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(0)  # Play once

    # play-mp3\main.py for examples on reserve channel and other things
    sound_effect = pygame.mixer.Sound(file_path)
    yield from Delay(2)

    # pygame.time.wait(1000)
    sound_effect.play()



class Square():

    def __init__(self, screen):
        self.w = 100
        self.h = 50
        self.x = 100
        self.y = 100
        self.screen = screen

    def render(self):
        pygame.draw.rect(self.screen, RED, (self.x, self.y, self.w, self.h)) # Draw a red rectangle at (100,100) with size 50x50


    def move(self):
        self.x += 1
        self.y += 0.5




def main_loop(screen):
    event_queue = EventQueue()
    clock = pygame.time.Clock()

    # event_queue.append(sound_loop())

    square = Square(screen)
    
    i = 0
    running = True
    while running:
        i += 1
        # print(lib_sprites)

        if i > 555:
            return
        for event in pygame.event.get():  # Process all events in the queue
            if event.type == pygame.QUIT:
                running = False
                return
        
        screen.fill(BLACK)
        square.move()
        square.render()
        event_queue.update()


        pygame.display.flip()
        # I think this is for a consistent framerate??
        clock.tick(60)

        # pygame.time.wait(1)
        sound_loop()

    return


# https://pyga.me/docs/ref/display.html#pygame.display.set_window_position
# switch to pygame-ce???
# https://www.reddit.com/r/pygame/comments/1ajih56/pygame_or_pygamece/
# pygame-ce 2.5.6 (SDL 2.32.10, Python 3.13.9)                                                                                                                                             
def main():

    # return
    _init()
        
    screen = get_screen()
    screen.fill(WHITE)  # Fill the screen with white


# https://github.com/pygame/pygame/issues/1525
# https://www.gamedev.net/forums/topic/428022-sdl-window-resize-glitch/
    pygame.display.flip() # Or pygame.display.update()

    main_loop(screen)


    pygame.quit()


main()