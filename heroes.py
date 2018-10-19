#-------------------------------------------------------------------------#
# Hero Simulator v0.1.2-dev                                               #
# By Douglas J. Honeycutt                                                 #
# https://withacact.us/ | https://github.com/RidleyofZebes/hero-simulator #
#-------------------------------------------------------------------------#

#imports...
import os
import pickle # <-- The thing that lets the save/load function work. Favorite module name.
import pygame
import pygame_textinput
from random import randint # <-- LulZ S000 RaNdUm
from natural.number import ordinal # <-- Makes the numbers look pretty - 1st, 2nd, 3rd, 4th...

version = "v0.1.2-dev"
window_res = (800, 600)
FPS = 30

pygame.init() # <-- This is what starts it all...

# Game Window Setup

game_window = pygame.display.set_mode(window_res)
#window_top = pygame.Surface((window_res[0], window_res[1] / 2))
#window_bot = pygame.Surface((window_res[0], window_res[1] / 2))
#win_top_xy = (0, 0)
#win_bot_xy = (0, window_res[1] / 2)

pygame.mouse.set_visible(1)

pygame.display.set_caption('Hero Simulator ' + version)
window_icon = pygame.image.load("res/icon.png").convert_alpha() 
pygame.display.set_icon(window_icon)

clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Font(s)
font = pygame.font.Font('res/alkhemikal.ttf', 28)

# Images
menubtn = pygame.image.load('res/menu.png')
#monsterico = pygame.image.load('res/monster.png')


# PyGame Functions

def cls():
	game_window.fill(black)
	pygame.draw.rect(game_window, white, (25,300,750,275), 0)
	pygame.draw.rect(game_window, black, (29,304,742,267), 0)

def mb_clear():
	game_window.fill(black)
	pygame.draw.rect(game_window, white, (25,300,750,275), 0)
	pygame.draw.rect(game_window, black, (29,304,742,267), 0)

def pyButton(butnPos, butnText, *butnWid): # Gets button X,Y and button label
		buttonPadding = 25 # Set padding between button text and border
		label = font.render(butnText, 0, white) # Renders button label
		butnDimsX, butnDimsY = label.get_size() # Sends button label dimensions to A,B variables
		if not butnWid:
			game_window.blit(label, ((butnPos[0] + (buttonPadding/2)),(butnPos[1] + (buttonPadding/2)))) # Outputs the button with default padding to the screen
			butnSize = (butnPos[0],butnPos[1],(butnDimsX + buttonPadding),(butnDimsY + (buttonPadding*0.8)))
		else:
			game_window.blit(label, ((((butnPos[0] + ((butnWid[0]+buttonPadding)/2)))-(butnDimsX/2)), (butnPos[1] + (buttonPadding/2)))) # Outputs the button with padding and centered text to the screen
			butnSize = (butnPos[0],butnPos[1],(butnWid[0] + buttonPadding),(butnDimsY + (buttonPadding*0.8)))
		pygame.draw.rect(game_window, white, butnSize, 4)
		return pygame.Rect(butnSize)
		
def pyNameplate(butnPos, butnText, *butnWid): # Gets button X,Y and button label
		buttonPadding = 25 # Set padding between button text and border
		label = font.render(butnText, 0, white) # Renders button label
		butnDimsX, butnDimsY = label.get_size() # Sends button label dimensions to A,B variables
		if not butnWid:
			game_window.blit(label, ((butnPos[0] + (buttonPadding/2)),(butnPos[1] + (buttonPadding/2)))) # Outputs the button with default padding to the screen
			butnSize = (butnPos[0],butnPos[1],(butnDimsX + buttonPadding),(butnDimsY + (buttonPadding*0.8)))
		else:
			game_window.blit(label, ((((butnPos[0] + ((butnWid[0]+buttonPadding)/2)))-(butnDimsX/2)), (butnPos[1] + (buttonPadding/2)))) # Outputs the button with padding and centered text to the screen
			butnSize = (butnPos[0],butnPos[1],(butnWid[0] + buttonPadding),(butnDimsY + (buttonPadding*0.8)))
		pygame.draw.rect(game_window, white, butnSize, 4)
		return pygame.Rect(butnSize)
	
def message(text, *texloc, color=white):
	words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
	space = font.size(' ')[0]  # The width of a space.
	max_width, max_height = 750, 300
	if not texloc:
		pos = 40, 315
	else:
		pos = texloc
	x, y = pos
	for line in words:
		for word in line:
			word_surface = font.render(word, 0, color)
			word_width, word_height = word_surface.get_size()
			if x + word_width >= max_width:
				x = pos[0]  # Reset the x.
				y += word_height  # Start on new row.
			game_window.blit(word_surface, (x, y))
			x += word_width + space
		x = pos[0]  # Reset the x.
		y += word_height  # Start on new row.
		
# Define the Monster object and Hero object
class Monster:
	name = ""
	hp = ""
	maxhp = ""
	attack = ""
	accuracy = ""
	armor = ""
	speed = ""
	xp = ""
	
	# def attack(self):
		# print("attack")
	
class Hero:
	name = ""
	level = 0
	hp = ""
	xp = 0
	killcount = 0
	encounter = 0
	accuracy = ""
	attack = ""
	armor = ""
	speed = ""
	
	# def levelup():
		# if xp 
	
# Define a few sample monsters
goblin = Monster()
goblin.name = "Goblin"
goblin.hp = 15
goblin.maxhp = 15
goblin.attack = 6
goblin.accuracy = 5
goblin.armor = 13
goblin.speed = 17
goblin.xp = 300

slime = Monster()
slime.name = "Slime"
slime.hp = 30
slime.maxhp = 30
slime.attack = 6
slime.accuracy = 5
slime.armor = 5
slime.speed = 7
slime.xp = 250

rat = Monster()
rat.name = "Rat"
rat.hp = 10
rat.maxhp = 10
rat.attack = 2
rat.accuracy = 5
rat.armor = 5
rat.speed = 10
rat.xp = 50

bandit = Monster()
bandit.name = "Bandit"
bandit.hp = 40
bandit.maxhp = 40
bandit.attack = 8
bandit.accuracy = 5
bandit.armor = 17
bandit.speed = 15
bandit.xp = 600

dragon = Monster()
dragon.name = "Dragon"
dragon.hp = 500
dragon.maxhp = 500
dragon.attack = 20
dragon.accuracy = 5
dragon.armor = 20
dragon.speed = 10
dragon.xp = 10000

mimic = Monster()
mimic.name = "Mimic"
mimic.hp = 75
mimic.maxhp = 75
mimic.attack = 7
mimic.accuracy = 5
mimic.armor = 13
mimic.speed = 10
mimic.xp = 400

monsterList = (goblin, slime, rat, bandit, dragon)

# Basic Hero stats
hero = Hero()
hero.name = "Nameless"
hero.hp = 100
hero.maxhp = 100
hero.temphp = 0
hero.accuracy = 5
hero.attack = 5
hero.armor = 12
hero.speed = 5
hero.killcount = 0
hero.encounter = 0
hero.gametime = 0
hero.xp = 0
hero.lvl = 1
hero.gold = 0
# D&D5e Hero Stats - don't know if they'll be used yet, but they're here for reference.
# Eventually, if it would be simpler, I'd like to see everything done like this.
# hero.str = 0
# hero.dex = 0
# hero.con = 0
# hero.wis = 0
# hero.cha = 0
# hero.lck = 0

	
# Game Logic Functions
prompt = pygame_textinput.TextInput('', 'res/alkhemikal.ttf', 28, False, white, white, 1000, 100)

def test():
	message("<<<<TESTING FOR DEV PURPOSES PLEASE IGNORE>>>>", 20, 20)
	pygame.display.update()
	
def game_menu():
	menuCheck = True
	while menuCheck:
		menuEvents = pygame.event.get()
		for event in menuEvents:
			if event.type == pygame.QUIT:
				stopped = True
			message("MENU", 362,15)
			msave = pyButton((130,50), "Save", 100)
			mload = pyButton((265,50), "Load", 100)
			mback = pyButton((400,50), "Back", 100)
			mquit = pyButton((535,50), "Quit", 100)
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				if msave.collidepoint(pos):
					Save_Game()
				elif mload.collidepoint(pos):
					Load_Game()
				elif mback.collidepoint(pos):
					menuCheck = False
				elif mquit.collidepoint(pos):
					save_n_quit()
			pygame.display.update()
			
def save_n_quit():
	saveYN = True
	while saveYN:
		smenuEvents = pygame.event.get()
		for event in smenuEvents:
			if event.type == pygame.QUIT:
				stopped = True
			cls()				
			message("Would you like to save your progress?")
			mYsave = pyButton((40,380), "Yes", 100)
			mNsave = pyButton((175,380), "No", 100)
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				if mYsave.collidepoint(pos):
					Save_Game()
					cls()
					message("Fare thee well, " + hero.name + "...\nIn the end, you slew " + str(hero.killcount) + " monsters and earned " + str(hero.xp) + "xp.\n\nClick anywhere to leave.") # display scores here	
					pygame.display.update()
					wait()
					os._exit(1)
				elif mNsave.collidepoint(pos):
					cls()
					message("Fare thee well, " + hero.name + "...\nIn the end, you slew " + str(hero.killcount) + " monsters and earned " + str(hero.xp) + "xp.\n\nClick anywhere to leave.") # display scores here	
					pygame.display.update()
					wait()
					os._exit(1)

def enemy_attack():
	cls()
	if (randint(1, 20) + enemy.accuracy) > (hero.armor * hero.lvl): # 1d20 + enemy accuracy vs. hero's armor class
		mobattack = (randint(1, 10) + enemy.attack) # 1d10 + enemy attack bonus
		hero.hp = hero.hp - mobattack
		message("The " + enemy.name + " strikes you for " + str(mobattack) + " damage, leaving you with " + str(hero.hp) + " health!")
		pygame.display.update()
		wait()
	else:
		message("You narrowly avoid the " + enemy.name + "'s blow!")
		pygame.display.update()
		wait()
		
def hero_attack():
	cls()
	if ((randint(1, 20) + hero.accuracy) * hero.lvl) > enemy.armor:
		attack = ((randint(1, 10) + hero.attack) * hero.lvl)
		enemy.hp = enemy.hp - attack
		message("You deal a mighty blow, causing " + str(attack) + " damage, leaving it with " + str(enemy.hp) + " health!")
		pygame.display.update()
		wait()
	else:
		message("Your attack is stopped by the " + enemy.name + "'s defenses!")
		pygame.display.update()
		wait()

def hero_death():
	cls()
	message("I'm sorry " + hero.name + ", you appear to have died.\nIn the end, you enountered " + str(hero.encounter) + " monsters, slew " + str(hero.killcount) + " of them, and earned " + str(hero.xp) + "xp.")
	pygame.display.update()
	wait()
	pygame.quit() #TODO: Needs to be continue/quit screen. Make a function.
	
def enemy_death():	
	hero.xp = hero.xp + enemy.xp # Grant hero experience points
	herolevelupcheck()
	hero.killcount = hero.killcount + 1 # Add up the kill count
	cls()
	message("The " + enemy.name + " is slain!\nYou gain " + str(enemy.xp) + "xp, for a total of " + str(hero.xp) + "xp!") # Then tell the player
	pygame.display.update()
	wait()
	enemy.hp = enemy.maxhp
	
def time_tick():
	# Game Calendar - May be more useful later?
	qcalen = ["Jannus","Quintest","Everborn","Sprynthane","Tavyris","Midsummers","Entmordaughn","Autumnus","Harvestone","Fallowfield","Winterholm"]
	qweekd = ["Sunstone", "Mondred", "Tuendala", "Wednyght", "Threasdon", "Frindaal", "Satterdawn"]
	qclock = ["12:00am", "1:00am", "2:00am", "3:00am", "4:00am", "5:00am", "6:00am", "7:00am", "8:00am", "9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm", "8:00pm", "9:00pm", "10:00pm", "11:00pm"]
	year = 1670
	mtod = 0
	mnth = 5
	days = 0
	hour = 7

	hour = hour + hero.gametime
	
	while hour >= len(qclock):
		hour = hour - len(qclock)
		days = days + 1
		mtod = mtod + 1	
	
	if days >= len(qweekd):
		days = days - len(qweekd)
	
	if mtod >= 31:
		mtod = 0
		mnth = mnth + 1
				
	if mnth >= len(qcalen):
		mnth = mnth - len(qcalen)
		year = year + 1
	
	global gamedate
	gamedate = (qweekd[days] + ", " + qcalen[mnth] + " " + ordinal(str(mtod + 1)) + ", " + str(year) + ", " + qclock[hour])
	return gamedate
	
def herolevelupcheck():
	nextlevel = 500 * (hero.lvl ** 2) - (500 * hero.lvl)
	if hero.xp >= nextlevel:
		hero.lvl = hero.lvl + 1
	
def display_stats():
	message(hero.name + ", lvl " + str(hero.lvl), 20, 10)
	message(str(hero.hp) + "hp", 20, 45)
	message(str(hero.xp) + "xp", 20, 80)
	time_tick()
	message(gamedate, 20, 115)
	
def combat_encounter():
	combat = True
	while combat:
		combatInput = pygame.event.get()
		for event in combatInput:
			cls()
			message(enemy.name, 20, 10)
			message(str(enemy.hp) + "hp", 20, 45)
			message(hero.name, 650, 10)
			message(str(hero.hp) + "hp", 650, 45)
			# monsterico = game_window.blit(monsterico,((game_window[1]/2)-50),200) # Eventually there will be a custom icon/portrait for every monster. I'll figure it out later.
			
			message("What will you do?") # get the player input
			cattack = pyButton((40,380), "Attack", 100)
			citem = pyButton((175,380), "Item", 100)
			cwait = pyButton((310,380), "Wait", 100)
			crun = pyButton((445,380), "Run", 100)
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				if cattack.collidepoint(pos):
					cls()
					message("You trade blows with the " + enemy.name + "!")
					pygame.display.update()
					wait()
					if randint(1, (hero.speed * hero.lvl)) < randint(1, enemy.speed): # if the enemy is faster...\
						message("\nThe " + enemy.name + " is quick on their feet!")
						pygame.display.update()
						wait()
						enemy_attack()
						if hero.hp <= 0:
							hero_death()
						hero_attack()
						if enemy.hp <= 0: # If the enemy is dead...
							enemy_death()
							combat = False
					else:
						message("\nYou have the upper hand!")
						pygame.display.update()
						wait()
						hero_attack()					
						if enemy.hp <= 0: # If the enemy is dead...
							enemy_death()
							combat = False
						else:
							enemy_attack()
							if hero.hp <= 0:
								hero_death()
				elif citem.collidepoint(pos):
					test()
				elif cwait.collidepoint(pos):
					cls()
					message("After a moment of uncertainty, the " + enemy.name + " strikes!")
					pygame.display.update()
					wait()
					enemy_attack()	
					if hero.hp <= 0:
						hero_death()
				elif crun.collidepoint(pos):				
					if randint(1, hero.speed) < randint(1, enemy.speed): # hero speed vs monster speed, if monster speed greater than hero speed, monster attack before flee.
						cls()
						message("You turn to run, but you are not fast enough!")
						pygame.display.update()
						wait()
						enemy_attack()
						if hero.hp <= 0:
							hero_death()
					else:
						cls()
						message("You turn to run, escaping nimbly into the darkness. \nYour body is uninjured, but you feel your pride has taken a mortal blow...")
						pygame.display.update()
						wait()
						combat = False
	
def wait():
	holding = True
	while holding:
		loadWait = pygame.event.get()
		for event in loadWait:
			if event.type == pygame.MOUSEBUTTONDOWN:
				holding = False
	
def Save_Game():
	player = {'name':hero.name, 'hp':str(hero.hp), 'xp':str(hero.xp), 'gold':str(hero.gold), 'kills':str(hero.killcount), 'encounters':str(hero.encounter), 'gametime':str(hero.gametime)}
	with open('save/savegame.sav', 'wb') as f:
		pickle.dump(player, f)
	message("Game saved.", 20, 20)
	pygame.display.update()
		
def Load_Game():
	with open('save/savegame.sav', 'rb') as f:
		player = pickle.load(f)
	hero.name = player['name']
	hero.hp = int(player['hp'])
	hero.xp = int(player['xp'])
	hero.gold = int(player['gold'])
	hero.killcount = int(player['kills'])
	hero.encounter = int(player['encounters'])
	hero.gametime = int(player['gametime'])
	cls()
	message("Ah, " + hero.name + ", it's good to see you again!")
	pygame.display.update()
	herolevelupcheck()
	
	
	
# Begin Main Game Function
def main():
	stopped = False
	while not stopped:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				stopped = True		
			cls()			
			message("Welcome, Hero! Your destiny awaits.\nHave we met before?")
			loadYes = pyButton((40,380), "Yes", 100)
			loadNo = pyButton((175,380), "No", 100)
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				if loadYes.collidepoint(pos):
					cls()					
					Load_Game()
					wait()
					quest()
				elif loadNo.collidepoint(pos):
					cls()						
					getName = True					
					while getName:
						nameGET = pygame.event.get()
						for event in nameGET:
							cls()
							message("What may we call you?")
							game_window.blit(prompt.get_surface(), (40, 380))
							pygame.display.update()
							clock.tick(FPS)
							if prompt.update(nameGET):
								hero.name = prompt.get_text()
								cls()
								message("Then welcome, " + hero.name + ", may the Gods guide you in your trials.\n\nClick to continue...")
								pygame.display.update()
								wait()
								quest()
	pygame.quit()

def quest():
	quest = True
	while quest:
		getQuest = pygame.event.get()
		for event in getQuest:
			cls()
			display_stats()
			message("Venture onward, " + hero.name + "? \nOr do you seek rest?")
			bquest = pyButton((40,380), "Quest", 100)
			btown = pyButton((175,380), "Town", 100)
			brest = pyButton((310,380), "Rest", 100)
			bwait = pyButton((500,380), "Wait", 100)
			bmenu = game_window.blit(menubtn,(730,20))
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				if brest.collidepoint(pos):
					if hero.hp < (hero.maxhp + hero.temphp):
						qlocation = "Wilderness" # This will soon match the terrain of the current quest.
						cls()
						message("You seek shelter in the " + qlocation + ", pulling together what little you can for comfort.")
						pygame.display.update()
						wait()
						rest = randint(0,3)
						if rest == 0:
							cls()
							message("To your pleasant surprise, you awake well rested and eager for the next adventure!")
							pygame.display.update()
							wait()
							hero.gametime = hero.gametime + 8
							hero.hp = hero.hp + (randint(10,25))
							if hero.hp > hero.maxhp:
								hero.hp = hero.maxhp
						elif rest == 1:
							cls()
							message("Feeling secure in your makeshift shelter you allow yourself to drift to sleep, completely unaware of the assailant approaching your position!")
							hero.gametime = hero.gametime + 1
							pygame.display.update()
							wait()
							combat_encounter()
						elif rest > 1:
							cls()
							message("You find rest difficult in the " + qlocation + "; you barely shut your eyes before you sense you are being watched. It is time to move on.")
							pygame.display.update()
							wait()
							hero.gametime = hero.gametime + 1
							hero.hp = hero.hp + (randint(0, 5))
							if hero.hp > hero.maxhp:
								hero.hp = hero.maxhp
					else:
						cls()
						message("You already feel fit as a fiddle! To rest now would be a waste of time.")
						pygame.display.update()
						wait()
				elif bmenu.collidepoint(pos):
					game_menu()				
				elif bwait.collidepoint(pos):
					hero.gametime = hero.gametime + 1
					pygame.display.update()
				elif btown.collidepoint(pos):
					test()
				elif bquest.collidepoint(pos):
					hero.gametime = hero.gametime + 1
					cf = randint(0,2) # Determine the type of encounter. As it stands, 0 = nothing, 1 = monster, 2 = chest, 3 = trap
					if cf == 0: # Nothing encountered
						cls()
						message("The coast is clear... for now.")
						pygame.display.update()
						wait()
					elif cf == 1: # Monster encounter!
						cls()
						e = (randint(0,4)) # picks a random number, 0 - 4
						global enemy # MAKE SURE "enemy" can be used GLOBALLY (ie. inside other functions). See those two words right there? Two words. Solved an hour headache.
						enemy = monsterList[(e)] # get random enemy						
						message("A " + enemy.name + " has appeared!")
						pygame.display.update()
						hero.encounter = hero.encounter + 1
						wait()
						combat_encounter()
					elif cf == 2: # Chest encounter!
						cls()
						message("You see a large, iron-bound chest before you. What will you do?")
						copen = pyButton((40,380), "Open the Chest", 200)
						cleave = pyButton((275,380), "Leave it be", 200)
						pygame.display.update()
						cquest = True
						while cquest:
							getChest = pygame.event.get()
							for event in getChest:
								if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
									pos = pygame.mouse.get_pos()
									if copen.collidepoint(pos):
										m = randint(0,2)
										if m == 0:
											cls()
											message("You ease back the lid of the chest. Your eyes are immediately dazzled by the glint and glitter of a mound of unimaginable loot!")
											pygame.display.update()
											hero.xp = hero.xp + 1000
											herolevelupcheck()
											hero.gold = hero.gold + 1000
											wait()
											cquest = False
										if m == 1:
											cls()
											message("Knocking aside the rust-eaten lock, you swing back the lid of the old chest. The heavy, old lid snaps off its hinges under it's own weight. Inside you find naught but cobwebs and dust.\nThe chest is empty.")
											pygame.display.update()
											hero.xp = hero.xp + 50
											herolevelupcheck()
											wait()
											cquest = False
										if m == 2: # MIMIC!!!
											enemy = mimic
											cls()
											message("As you attempt to pull back the lid of the chest, you feel a sticky secretion covering your hand. You pull back in disgust just as the lid opens of its own accord, revealing a full set of teeth in a gaping, slimy maw!\nA " + enemy.name + " has appeared!")
											pygame.display.update()
											hero.encounter = hero.encounter + 1
											wait()
											combat_encounter()
											cquest = False
									elif cleave.collidepoint(pos):
										cls()
										message("You decide that it's best to leave well enough alone.")
										pygame.display.update()
										wait()
										cquest = False
									elif bmenu.collidepoint(pos):
										game_menu()
					# elif cf == 3: # Trap encounter! [NOT USED AT THIS TIME]
						# print("You see a large, iron-bound chest before you. What will you do?")
						# cc = input("[open, leave, menu]")
						# if cc == 'open':
							# m = randint(0,1)
						# elif cc == 'leave':
							# combat = False
						# elif cc == 'menu':
							# game_menu()
	
	
# Launches the Game
	
main()
	

#Notes:
#Window is 800x600px, textbox is 750x275px, positioned 25px away from each edge.
#window border is 4px @ 800x600
#do math to figure out how that works in fullscreen.
	