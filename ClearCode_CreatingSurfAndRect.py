import pygame, sys

# General setup
pygame.init() #Initiates the entire program
clock = pygame.time.Clock()

# Create the display surface
screen = pygame.display.set_mode( (800, 800) )
second_surface = pygame.Surface([100,200])
second_surface.fill((0, 0, 128))

background = pygame.image.load('background_0.png')
background_rect = background.get_rect(topleft = [100, 200])

while True:
    # Events in pygame are just inputs from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Uninitiates the entire program
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(second_surface, (0, 50))
    screen.blit(background,background_rect)
    background_rect.right += 5
    pygame.display.flip() # will update the contents of the entire display
    # pygame.display.update() # updates only a specific section of the screen, but with no arguments, it works similar to pygame.display.flip().

    # To tell PyGame which portions of the screen it should update (i.e. draw on your monitor) you can pass a single pygame.
    # Rect object, or a sequence of them to the display.update() function. A Rect in PyGame stores a width and a height as well as a x- and y-coordinate for the position.

    clock.tick(60)