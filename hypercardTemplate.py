# Hypercard Template for Pygame

import pygame
import time
import random




# boiler plate for all pygame calls
pygame.init()
pygame.mixer.init()

FPS = 60
clock = pygame.time.Clock()

# pallette for the game 
black = (0,0,0)
white = (255,255,255)

# play area generated or res
display_width = 800
display_height = 600
 
# create the display or "Canvas" and title screen, with no frame
gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.NOFRAME)
pygame.display.set_caption('HYPERCARD TEMPLATE') # not seen cuz no frame

# game UI/OS icon
#icon = pygame.image.load('YourICON.png')
#pygame.display.set_icon(icon)





def card1():

	card1 = True

	cursor = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	while card1:

		for event in pygame.event.get():
			# if player closes window it quits
			if event.type == pygame.QUIT: # there is no border so this maybe be redundant
				pygame.quit()
				quit()
			# press c down and end intro..
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					card1 = False
				if event.key == pygame.K_SPACE:
					card1 = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		if 0  < cursor[0] < 800 and 0  < cursor[1] < 600:
			if event.type == pygame.MOUSEBUTTONDOWN:
				card1 = False

		# display bg image			
		pygame.display.update()
		clock.tick(10)




# load background image 
#lvlBG = pygame.image.load('lvlBG.png')



clock = pygame.time.Clock()

card1()






