

# include pygame
import pygame
import random

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
monster_image = pygame.image.load("images/monster.png")



hero = {
	"x": 100,
	"y": 100,
	"speed": 5,
	"wins": 0
}


goblin = {
	"x": 200,
	"y": 200,
	"speed": 5
}

monster = {
	"x": 300,
	"y": 300,
	"speed": 1
}

hidden_coin = {
	"x": 100,
	"y": 400
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
tick = 0 # (tick += 1) (if tick % 20 == 0 ) you can make the monster move only every 20 ticks
while game_on:
	direction_decider = random.randint(0,1); # decide whether to change x direction or y direction
	random_movement = random.randint(-1,1); # decide whether to move positive direction or negative direction
	moving_positive_direction = random.randint(0,1); # movement for positive direction only
	moving_negative_direction = random.randint(-1,0); # movement for negative direction only

	if(direction_decider == 0 and monster["x"] >= 500):
		monster["x"] += monster["speed"] * moving_negative_direction
	elif(direction_decider == 0 and monster["x"] <= 12):
		monster["x"] += monster["speed"] * moving_positive_direction
	elif(direction_decider == 1 and monster["y"] >= 460):
		monster["y"] += monster["speed"] * moving_negative_direction
	elif(direction_decider == 1 and monster["y"] <= 20):
		monster["y"] += monster["speed"] * moving_positive_direction
	else:
		if(direction_decider == 0):
			monster["x"] += monster["speed"] * random_movement
		else:
			monster["y"] += monster["speed"] * random_movement

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
	if distance_between < 50:
		print "Goblin Report : collision!"
		try_your_luck = random.randint(0,2); # you will be confused or moving faster!! Good luck!!
		if try_your_luck == 0:
			hero['speed'] = -5
		elif try_your_luck == 1:
			hero['speed'] = 5
		else:
			hero['speed'] = 20
	else:
		print "Goblin Report : not touching"

	strange_distance = fabs(hero['x'] - hidden_coin['x']) + fabs(hero['y'] - hidden_coin['y'])
	if strange_distance < 50:
		try_your_luck_hard = random.randint(0,2);
		print "uhhhhh what is going on?"
		if(strange_distance == 0): # you will be teleported. uhh btw you will be really really slow 
			hero['x'] = 400
			hero['y'] = 400
			hero['speed'] = 1
		elif(strange_distance == 1): # how did monster get a steroided energy juice?
			monster['speed'] = 5000000
		else:
			hero_image = pygame.image.load("images/monster.png") # you will look like a hot monster!


	danger_distance = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
	if danger_distance < 50:
		print "I need to be stronger :("
		game_on = False
		play_again = raw_input("Play again? yes or no?")
		print "Monster Report : danger!"
		print play_again
		if(play_again == "yes"):
			game_on = True
			monster['x'] = 300
			monster['y'] = 300
			hero['x'] = 100
			hero['y'] = 100
			hero['speed'] = 5
		else:
			game_on = False
	else:
		print "Monster Report : so far so good!"




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
	pygame_screen.blit(monster_image,[monster["x"],monster["y"]])

# fill in the screen with a color (or image)
# repeat 6 over and over and over ...
	pygame.display.flip()

