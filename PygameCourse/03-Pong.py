#pong.py
 
import pygame
from pygame.locals import *
from random import randint, choice

class Ball:
    def __init__(self,radius,color,xcor,ycor,xvel,yvel):
        self.radius = radius
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.rect = pygame.Rect(self.xcor,self.ycor,2*self.radius,2*self.radius)
        
    def move(self,paddle):
        if self.ycor < 0 or self.ycor > 500 - 2*self.radius:
            self.yvel = -self.yvel
        if self.rect.colliderect(paddle):
            self.xvel = -self.xvel
        self.xcor += self.xvel
        self.ycor += self.yvel
        self.rect = pygame.draw.rect(screen, self.color,
                            [self.xcor,self.ycor,2*self.radius,2*self.radius])

class Paddle:
    def __init__(self,xcor,ycor,height,width,color):
        self.xcor = xcor
        self.ycor = ycor
        self.height = height
        self.width = width
        self.color = color
        self.move = 0 #paddle doesn't move at first
        self.rect = pygame.Rect(self.xcor, self.ycor,self.width,self.height)

    def draw(self):
        self.ycor += self.move
        #don't go off the bottom of the screen
        if self.ycor > 500 - self.height: #if the ycor is off the screen
            self.ycor = 500 - self.height #reset the ycor to the bottom
            self.move = 0               #stop moving
        #don't go off the top of the screen:
        if self.ycor < 0: #if the ycor is off the screen
            self.ycor = 0 #reset the ycor to the top
            self.move = 0 #stop moving
        self.rect = pygame.draw.rect(screen, self.color,
                            [self.xcor,self.ycor,self.width,self.height])

class Score:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.score = 0

    def increaseScore(self,value):
        self.score += value

    def displayScore(self):
        # This is a font we use to draw text on the screen (size 72)
        font = pygame.font.SysFont("911 Porscha", 72)
        text = font.render(str(self.score), True, WHITE)
        screen.blit(text, [self.xpos, self.ypos])
        
    def resetScore(self):
        self.score = 0
        
def drawNet():
    '''draws the "net" down the middle of the screen'''
    y = 0 #start at top of screen
    while y < 500: # keep going until you reach the bottom
        pygame.draw.rect(screen,WHITE,[350,y,10,10]) #draw a square
        y += 20 #next y-value
        
# Define the colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

ball_list = []
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pong, Baby")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#create the ball
ball = Ball(5, #radius
            WHITE, #color
            randint(0,650), #x-value
            randint(0,450), #y-value
            1,   #x-velocity
            2)   #y-velocity

#create the paddles:
leftpaddle = Paddle(50,#xcor
                    randint(50,450),#ycor
                    50,#height
                    10,#width
                    WHITE) #color

rightpaddle = Paddle(650,#xcor
                    randint(50,450),#ycor
                    50,#height
                    10,#width
                    WHITE) #color

leftscore = Score(250,25)
rightscore = Score(400,25)
    
while not done:
    for event in pygame.event.get(): #Check all the clicks and keystrokes
        if event.type == pygame.QUIT: # If user clicked the X to close the window
            done = True # stop repeating this loop
        if event.type == pygame.KEYDOWN: #if a key is pressed
            if event.key == K_UP: #if the up arrow key is pressed
                rightpaddle.move = -5 #the right paddle should go up
            if event.key == K_DOWN: #if the down arrow key is pressed
                rightpaddle.move = 5 #the right paddle should go down
            if event.key == K_w: #if the W key is pressed
                leftpaddle.move = -5 #the left paddle should go up
            if event.key == K_s: #if the S key is pressed
                leftpaddle.move = 5 #the left paddle should go down
        if event.type == pygame.KEYUP: #if a key is released
            if event.key == K_UP or event.key == K_DOWN: #if it's the UP or DOWN key:
                rightpaddle.move = 0 #stop the right paddle
            if event.key == K_w or event.key == K_s: #if it's the W or S key:
                leftpaddle.move = 0 #stop the left paddle
                
    # --- Game logic should go here
    if ball.xcor > 700:
        ball.xcor = 350
        leftscore.increaseScore(1)
    if ball.xcor < 0:
        ball.xcor = 350
        rightscore.increaseScore(1)
    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #draw the net
    drawNet()
    
    #move the ball
    for paddle in [leftpaddle, rightpaddle]:
        ball.move(paddle)

    #move the paddles
    leftpaddle.draw()
    rightpaddle.draw()

    #display the scores
    leftscore.displayScore()
    rightscore.displayScore()

    #if one player scores 5 (or whatever max you choose)
    if leftscore.score == 5 or rightscore.score == 5:
        #start "waiting" for a response
        waiting = True
        while waiting:
            #display the Game Over text
            font = pygame.font.Font(None, 36)
            text = font.render("GAME OVER. PLAY AGAIN? Y/N ", True, WHITE)
            screen.blit(text, [200, 250])
            for event in pygame.event.get(): #check keystrokes
                if event.type == pygame.KEYDOWN: #if a key is pressed
                    if event.key == K_y: #if player presses Y for "yes"
                        leftscore.resetScore() #reset the scores
                        rightscore.resetScore()
                        waiting = False
                        break
                    if event.key == K_n: #if player presses N for "no"
                        waiting = False
                        done = True #game is done
                        break
            pygame.display.update() #keep refreshing screen while waiting
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# quit nicely.
pygame.quit()