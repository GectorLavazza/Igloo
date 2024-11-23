import pygame
from load_image import load_image
from settings import RATIO


class Sprite(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)


class SpriteSheet:
    def __init__(self, sheet: str):
        self.sheet = load_image(sheet, do_scale=False)

    def get_image(self, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale_by(image, RATIO)

        return image
