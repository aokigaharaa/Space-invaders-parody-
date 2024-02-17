import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Стрелялки убивалки")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    chubriks = Group()
    controls.create_army(screen, chubriks)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, chubriks, bullets)
            controls.update_bullets(screen, stats, sc, bullets, chubriks)
            controls.update_chubriks(stats, screen, sc, gun, chubriks, bullets)  

run()

