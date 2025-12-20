import pygame

class InputHandler():
        # pygame.mouse.set_visible(False) # this is working, I can't see mouse within window

        # pygame.event.set_grab(True)

    joystick: pygame.joystick.JoystickType = None

    _pygame = None

    _south = False
    _west = False
    _south_just_pressed = False
    _west_just_pressed = False

    _tick = 0

    left = False
    right = False
    up = False
    down = False

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
    
    @west.setter
    def west(self, val):
        self._west_just_pressed = val
        self._west = val
    
    @property
    def south(self):
        return self._south
    
    @south.setter
    def south(self, val):
        self._south_just_pressed = val
        self._south = val


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
        # do_iteration <Event(1540-JoyButtonUp {'joy': 0, 'instance_id': 0, 'button': 0})>

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
        elif event.type == self._pygame.JOYBUTTONUP:

            if self.joystick:
                if  self.joystick.get_instance_id() == event.instance_id:
                    if event.button == 0:
                        self.south = False
                    elif event.button == 2:
                        self.west = False
                else:
                    print("unhandled joystick instance ", event.instance_id, self.joystick.get_instance_id())

            else:
                print("no joystick registered")
        elif event.type == self._pygame.JOYBUTTONDOWN:
            if self.joystick:
                if  self.joystick.get_instance_id() == event.instance_id:
                    if event.button == 0:
                        self.south = True
                    elif event.button == 2:
                        self.west = True
                else:
                    print("unhandled joystick instance ", event.instance_id, self.joystick.get_instance_id())

            else:
                print("no joystick registered")
        elif event.type == self._pygame.JOYAXISMOTION:
            print(event)

            if self.joystick and self.joystick.get_instance_id() == event.joy:
                
                if event.axis == 0:
                    if event.value < -0.5:
                        self.left = True
                        self.right = False
                    elif event.value > 0.5:
                        self.right = True
                        self.left = False
                    else:
                        self.right = self.left = False
                elif event.axis == 1:
                    if event.value < -0.5:
                        self.up = True
                        self.down = False
                    elif event.value > 0.5:
                        self.down = True
                        self.up = False
                    else:
                        self.up = self.down = False
                # self.joystick.get_axis(0)
                # if event.button == 0:
                #     self.south = True
                # elif event.button == 2:
                #     self.west = True
        pass
    pass


__all__ = [InputHandler]