import pygame
import sys
from bullet import Bullet
from chubrik import Chubrik
import time


def events(screen, gun, bullets):      #обрабатываются происходящие события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_d:     #летит вправо
                gun.moveright = True
            elif event.key == pygame.K_a:   #летит влево   
                gun.moveleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:    
            if event.key == pygame.K_d:     #летит вправо
                gun.moveright = False
            elif event.key == pygame.K_a:   #летит влево
                gun.moveleft = False

def update(bg_color, screen, stats, sc, gun, chubriks, bullets):      #обновляется экран
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    chubriks.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, bullets, chubriks):    #обновляется позиция пули
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, chubriks, True, True)
    if collisions:
        for chubriks in collisions.values():
            stats.score += 10 * len(chubriks)
        sc.image_score()
        check_record(stats, sc)
        sc.image_guns()
    if len(chubriks) == 0:
        bullets.empty()
        create_army(screen, chubriks)

def gun_kill(stats, screen, sc, gun, chubriks, bullets):    #пушка и армия чубриков сталкиваются
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        chubriks.empty()
        bullets.empty()
        create_army(screen, chubriks)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_chubriks(stats, screen, sc, gun, chubriks, bullets):      #обновляется позиция чубриков
    chubriks.update()
    if pygame.sprite.spritecollideany(gun, chubriks):
        gun_kill(stats, screen, sc, gun, chubriks, bullets)
    chubriks_check(stats, screen, sc, gun, chubriks, bullets)

def chubriks_check(stats, screen, sc, gun, chubriks, bullets):      #проверяем находятся ли чубрики на краю экрана
    screen_rect = screen.get_rect()
    for chubrik in chubriks.sprites():
        if chubrik.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, chubriks, bullets)
            break

def create_army(screen, chubriks):      #создаётся армия чубриков
    chubrik = Chubrik(screen)
    chubrik_width = chubrik.rect.width
    number_chubrik_x = int((800 - 2 * chubrik_width) / chubrik_width)
    chubrik_height = chubrik.rect.height
    number_chubrik_y = int((700 - 160 - 2 * chubrik_height) / chubrik_height)

    for row_number in range(number_chubrik_y):
        for chubrik_number in range(number_chubrik_x):
            chubrik = Chubrik(screen)
            chubrik.x = chubrik_width + (chubrik_width * chubrik_number)
            chubrik.y = chubrik_height + (chubrik_height * row_number)
            chubrik.rect.x = chubrik.x
            chubrik.rect.y = chubrik.rect.height + (chubrik.rect.height * row_number)
            chubriks.add(chubrik)

def check_record(stats, sc):        #проверяем рекорды
    if stats.score > stats.record:
        stats.record = stats.score
        sc.image_record()
        with open('record.txt', 'w') as file:
            file.write(str(stats.record))

