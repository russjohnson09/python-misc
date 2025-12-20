

class InputHandler():
        # pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        # pygame.event.set_grab(True)

    _pygame = None

    _south = False
    _west = False
    _south_just_pressed = False
    _west_just_pressed = False

    _tick = 0

    def __init__(self, pygame):
        self._pygame = pygame
        pass


    @property
    def south_just_pressed(self):
        val = self._south_just_pressed
        # self._south_just_pressed = False
        return val
    
    @property
    def west_just_pressed(self):
        val = self._west_just_pressed
        # self._west_just_pressed = False
        return val
    
    @property
    def west(self):
        return self._west
    
    @property
    def south(self):
        return self._south
    @property
    def primary(self):
        return self.south

    def get_mouse_pos(self):
        return self._pygame.mouse.get_pos()
    
    def get_mouse_pressed(self):
        # https://www.pygame.org/docs/ref/mouse.html
        return self._pygame.mouse.get_pressed()

    def clear_just_pressed(self):
        self._south_just_pressed = False
        self._west_just_pressed = False
        pass

    def handle_event(self, event):
        
        if event.type == self._pygame.MOUSEBUTTONUP:
            # pos = self.pygame.mouse.get_pos()
            if event.button == 1:
                self._south = False
            elif event.button == 3:
                self._west = False
        elif event.type == self._pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._south = True
                self._south_just_pressed = True

            elif event.button == 3:
                self._west = True
                self._west_just_pressed = True

        pass
    pass


__all__ = [InputHandler]