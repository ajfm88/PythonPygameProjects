import pygame
from pygame.locals import *
from random import randint, choice, randrange
import time

class Ball:
    def __init__(self,radius,color,xcor,ycor,xvel,yvel):
        self.radius = radius
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.rect = pygame.Rect(self.xcor,self.ycor,2*self.radius,2*self.radius)
        
    def move(self,paddle,block_list,lives_obj):
        #if ball gets to right or left wall, bounce
        if self.xcor < 0 or self.xcor > 700 - 2*self.radius:
            self.xvel = -self.xvel
        #if ball gets to top edge, bounce
        if self.ycor < 0:
            self.yvel = -self.yvel
        if self.ycor > 500:
            self.ycor = 250
            lives_obj.decreaseLives()
        #if ball collides with paddle, bounce
        if self.rect.colliderect(paddle):
            self.yvel = -self.yvel
        #if ball collides with block, bounce
        for block in block_list:
            if self.rect.colliderect(block):
                self.yvel = -self.yvel
                block.status = 0
                score.increaseScore(10)
        self.xcor += self.xvel #update position by velocity
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
        self.xcor += self.move
        #don't go off the right side of the screen
        if self.xcor > 700 - self.width: #if the xcor is off the screen
            self.xcor = 700 - self.width #reset the xcor to the right
            self.move = 0               #stop moving
        #don't go off the left side of the screen:
        if self.xcor < 0: #if the xcor is off the screen
            self.xcor = 0 #reset the xcor to the left
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
        # This is a font we use to draw text on the screen (size 36)
        font = pygame.font.Font(None, 36)
        text = font.render("Score:"+str(self.score), True, GREEN)
        screen.blit(text, [self.xpos, self.ypos])
        
    def resetScore(self):
        self.score = 0

class Block():
    def __init__(self,xpos,ypos,length,width, color):
        self.x = xpos
        self.y = ypos
        self.length = length
        self.width = width
        self.color = color
        self.status = 1 #blocks start off "alive"
        self.rect = pygame.draw.rect(screen,self.color,
                         [self.x,self.y,self.length,self.width])

    def update(self,block_list):
        if self.status == 1:
            self.rect = pygame.draw.rect(screen,self.color,
                                    [self.x,self.y,self.length,self.width])
        else:
            block_list.remove(self)

#This is outside the Block class!
def setBlockField(block_list):
    #create field of Blocks:
    rows = 5
    cols = 12
    #width and height of a block
    WIDTH = 50
    HEIGHT = 25
    for i in range(rows):
        #every row gets its own color
            color = (randrange(0,255),randrange(0,255),randrange(0,255))
            for j in range(cols):
                block = Block((WIDTH+2)*j + 50,
                              (HEIGHT+2)*i+100,
                              WIDTH,HEIGHT,
                              color)
                block_list.append(block)
    return block_list

class Lives:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.lives = 3

    def decreaseLives(self):
        self.lives -= 1

    def displayLives(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Lives: "+str(self.lives), True, YELLOW)
        screen.blit(text, [self.xpos, self.ypos])
	
    def resetLives(self):
        self.lives = 3

# Define the colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255,255,0)

ball_list = []
block_list = []
 
pygame.init()
 
# Set the width and height of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Breakout!")
 
# boolean for keeping the game going
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#create the ball
ball = Ball(5, #radius
            WHITE, #color
            randint(0,650), #x-value
            randint(300,450), #y-value
            2,   #x-velocity
            -3)   #y-velocity

#create the paddle:
paddle = Paddle(randint(50,450),#xcor
                    450,#ycor
                    10,#height
                    50,#width
                    WHITE) #color

#create field of blocks
block_list = setBlockField(block_list)

#create the score object
score = Score(150,25)

#create the lives object
lives_obj = Lives(550,25)

#game loop
while not done:
    for event in pygame.event.get(): #Check all the clicks and keystrokes
        if event.type == pygame.QUIT: # If user clicked the X to close the window
            done = True # stop repeating this loop
        if event.type == pygame.KEYDOWN: #if a key is pressed
            if event.key == K_LEFT: #if the left arrow key is pressed
                paddle.move = -5 #the paddle should go left
            if event.key == K_RIGHT: #if the right arrow key is pressed
                paddle.move = 5 #the right paddle should go right
        
        if event.type == pygame.KEYUP: #if a key is released
            if event.key == K_RIGHT or event.key == K_LEFT: #if it's the LEFT or RIGHT key:
                paddle.move = 0 #stop the paddle

    # set the background color
    screen.fill(BLACK)
    
    #move the ball
    ball.move(paddle,block_list,lives_obj)

    #move the paddles
    paddle.draw()

    #display the score
    score.displayScore()

    #if all the blocks are gone:
    if len(block_list) == 0:
        #create new field of blocks
        block_list = setBlockField(block_list)
        #display the Game Over text
        font = pygame.font.Font(None, 72)
        text = font.render("NEXT LEVEL", True, GREEN)
        screen.blit(text, [100 ,300])
        pygame.display.update()
        #pause for next "level"
        time.sleep(3)
    #display the blocks
    for block in block_list:
        block.update(block_list)

    #display the lives object
    lives_obj.displayLives()

    #if the lives run out:
    if lives_obj.lives == 0:
	#keep the loop going       
        waiting = True
        #display the Game Over text
        font = pygame.font.Font(None, 36)
        text = font.render("GAME OVER. PLAY AGAIN? Y/N ", True, GREEN)
        #keep going util player gives an answer
        while waiting:               
            #blit the prompt image on the main surface
            screen.blit(text, [100 ,300])
            pygame.display.update()        
            #get an game events
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #if the user hit N the want to play again
                    if event.key == K_n:
                        done = True
                        waiting = False
                        break
                     #if the user hit Y the want to play again
                    if event.key == K_y :
                        lives_obj.resetLives()
                        #create new field of blocks
                        block_list = setBlockField(block_list)
                        waiting = False
                        playing = True
                        break
    
    # update the screen
    pygame.display.flip()
 
    # limit the speed to 60 frames per second
    clock.tick(60)
 
# quit pygame
pygame.quit()