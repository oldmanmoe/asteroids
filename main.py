import pygame
from player import *
from asteroid import *
from asteroidfield import *
from constants import * 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    dt = 0

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    asteroid_field = AsteroidField()
    updatable.add(player)
    drawable.add(player)

    
    while True:
        print(f"Number of asteroids: {len(asteroids)}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        updatable.update(dt)
        
        for drawing in drawable:
            drawing.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
     
       
if __name__ == "__main__":
    main()