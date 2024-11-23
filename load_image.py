import os

import pygame

from settings import RATIO


def load_image(name, color_key=None, scale=(RATIO, RATIO), do_scale=True):
    fullname = os.path.join("assets/sprites/", name + '.png')

    try:
        image = pygame.image.load(fullname).convert_alpha()
        if do_scale:
            image = pygame.transform.smoothscale_by(image, scale)
    except pygame.error as e:
        print(f"Err: {e}")
        raise SystemExit(e)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)

    else:
        image = image.convert_alpha()

    return image
