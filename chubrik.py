import pygame

class Chubrik(pygame.sprite.Sprite):    #чубрик
    def __init__(self, screen):     #инициализация и дефолтная позиция
        super(Chubrik, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('sprites/chubrik.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):     #рисуем чубрика на экране
        self.screen.blit(self.image, self.rect)

    def update(self):   #чубрики перемещаются
        self.y += 0.1
        self.rect.y = self.y
