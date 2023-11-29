import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, position, speed, screen_height):
        super().__init__()
        self.image = pygame.image.load('python-space-invaders/graphics/bullet.png').convert_alpha()
        # self.image.fill("white")
        self.rect = self.image.get_rect(center = position)
        self._initial_position = position
        self._bullet_speed = speed
        self._y_limit = screen_height + 50
    
    def update(self):
        self.rect.y += self._bullet_speed
        self.vanish()
        
    def vanish(self):
        if self.rect.y <= -50 or self.rect.y >= self._y_limit:
            self.kill()