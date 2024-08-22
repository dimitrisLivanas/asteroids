# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    # create Player instance AFTER adding Player to the groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidField = AsteroidField()
    while True:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0))
        for player in updatable:
            player.update(dt)
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()