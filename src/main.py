import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from asteroidfield import *
from player import Player
import sys

from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        for item in asteroids:
            if item.collision(player) == True:
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        # FrameRate 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
