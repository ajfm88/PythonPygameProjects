import pygame
from pygame.locals import *

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
VIOLET = (148,0,211)

#define variables
#starting location:
x = 200
y = 200
#initial velocity:
xvel = 2
yvel = 3

#set up display
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('The Bouncing Ball')

clock = pygame.time.Clock()

#loop until user clicks the close button
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT: #if pygame window is closed by user
            done = True

    #fill the screen with background color
    screen.fill(BLACK)

    #check if ball needs to bounce:
    if x >= 600-20 or x <= 0: #if ball is at left or right wall
        xvel = -xvel        #change direction
    if y >= 600-20 or y <= 0: #if ball is at top or bottom:
        yvel = -yvel        #change direction

    #draw here
    pygame.draw.ellipse(screen,WHITE,[x,y,20,20],0)
    x += xvel #make x go up by xvel
    y += yvel #make y go up by yvel

    #update the screen
    pygame.display.update()

    #limit the speed
    clock.tick(60)

#quit and close
pygame.quit()