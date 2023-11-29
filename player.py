import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, position, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load('python-space-invaders/graphics/ship.png').convert_alpha()
        # pass a tuple for the postion of the rectangle
        self.rect = self.image.get_rect(midbottom = position)
        # character movement per assigned number of pixels
        self._speed = 5
        
        # variable use to limit the movement of ship on screen
        self._screen_width = screen_width
        
        # variable use to limit the travel of the bullet
        self._screen_height = screen_height
        
        self._shoot_time = 0
        self._shooter_ready = True
        # shooter ready for every 600 milliseconds
        self._shooter_cooldown = 600
        self._bullet = pygame.sprite.Group()
        
        # bullet sound effect
        self._bullet_sound = pygame.mixer.Sound('python-space-invaders/audio/laser.wav')
        self._bullet_sound.set_volume(.4)
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < self._screen_width:
            self.rect.x+= self._speed
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self._speed
        
        if keys[pygame.K_SPACE] and self._shooter_ready:
            self.shoot()
            self._shooter_ready = False
            self._shoot_time = pygame.time.get_ticks()
            self._bullet_sound.play()
    
    def recharge(self):
        if not self._shooter_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self._shoot_time >= self._shooter_cooldown:
                self._shooter_ready = True
            
    def update(self):
        self.get_input()
        self.recharge()
        self._bullet.update()
    
    def shoot(self):
        self._bullet.add(Bullet(self.rect.center, -8, self._screen_height))
