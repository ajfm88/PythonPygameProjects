import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time #Gives the time since we started pygame.init in miliseconds
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64)) #putting the variable into an f string so that it's converrted to a string
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list: # If the list is empty, it will evaluate to false
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surf,obstacle_rect)
            else: screen.blit(fly_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] #List Comprehension. Will check all of our rectangles and see if they're too far to the left

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PixelRunner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('PixelRunner\\font\Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('PixelRunner\graphics\Sky.png').convert()
ground_surface = pygame.image.load('PixelRunner\graphics\ground.png').convert()

# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

#Obstacles
snail_surf = pygame.image.load('PixelRunner\graphics\snail\snail1.png').convert_alpha()
fly_surf = pygame.image.load('PixelRunner\graphics\Fly\Fly1.png').convert_alpha()

obstacle_rect_list = []


player_surf = pygame.image.load('PixelRunner\graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('PixelRunner\graphics\Player\player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer - a cusom user event that is triggered in certain time intervals
obstacle_timer = pygame.USEREVENT + 1 # Add +1 there are some events that are already reserved for pygame. To avoid a conflict, we add a plus 1.
pygame.time.set_timer(obstacle_timer,1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: #Making sure player can only jump when touching the ground
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: #Stops the player from flying by double jump
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

                start_time = int(pygame.time.get_ticks() / 1000)
        
        if event.type == obstacle_timer and game_active:
            if randint(0,2): # Randomly triggering either True or False (evaluates to either 0 [false] or 1 [true])
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        # screen.blit(score_surf,score_rect)
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surf,snail_rect)

        # Player
        player_gravity += 1 # In every cycle of the game loop we will increase gravity by a bit.
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300 #Gravity.
        screen.blit(player_surf,player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        game_active = collisions(player_rect,obstacle_rect_list)

    else: # Game Over screen
        screen.fill((94, 129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear() # We remove enemies when gaming over, that way the game restarts properly and doesn't crash right away
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0: screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message,score_message_rect)
 
    pygame.display.update()
    clock.tick(60)