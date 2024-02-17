import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('sprites/tank3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moveright = False
        self.moveleft = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_gun(self):      #позиция пушки 
        if self.moveright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.moveleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):       #размещает пушку по центру снизу
        self.center = self.screen_rect.centerx
        