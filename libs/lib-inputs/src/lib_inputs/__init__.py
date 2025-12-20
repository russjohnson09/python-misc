

class InputHandler():
        # pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        # pygame.event.set_grab(True)

    _pygame = None

    _south = False
    _west = False

    def __init__(self, pygame):
        self._pygame = pygame
        pass

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

    def handle_event(self, event):
        if event.type == self._pygame.MOUSEBUTTONUP:
            # pos = self.pygame.mouse.get_pos()
            if event.button == 1:
                self._south = False
            elif event.button == 3:
                self._west = False
            # if event.
        elif event.type == self._pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._south = True
            elif event.button == 3:
                self._west = True
        pass
    pass


__all__ = [InputHandler]