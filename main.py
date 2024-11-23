import random

import pygame
import time
from settings import set_screen, FPS, SW, SH, RATIO
from particles import create_particles, generate_particles
from igloo import Igloo
from light import Light

lp = [(54, 121),
      (118, 422),
      (266, 202),
      (185, 37),
      (482, 75),
      (558, 486),
      (616, 264),
      (709, 89),
      (891, 194),
      (846, 454),
      (1054, 38),
      (1133, 345),
      (1221, 137),
      (1355, 455),
      (1550, 334),
      (1614, 203),
      (1482, 67),
      (1786, 34),
      (1734, 275),
      (1797, 452),
      (347, 343)]

lp = list(map(lambda p: (p[0] / 4, p[1] / 4), lp))

pygame.init()
clock = pygame.time.Clock()
screen, size, screen_rect = set_screen((SW, SH))

last_time = time.time()

running = True

igloo_g = pygame.sprite.Group()
light_g = pygame.sprite.Group()

igloo = Igloo('igloo-Sheet', 480, 270, igloo_g)
for pos in lp:
    d = random.randint(20, 30) / 100
    light = Light(4, pos, (153, 201, 179), d, light_g)

light = Light(8, (240, 151), (153, 201, 179), 0.5, light_g)
light = Light(20, (455, 37), (153, 201, 179), 0.2, light_g)

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
    light_g.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
