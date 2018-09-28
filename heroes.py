#-------------------------------------------------------------------------
# Hero Simulator v0.02alpha                                              #
# By Douglas J. Honeycutt                                                #
# https://withacact.us/                                                  #
#-------------------------------------------------------------------------

#imports...
import os
import sys # <-- Literally only using this one for the sys.exit command. If it's ever deprecated, remove this.
from random import randint

# Define the Monster object and Hero object
class Monster:
	name = ""
	hp = ""
	attack = ""
	armor = ""
	init = ""
	
	def attack(self):
		print("attack")
	
class Hero:
	name = ""
	level = ""
	hp = ""
	xp = 0
	accuracy = ""
	attack = ""
	armor = ""
	init = ""
	
# Define a few sample monsters
goblin = Monster()
goblin.name = "Goblin"
goblin.hp = 15
goblin.attack = 6
goblin.armor = 13
goblin.init = 17
goblin.xp = 300

slime = Monster()
slime.name = "Slime"
slime.hp = 30
slime.attack = 6
slime.armor = 5
slime.init = 7
slime.xp = 250

rat = Monster()
rat.name = "Rat"
rat.hp = 10
rat.attack = 4
rat.armor = 5
rat.init = 10
rat.xp = 150

bandit = Monster()
bandit.name = "Bandit"
bandit.hp = 40
bandit.attack = 8
bandit.armor = 17
bandit.init = 15
bandit.xp = 600


monsterList = (goblin, slime, rat, bandit)

# Basic Hero stats
hero = Hero()
hero.name = ""
hero.hp = 100
hero.accuracy = 20
hero.attack = 10
hero.armor = 15
hero.init = 15
# D&D5e Hero Stats - don't know if they'll be used yet, but they're here for reference.
# Eventually, if it would be simpler, I'd like to see everything done like this.
hero.str = ""
hero.dex = ""
hero.con = ""
hero.int = ""
hero.wis = ""
hero.cha = ""

# Begin game text and collect hero name
game = True
while game:
	print("Welcome, Hero! Your destiny awaits.")
	hero.name = input("What may we call you? ")
	print("Then welcome, " + hero.name + ", may the Gods guide you in your trials.")
	input("Press Enter to continue...")
	os.system('cls')

	vf = input("Venture forth, " + hero.name + "? ")
	if vf == 'n':
		game = False
		sys.exit("Fare thee well, coward...")
		# display scores here
	else:
		quest = True
		while quest:
			e = (randint(0,10)) # picks a random number, 1 - 10
			if e >= 4: # Numbers 0, 1, 2, & 3 correspond to mobs in the monsterList. 4 and above, no monster. Adds suspense?
				print("The coast is clear... for now.")
				vo = input("Venture onward, " + hero.name + "? ")
				if vo == 'n':
					game = False
					sys.exit("Fare thee well, coward...") # <-- Need to change that. Should be hero name, but why quit before you encounter your first monster?
					# display scores here
			else:
				enemy = monsterList[(e)] # get random enemy
				print("A " + enemy.name + " has appeared!")
				while enemy.hp > 0: # check if the enemy is still alive
					action = input("What will you do? \n [attack, run, wait] \n") # get the player input
					if action == "attack":
						print("you trade blows with the " + enemy.name + "!")
						if randint(1, hero.init) < randint(1, enemy.init): # if the enemy is faster...
							print("The " + enemy.name + " is quick on their feet!")
							if randint(1, 20) > hero.armor: # enemy gets a random attack bonus. Need a stat to actually give bonus later.
								mobattack = (randint(1, 20) + enemy.attack)
								hero.hp = hero.hp - mobattack
								print("The " + enemy.name + " strikes you for " + str(mobattack) + " damage, leaving you with " + str(hero.hp) + " health!")
							else:
								print("You narrowly avoid the " + enemy.name + "'s blow! ")
						else:
							print("You have the upper hand!")
						if hero.accuracy > enemy.armor:
							attack = randint(1, hero.attack)
							enemy.hp = enemy.hp - attack
							print("You deal a mighty blow, causing " + str(attack) + " damage, leaving it with " + str(enemy.hp) + " health!")
						
					elif action == "run":
						then() # hero speed vs monster speed, if monster speed greater than hero speed, monster attack before flee.
					elif action == "wait":
						then() # monster action

	