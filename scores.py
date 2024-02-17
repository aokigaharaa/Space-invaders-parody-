import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():     #выводится игровая информация
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (147, 216, 81)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_record()
        self.image_guns()

    def image_score(self):      #делаем из текста счёта в картинку этого счёта
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_record(self):     #делаем из рекорда картинку
        self.record_image = self.font.render(str(self.stats.record), True, self.text_color, (0, 0, 0))
        self.record_rect = self.record_image.get_rect()
        self.record_rect.centerx = self.screen_rect.centerx
        self.record_rect.top = self.screen_rect.top + 20

    def image_guns(self):       #количество жизней
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):       #выводим счёт на экран
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.record_image, self.record_rect)
        self.guns.draw(self.screen)