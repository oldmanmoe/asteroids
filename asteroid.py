import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
   
    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(random_angle)
        asteroid2_velocity = self.velocity.rotate(-random_angle) 
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 =  Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_1.velocity = asteroid1_velocity * 1.2
        asteroid_2.velocity = asteroid2_velocity * 1.2
        

        