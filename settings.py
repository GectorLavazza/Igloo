import pygame

FPS = 60

pygame.display.init()
screen_info = pygame.display.Info()


def fit_aspect_ratio(screen_width, screen_height,
                     target_width=480, target_height=270):
    aspect_ratio = target_width / target_height

    max_width = screen_width
    max_height = screen_height

    height_based_on_width = max_width / aspect_ratio
    if height_based_on_width <= max_height:
        return int(max_width), int(height_based_on_width)

    width_based_on_height = max_height * aspect_ratio
    if width_based_on_height <= max_width:
        return int(width_based_on_height), int(max_height)

    return int(max_width), int(max_height)


sw, sh = screen_info.current_w, screen_info.current_h
SW, SH = fit_aspect_ratio(sw, sh)
RATIO = SW / 480


def play_sound(filename, volume=0.5):
    sfx = pygame.mixer.Sound(f'assets/sfx/{filename}.wav')
    sfx.set_volume(volume)
    sfx.play()


def play_music(filename, volume=0.5):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f'assets/music/{filename}.wav')
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)


def set_screen(size, caption=''):
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
    screen_rect = (0, 0, size[0], size[1])

    return screen, size, screen_rect
