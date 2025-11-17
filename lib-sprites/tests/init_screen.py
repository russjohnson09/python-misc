import pygame
import os


# lib_dir = os.path.dirname(__file__)
# os.path.abspath(pythonfile)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def _init():
    pygame.init()
    pygame.mixer.init()

#  640x480 psone
def get_screen(screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT) -> pygame.surface.Surface:
    # screen_width = 800
    # screen_height = 600
    # screen = pygame.display.set_mode((screen_width, screen_height))
    # screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.SCALED)

    return screen


def go_full_screen(screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT) -> pygame.surface.Surface:
    return pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)



class GalagaSprites(pygame.sprite.Sprite):

    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha() # Load image with transparency
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Game():

    # screen: pygame.surface.Surface
    # player: Player
    sprites: pygame.sprite.Group

    def __init__(self, 
                 sprites: pygame.sprite.Group,
                 frames_per_second: int
                 ):

        # self.screen = screen
        self.sprites = sprites
        # self.sprites.add(self.player)
        self.frames_per_second = frames_per_second
        self.delta = 60.0 / self.frames_per_second # at 120 fps move at half speed per tick

    # FPS here
    def main_loop(self, events: List[pygame.Event]):
            
        for event in events:  # Process all events in the queue
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_RETURN:  # Check if Enter was pressed
                    # Check if the Alt key is also pressed (KMOD_ALT)
                    if event.mod & pygame.KMOD_ALT: 
                        print("Alt + Enter detected!")
                        # Add your desired action here, e.g., toggle fullscreen
                        pygame.display.toggle_fullscreen()
        # self.player.rect.x += (1.0 * self.delta)



        return True



def draw_sin(surface: pygame.surface.Surface):

    line_color = RED

    frequency = 5
    amplitude = 50
    overallY = 300
    # https://stackoverflow.com/questions/67874803/generating-and-drawing-sin-wave-using-pygame
    no_pts = surface.get_width()

    # no_pts = window.get_width()
    for i in range(no_pts):
        x = i/no_pts * 2 * math.pi
        y = (amplitude * math.cos(x * frequency)) + overallY

        if i > 0:
            pygame.draw.aaline(surface, line_color,  prev_pt, (i, y))
        prev_pt = (i, y)


# time based graph spiral


def draw_points(
        surface: pygame.surface.Surface, 
                points: list[tuple[int,int]],
                offset: numpy.array = numpy.array((0,0))):

    line_color = RED

    prev_pt: tuple[int,int] = None
    for point in points:
        # print(point, offset)
        point_real = point + offset
        # point_real = numpy.array(point) + numpy.array(offset) # points should already be a numpy array?
        if not prev_pt is None:
            # print(point)
            pygame.draw.aaline(surface, line_color,  prev_pt, point_real)
        
        prev_pt = point_real


def draw_circle(surface: pygame.surface.Surface, point: numpy.array):


     #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.
    pygame.draw.circle(surface, BLUE, point, 10.0, 2)


    pass

# https://www.reddit.com/r/pygame/comments/nvvabc/what_are_subsurfaces_used_for/
def main_loop_outer(countdown, max_extra):


    
    screen = get_screen()

    # ss = spritesheet.spritesheet('galaga_sprites.png')

    # player = Player(0,0)

    game_sprites = pygame.sprite.Group()

    # initialize with screen (probably not necessary?)
    # and a game sprite group. The game handles the main loop,
    # but not the drawing on the actual screen if possible to separate these two
    game = Game(game_sprites, frames_per_second=FPS)

# https://github.com/pygame/pygame/issues/1525
# https://www.gamedev.net/forums/topic/428022-sdl-window-resize-glitch/
    pygame.display.flip() # Or pygame.display.update()

    clock = pygame.time.Clock()
    running = True

    # screen.fill(FILL)
    # https://www.reddit.com/r/pygame/comments/ppglzo/transparent_surfaces_in_pygame_20/

    # https://www.reddit.com/r/pygame/comments/ppglzo/transparent_surfaces_in_pygame_20/
    # surf = pygame.Surface(size, pygame.SRCALPHA)
    points_surface =  pygame.Surface(screen.size, pygame.SRCALPHA) # screen.copy()

    offset = numpy.array((0,100))

    sin_path = SinPath(offset)

    sin_path2 = SinPath(offset=(0,200), frequency=0.05)

    # TODO add a rotate
    # sin_path2.points = rotate(sin_path2.points, angle=45)



    paths: list[SinPath] = [sin_path, sin_path2]

    paths.append(SinPath(offset=(0,200), frequency=0.1))
    paths.append(SinPath(offset=(0,300), frequency=0.2, speed=0.2))


    paths.append(SinPath(offset=(0,300), frequency=0.2, speed=1.2))
    paths.append(SinPath(offset=(0,300), frequency=0.2, speed=1.4))
    paths.append(SinPath(offset=(0,300), frequency=0.2, speed=1.6))
    paths.append(SinPath(offset=(0,300), frequency=0.2, speed=1.8))
    paths.append(SinPath(offset=(0,300), frequency=0.2, speed=2.0))
    paths.append(SinPath(offset=(0,300), frequency=0.2, speed=22))

    paths.append(SinPath(offset=(0,0), frequency=0.2, speed=1.0, rotation_degrees=45.0))


    # instead of draw circle 
    paths.append(SinPath(offset=(0,380), frequency=0.2, speed=1.0, rotation_degrees=-45.0))

    paths.append(SinPath(offset=(180,0), frequency=0.2, speed=1.0, rotation_degrees=90.0))


    # for i in range(0,10000):
    for i in range(0,max_extra):

        paths.append(SinPath(offset=(180,0), frequency=0.2, speed=1.0 * i, rotation_degrees=90.0))

    # draw_sin(screen)


    pygame.display.flip() # Or pygame.display.update()


    for sp in paths:
        draw_points(surface=points_surface,points=sp.points, offset=sp.offset)
    #draw_points(surface=points_surface,points=sin_path2.points, offset=sin_path.offset)

    tick = 0
    while running:
        if countdown is not None:
            pygame.display.set_caption(f"Countdown: {countdown}")
            countdown -= 1
            if countdown < 0:
                return
        

        screen.fill(FILL)

        for sp in paths:
            # draw_points(surface=points_surface,points=sin_path.points, offset=sin_path.offset)
            draw_circle(surface=screen, point=sp.get_next_point())

        screen.blit(points_surface)
        # for sp in paths:
        #     draw_points(surface=screen,points=sp.points, offset=sp.offset)
        
        running = game.main_loop(pygame.event.get())



        # sin_path.do_tick()




        # game_sprites.update()
        # game_sprites.draw(screen)

        # draw_sin(screen)
        pygame.display.flip() # Or pygame.display.update()
        # screen.update() # https://www.pygame.org/docs/ref/display.html#pygame.display.update partial screen update

        # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
        clock.tick(FPS)
        # print(clock.get_fps())
        actual_fps = clock.get_fps()
        if actual_fps < 55.0:
            print(actual_fps)

