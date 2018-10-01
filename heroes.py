#-------------------------------------------------------------------------#
# Hero Simulator v0.05-alpha                                              #
# By Douglas J. Honeycutt                                                 #
# https://withacact.us/ | https://github.com/RidleyofZebes/hero-simulator #
#-------------------------------------------------------------------------#

#imports...
import os
import pickle # <-- The thing that lets the save/load function work. Favorite module name.
import sys # <-- Literally only using this one for the sys.exit command. If it's ever deprecated, remove this.
from random import randint # <-- LulZ S000 RaNdUm

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
	
	def attack(self):
		print("attack")
	
class Hero:
	name = ""
	level = ""
	hp = ""
	xp = 0
	killcount = 0
	encounter = 0
	accuracy = ""
	attack = ""
	armor = ""
	speed = ""
	
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
rat.xp = 150

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
hero.accuracy = 5
hero.attack = 5
hero.armor = 12
hero.speed = 5
hero.killcount = 0
hero.encounter = 0
hero.xp = 0
# D&D5e Hero Stats - don't know if they'll be used yet, but they're here for reference.
# Eventually, if it would be simpler, I'd like to see everything done like this.
# hero.str = ""
# hero.dex = ""
# hero.con = ""
# hero.int = ""
# hero.wis = ""
# hero.cha = ""

# Functions?!
def test():
	print("<<<<TESTING FOR DEV PURPOSES PLEASE IGNORE>>>>")

def game_menu():
	menu = input("[save, load, back, quit]\n")
	if menu == 'quit':
		menusave = input("Would you like to save your progress? [y, n]\n")
		if menusave == 'y':
			Save_Game()
		print("Fare thee well, " + hero.name + "...")
		print("In the end, you slew " + str(hero.killcount) + " monsters and earned " + str(hero.xp) + "xp.") # display scores here
		sys.exit()
	elif menu == 'save':
		Save_Game()
	elif menu == 'load':
		Load_Game()

def enemy_attack():
	if (randint(1, 20) + enemy.accuracy) > hero.armor: # 1d20 + enemy accuracy vs. hero's armor class
		mobattack = (randint(1, 10) + enemy.attack) # 1d10 + enemy attack bonus
		hero.hp = hero.hp - mobattack
		print("The " + enemy.name + " strikes you for " + str(mobattack) + " damage, leaving you with " + str(hero.hp) + " health!")
	else:
		print("You narrowly avoid the " + enemy.name + "'s blow!")
		
def hero_attack():
	if (randint(1, 20) + hero.accuracy) > enemy.armor:
		attack = (randint(1, 10) + hero.attack)
		enemy.hp = enemy.hp - attack
		print("You deal a mighty blow, causing " + str(attack) + " damage, leaving it with " + str(enemy.hp) + " health!")		
	else:
		print("Your attack is stopped by the " + enemy.name + "'s defenses!")

def hero_death():
	print("I'm sorry " + hero.name + ", you appear to have died.")
	print("In the end, you enountered " + str(hero.encounter) + " monsters, slew " + str(hero.killcount) + " of them, and earned " + str(hero.xp) + "xp.")
	sys.exit()
	
def enemy_death():
	print("The " + enemy.name + " is slain!")
	hero.xp = hero.xp + enemy.xp # Grant hero experience points
	hero.killcount = hero.killcount + 1 # Add up the kill count
	print("You gain " + str(enemy.xp) + "xp, for a total of " + str(hero.xp) + "xp!") # Then tell the player
	# print("<<<DEV: resetting " + enemy.name + " to " + str(enemy.maxhp) + ".>>>") # This is just so I can make sure it's working. !!!!Deprecated, comented out!!!!
	enemy.hp = enemy.maxhp
	
def combat_encounter():
	combat = True
	while combat:
		action = input("What will you do? \n [attack, run, wait] \n") # get the player input
		if action == "attack":
			print("You trade blows with the " + enemy.name + "!")
			if randint(1, hero.speed) < randint(1, enemy.speed): # if the enemy is faster...
				print("The " + enemy.name + " is quick on their feet!")
				enemy_attack()
				if hero.hp <= 0:
					hero_death()
				hero_attack()
				if enemy.hp <= 0: # If the enemy is dead...
					enemy_death()
					combat = False
			else:
				print("You have the upper hand!")
				hero_attack()					
				if enemy.hp <= 0: # If the enemy is dead...
					enemy_death()
					combat = False
				else:
					enemy_attack()
					if hero.hp <= 0:
						hero_death()
		elif action == "run":
			if randint(1, hero.speed) < randint(1, enemy.speed): # hero speed vs monster speed, if monster speed greater than hero speed, monster attack before flee.
				print("You turn to run, but you are not fast enough!")
				enemy_attack()
				if hero.hp <= 0:
					hero_death()
			else:
				print("You turn to run, escaping nimbly into the darkness. \nYour body is uninjured, but your pride has taken a mortal blow.")
				combat = False
		elif action == "wait":
			print("After a moment of uncertainty, the " + enemy.name + " strikes!")
			enemy_attack()	
			if hero.hp <= 0:
				hero_death()
	
def Save_Game():
	player = {'name':hero.name, 'hp':str(hero.hp), 'xp':str(hero.xp), 'kills':str(hero.killcount), 'encounters':str(hero.encounter)}
	with open('save/savegame.sav', 'wb') as f:
		pickle.dump(player, f)
	print("Game saved.")
		
def Load_Game():
	with open('save/savegame.sav', 'rb') as f:
		player = pickle.load(f)
	hero.name = player['name']
	hero.hp = int(player['hp'])
	hero.xp = int(player['xp'])
	hero.killcount = int(player['kills'])
	hero.encounter = int(player['encounters'])
	print("Ah, " + hero.name + ", it's good to see you again!")
	
# Begin game text and collect hero name
print("Welcome, Hero! Your destiny awaits.")
returning = input("Have we met before? \n [yes, no] \n")
if returning == 'yes':
	Load_Game()
else:	
	hero.name = input("What may we call you? ")
	print("Then welcome, " + hero.name + ", may the Gods guide you in your trials.")
	input("Press Enter to continue...")
	os.system('cls')
# Begin the Adventure
quest = True
while quest:
	cf = randint(0,1)
	vo = input("Venture onward, " + hero.name + "? \nOr do you seek rest? \n [quest, menu, stop] \n")
	if vo == 'stop':
		print("Fare thee well, " + hero.name + "...")
		print("In the end, you enountered " + str(hero.encounter) + " monsters, slew " + str(hero.killcount) + " of them, and earned " + str(hero.xp) + "xp.") # display scores here
		sys.exit()
	elif vo == 'menu':
		game_menu()
	elif vo == 'quest':
		cf = randint(0,2) # Determine the type of encounter. As it stands, 0 = nothing, 1 = monster, 2 = chest, 3 = trap
		if cf == 0: # Nothing encountered
			print("The coast is clear... for now.")
		elif cf == 1: # Monster encounter!
			e = (randint(0,4)) # picks a random number, 0 - 4
			enemy = monsterList[(e)] # get random enemy
			print("A " + enemy.name + " has appeared!")
			hero.encounter = hero.encounter + 1
			combat_encounter()
		elif cf == 2: # Chest encounter!
			print("You see a large, iron-bound chest before you. What will you do?")
			cc = input("[open, leave, menu]")
			if cc == 'open':
				m = randint(0,1)
				if m == 0:
					test() #chest
				if m == 1: # MIMIC!!!
					print("As you attempt to pull back the lid of the chest, you feel a sticky secretion covering your hand. You pull back in disgust just as the lid opens of its own accord, revealing a full set of teeth in a gaping, slimy maw!")
					enemy = mimic
					print("A " + enemy.name + " has appeared!")
					hero.encounter = hero.encounter + 1
					combat_encounter()
			elif cc == 'leave':
				print("You decide that it's best to leave well enough alone.")
			elif cc == 'menu':
				game_menu()
		elif cf == 3: # Trap encounter! [NOT USED AT THIS TIME]
			print("You see a large, iron-bound chest before you. What will you do?")
			cc = input("[open, leave, menu]")
			if cc == 'open':
				m = randint(0,1)
			elif cc == 'leave':
				combat = False
			elif cc == 'menu':
				game_menu()
