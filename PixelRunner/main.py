import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PixelRunner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('PixelRunner\\font\Pixeltype.ttf', 50)

sky_surface = pygame.image.load('PixelRunner\graphics\Sky.png').convert()
ground_surface = pygame.image.load('PixelRunner\graphics\ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surf = pygame.image.load('PixelRunner\graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300)) # Bottom of the snail has to be in the same position as ground_surface

player_surf = pygame.image.load('PixelRunner\graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300)) #It takes a surface and draws a rectangle around it

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION: #Using the event loop to check if the mouse collides with the player rectangle
        #     if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800     #In pygame you don't move the surface, you move the rectangle that contains the surface
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect) # We are taking the player surface and we are placing it in the position of this rectangle

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos() #Getting the current position of the mouse
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed()) #Which mouse button is pressed

    pygame.display.update()
    clock.tick(60)