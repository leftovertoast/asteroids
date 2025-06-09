import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    myclock = pygame.time.Clock()
    dt = 0
    Player.containers = (updateable, drawable)
    p_1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        updateable.update(dt)
        pygame.display.flip()
        dt = (myclock.tick(60) / 1000)
        
    

if __name__== "__main__":
    main()