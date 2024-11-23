import pygame
from sprite import *


class Igloo(Sprite):
    def __init__(self, sheet, width, height, *group):
        super().__init__(*group)
        self.sheet = SpriteSheet(sheet)
        self.frame = 0
        self.max_frame = 3

        self.max_playback = 20
        self.playback = self.max_playback

        self.w, self.h = width, height

        self.image = self.sheet.get_image(self.frame, self.w, self.h)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def update(self, dt):
        self.update_playback(dt)

    def update_frame(self):
        if self.frame + 1 <= self.max_frame:
            self.frame += 1
        else:
            self.frame = 1

    def update_playback(self, dt):
        self.playback -= dt
        if self.playback < 0:
            self.playback = self.max_playback
            self.update_image()
            self.update_frame()

    def update_image(self):
        self.image = self.sheet.get_image(self.frame, self.w, self.h)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
