import pygame
from player import *
from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    dt = 0

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
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
     
       
if __name__ == "__main__":
    main()