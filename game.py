#The goal of the game is to grab the pint of beer before the enemies take it away from you.
#The enemy of enjoying a cold Germanic Fizzydrink is the Covid19 virus,
#sick people and the rules set out by our president.

#I used the example code as the foundation from which to build my game.
#The be honset, I wanted to do much more with the game, such as add music and sound effects,
#place a scoreboard on the screen and place a hitbox around the screen,
#which would allow the enemies to respawn if they leave the screen.
#Due to timeconstraints I had to settle for only the requirements of the task.
#I intend to return to this project when I have more skills at my disposal, as
#these capstone projects could be placed in my portfolio.

#-----------------------ADMIN-----------------------------------

import pygame
import random
pygame.init() 

#----------------------SCREEN-----------------------------------

#I changed the color of the screen, to grey, to add a scoreboard later on.

screen_width = 900
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
red = (100,100,100)


#--------------------CHARACTERS---------------------------------

player = pygame.image.load("superhero.png")
enemy1 = pygame.image.load("cough.png")
enemy2 = pygame.image.load("virus.png")
enemy3 = pygame.image.load("cyril_ramaphosa.png")
prize = pygame.image.load("beer.png")

#By using get.height and get.width, the sizes of the images stay the same as the files.
#I resized the images manually, so that they are all the same size.
#All icon images were downloaded from flaticon.com and is free to use.

superhero_height = player.get_height()
superhero_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

#--------------------POSITIONS----------------------------------

#The positions of the characters are such, that they will all start at the edge of the screen.
#The enemies will all attack from different directions and the player will
#start at the bottom of the y-axis.

playerXPosition = 450
playerYPosition = (500 - superhero_height)	#This is to make sure that the superhero starts at the bottom of the screen.

enemy1XPosition =  random.randint(0, screen_width - enemy1_width)
enemy1YPosition =  0

enemy2XPosition =  0
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

enemy3XPosition =  900 - enemy1_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

prizeXPosition =  300
prizeYPosition =  100

#I kept the code below as a comment, because it allows the prize to spawn randomly at the beginning.
#If I want to use it later on, I can easily do it.
#prizeXPosition =  random.randint(0, screen_width - prize_width)
#prizeYPosition =  random.randint(0, screen_height - prize_height)

#----------------------SCORE-------------------------------------

#I added these variables to easily add a scoreboard later on.
#Initially I gave the player three lives, but the briefing calls
#for instant death when the player collides with an enemy.
#The briefing further asks for instant victory once the prize is caught.
#I initially had the player and enemies compete for the first team to 5,
#but this isn't in line with the briefing.
#This can easliy be changed later.

player_score = 0
enemy_score = 0
lives = 1

#---------------------CONTROLS-----------------------------------

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

#--------------------GAME LOOP-----------------------------------

#I need to familiarise myself with the pygame commands,
#such a .blit.

while 1:

    screen.fill(red) 
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()   
	
#-------------------PLAYER MOVEMENT------------------------------------ 
 
#I added the possibility of moving the character on the x-axis.
#The example only allowed vertical movement.
 
    for event in pygame.event.get():    
               
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
                
        if event.type == pygame.KEYDOWN:        

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True               
        
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
    
#This is the speed at which the player moves.
#To make the game more challenging, the speed
#could be increased here.	
	
    if keyUp == True:
        if playerYPosition > 0 :
            playerYPosition -= 0.2
    if keyDown == True:
        if playerYPosition < screen_height - superhero_height:
            playerYPosition += 0.2
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 0.2
    if keyRight == True:
        if playerXPosition < screen_width - superhero_width:
            playerXPosition += 0.2

# This code was added for enemies to respawn if they reach the edge of the screen.			

    if enemy1YPosition > 500:
        enemy1XPosition =  random.randint(0, screen_width - enemy1_width)
        enemy1YPosition =  0

    if enemy2XPosition > (900 + enemy2_width):
        enemy2XPosition =  0
        enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

    if enemy3XPosition < 0:
        enemy3XPosition =  900 - enemy3_width
        enemy3YPosition =  random.randint(0, screen_height - enemy3_height)


#----------------BOUNDING BOXES-------------------------------------------

#These are the hitboxes for all the icons on the screen. It is used
#to detect collision between objects.

    playerBox = pygame.Rect(player.get_rect()) 
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
       
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
	
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
	
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
	
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
	
#----------------COLLISION AND POINTS-------------------------------------------

#I added if statements for a possible scoreboard and health system.
#If the player collides with an enemy, he will lose a life.
#If any of the enemies collide with the pize, they will receive a point.
#The briefing only asked for 1 point for victory and instant death,
#but this could easily be changed later on.
#The player will also respawn if he dies, but seeing as he only has one
#life at this stage, he will die instantly.
#Enemy score is 2 to win, in case the enemies spawn very close to the prize.
   
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        lives -= 1
        playerXPosition = 450
        playerYPosition = (500 - superhero_height)

    if enemy1Box.colliderect(prizeBox) or enemy2Box.colliderect(prizeBox) or enemy3Box.colliderect(prizeBox):
        enemy_score += 1
		
    if enemy_score == 2:
        print("You lose!")
        pygame.quit()
        exit(0)
	
    if lives == 0:
        print("You lose!")
        pygame.quit()
        exit(0)	
 	
    if playerBox.colliderect(prizeBox):
        player_score += 1       
  
    if player_score == 1:
        print("You Win!")   
        pygame.quit()
        exit(0)
    
#This code was added for the possible collision between the enemies and the prize.
#Enemies will respawn if they hit each other.
#The prize will respawn if it is hit by an enemy or by the player, if the score to win is higher than 1.

    if enemy1Box.colliderect(enemy2Box):
        enemy1XPosition =  random.randint(0, screen_width - enemy1_width)
        enemy1YPosition =  0
    elif enemy1Box.colliderect(enemy3Box):
        enemy1XPosition =  random.randint(0, screen_width - enemy1_width)
        enemy1YPosition =  0
    elif enemy1Box.colliderect(prizeBox):
        prizeXPosition =  random.randint(0, screen_width - prize_width)
        prizeYPosition =  random.randint(0, screen_height - prize_height)
    elif enemy2Box.colliderect(enemy3Box):
        enemy2XPosition =  0
        enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
    elif enemy2Box.colliderect(prizeBox):
        prizeXPosition =  random.randint(0, screen_width - prize_width)
        prize2YPosition =  random.randint(0, screen_height - prize_height)
    elif enemy3Box.colliderect(prizeBox):
        prizeXPosition =  random.randint(0, screen_width - prize_width)
        prizeYPosition =  random.randint(0, screen_height - prize_height)
    elif playerBox.colliderect(prizeBox):
        prizeXPosition =  random.randint(0, screen_width - prize_width)
        prizeYPosition =  random.randint(0, screen_height - prize_height)
			       
#-------------------ENEMY MOVEMENT-------------------------------------------
    
#The speed at which the enemies move can be changed here, to make it more challenging.
#The + and - difference influences the direction in which the enemies move.

    enemy1YPosition += 0.10
    enemy2XPosition += 0.10
    enemy3XPosition -= 0.10
    
#------------------------END--------------------------------------------------
