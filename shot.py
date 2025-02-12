import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), (self.position.x, self.position.y), SHOT_RADIUS)
        
    def update(self, dt):
        self.position += self.velocity * dt 