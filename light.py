import pygame
from sprite import Sprite
from settings import RATIO


class Light(Sprite):
    def __init__(self, radius, pos, color, density, *group):
        super().__init__(*group)

        self.color = color
        self.density = density

        self.r = radius
        self.w = self.h = self.r * 2

        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = pos[0] * RATIO, pos[1] * RATIO

        self.max_playback = 30
        self.playback = self.max_playback

    def update(self, dt):
        pass

    def get_image(self):
        image = pygame.Surface((self.w, self.h)).convert_alpha()

        image.set_alpha(255)
        image.fill(pygame.Color(0, 0, 0, 0))

        for i in range(4):
            ck = self.density / 4 * (i + 1)
            color = pygame.Color(*self.color, int(255 * ck))
            radius = int(self.r / 4 * (4 - i))
            pygame.draw.circle(image, color, (self.r, self.r), radius)
        image = pygame.transform.scale_by(image, RATIO)

        return image
