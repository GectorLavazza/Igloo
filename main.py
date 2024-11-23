import random

import pygame
import time
from settings import set_screen, FPS, SW, SH, RATIO, play_music
from particles import create_particles, generate_particles
from igloo import Igloo
from light import Light, Darkness

lp = [(13, 30),
      (29, 105),
      (66, 50),
      (86, 85),
      (46, 9),
      (120, 18),
      (139, 121),
      (154, 66),
      (177, 22),
      (211, 113),
      (222, 48),
      (263, 9),
      (283, 86),
      (305, 34),
      (338, 113),
      (370, 16),
      (403, 50),
      (387, 83),
      (433, 69),
      (449, 113),
      (446, 7)]

pygame.init()
clock = pygame.time.Clock()
screen, size, screen_rect = set_screen((SW, SH))

last_time = time.time()

running = True

darkness = Darkness()

igloo_g = pygame.sprite.Group()
light_g = pygame.sprite.Group()

igloo = Igloo('igloo-Sheet', 480, 270, igloo_g)
for pos in lp:
    x, y = pos[0] + 0.5, pos[1] + 0.5
    d = random.randint(20, 30) / 100
    light = Light(4, (x, y), (153, 201, 179), d, darkness, light_g)

light = Light(8, (240, 151), (153, 201, 179), 0.5, darkness, light_g)
light = Light(20, (455, 37), (153, 201, 179), 0.2, darkness, light_g)

play_music('igloo', volume=1)

while running:

    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_pos[0] / RATIO, mouse_pos[1] / RATIO)

    igloo_g.update(dt)
    light_g.update(dt)

    screen.fill(pygame.Color('black'))

    igloo_g.draw(screen)

    darkness.draw(screen)

    light_g.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
