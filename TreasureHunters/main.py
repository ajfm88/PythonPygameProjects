from cgi import test
import pygame
import sys
from settings import *
from level import Level

# note from quasar098: it would be cool to this but multiplayer with either pickle or socket modules

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
pygame.display.set_caption("Treasure Hunters")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(75)
    # change this to match your refresh rate
