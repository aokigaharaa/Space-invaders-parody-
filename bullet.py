import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):    #создаётся пуля там, где пушка
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 147, 216, 81
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):       #пулька летит
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):      #рисуется пулька
        pygame.draw.rect(self.screen, self.color, self.rect)