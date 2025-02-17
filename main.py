import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from shot import Shot
from sys import exit


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField() 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    updatable.add(player)
    drawable.add(player)
    



    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
             
        screen.fill((0,0,0))
        updatable.update(dt) 
        
        for drawing in drawable:
            drawing.draw(screen)
        
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                exit()
                
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.kill() 
                
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
     
       
if __name__ == "__main__":
    main()