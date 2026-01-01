import pygame


class FontHelper():

    # TECHNOLOGIC_SCREEN_BACKGROUND_COLOR = (255,0,0)
    # TECHNOLOGIC_SCREEN_BACKGROUND_COLOR = (89.0,7.5,2.0)
    # TECHNOLOGIC_SCREEN_BACKGROUND_COLOR = (89.0 * 1.5,7.5 * 1.5,2.0 * 1.5)
    # TECHNOLOGIC_SCREEN_BACKGROUND_COLOR = (
        # 97.3,32.2,0.8)

    # TECHNOLOGIC_SCREEN_BACKGROUND_COLOR = (
        # 97.3,12.2,0.8)

    TECHNOLOGIC_SCREEN_BACKGROUND_COLOR = (89.0,7.5,2.0)

    _ph = None


    _font = None
    _font_technologic = None

    @property
    def font(self):
        # TODO if screen size has changed then get a new font.
        if self._font is None:
            self._font = pygame.font.SysFont("Arial" , 8 , bold = False)
        

        return self._font
    
    @property
    def font_technologic(self):
        if self._font_technologic is None:
            self._font_technologic = pygame.font.SysFont("Arial" , 140 , bold = False)
        

        return self._font_technologic

    def __init__(self, pygame_handler):

        # font size is dependent on screen size set by self._ph


        self._ph = pygame_handler

        pass

# https://en.wikipedia.org/wiki/ClearType
    def draw_technologic(self, text = 'PRESS'):
        if text == '':
            return


        # https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
        # render(text, antialias, color, background=None) -> Surface

        # scale based on screen width
        screen_size = size = self._ph.size

        # scale = float(screen_size[0]) / float(640) # screen size of 320 will scale to 0.5 its size

        # Is there padding or margins that are a part of this surface?
        # I should have a border around the surface to make this clearer
        # text_surface: pygame.surface.Surface = self.font_technologic.render(text , antialias=False, color=pygame.Color("BLACK"))

        text_surface: pygame.surface.Surface = self.font_technologic.render(text , antialias=True, color=pygame.Color("BLACK"))
        # text_surface = pygame.transform.scale_by(text_surface, scale)
        # text_surface = pygame.transform.scale(text_surface, screen_size)


        # RENAME
        text_surface = pygame.transform.scale(text_surface, (screen_size[0] * (len(text) / 6) , screen_size[1]))


        # pygame.draw.rect(text_surface, (0,0,0), (0,0,screen_size[0], screen_size[1]), 0)

        # pygame.draw.line(text_surface, (0,0,0), 0, screen_size[1], 5)

        # pygame.draw.line(text_surface, (0,0,0), (0,0), (screen_size[1], 0), 5)



        rect = text_surface.get_rect()

        width = rect.w
        height = rect.h

        text_surface2: pygame.surface.Surface = self.font.render(f"{(width, height)} : {size}" , antialias=False, color=pygame.Color("BLACK"))

        screen = self._ph.screen
        
        # centering logic based on the texture surface size?

        center = (size[0] / 2.0, size[1] / 2.0)

        offset_x = width / 2.0
        offset_y = height / 2.0

        center = (center[0] - offset_x, center[1] - offset_y)

        # screen.blit(text_surface,center)
        screen.blit(text_surface,(center[0],0))


        screen.blit(text_surface2,(40,40))

        pass


__all__ = [
    FontHelper
]