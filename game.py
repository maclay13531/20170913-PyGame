

# include pygame
import pygame

#from the math module(built into python) get the fabs method

from math import fabs

# init pygame
pygame.init()
# create a screen with a particular size
screen_size = (512,480) #screen_size MUST be a tuple
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load("images/background.png")
hero_image = pygame.image.load("images/hero.png")
goblin_image = pygame.image.load("images/goblin.png")



hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0
}


goblin = {
	"x": 200,
	"y": 200,
	"speed": 20
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276 
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

# create a game loop (while)
game_on = True
while game_on:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			game_on = False
		elif(event.type == pygame.KEYDOWN):
			if(event.key == keys["up"]):
				#hero['y'] -= hero["speed"]
				keys_down["up"] = True
			elif(event.key == keys["down"]):
				#hero['y'] += hero["speed"]
				keys_down["down"] = True
			elif(event.key == keys["left"]):
				#hero['x'] -= hero["speed"]
				keys_down["left"] = True
			elif(event.key == keys["right"]):
				#hero['x'] += hero["speed"]
				keys_down["right"] = True
		elif event.type == pygame.KEYUP:
			if event.key == keys['up']:
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['right']:
				keys_down['right'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
	if keys_down["up"]:
		hero['y'] -= hero["speed"]
	elif keys_down["down"]:
		hero['y'] += hero["speed"]
	if keys_down["left"]:
		hero['x'] -= hero["speed"]
	elif keys_down["right"]:
		hero['x'] += hero["speed"]

	#collision detection!!
	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_between < 32:
		print "collision!"
	else:
		print "not touching"


# add a quit event (python needs an escape)
# blit takes 2 arguments
	# 1. what do you want to draw?
	# 2. where do you want to draw?
	pygame_screen.blit(background_image,[0, 0])

	font = pygame.font.Font(None, 25)
	wins_text = font.render("wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])

	pygame_screen.blit(hero_image,[hero["x"],hero["y"]])
	pygame_screen.blit(goblin_image,[goblin["x"],goblin["y"]])

# fill in the screen with a color (or image)
# repeat 6 over and over and over ...
	pygame.display.flip()

