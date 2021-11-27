import pygame, sys

class Crosshair(pygame.sprite.Sprite):

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)