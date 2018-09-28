#-------------------------------------------------------------------------
# Hero Simulator v0.1alpha                                               #
# By Douglas J. Honeycutt                                                #
# https://withacact.us/                                                  #
#-------------------------------------------------------------------------

#imports...
import os
import sys
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
	hp = ""
	accuracy = ""
	attack = ""
	armor = ""
	init = ""
	
# Define a few sample monsters
goblin = Monster()
goblin.name = "Goblin"
goblin.hp = 15
goblin.attack = "1d6"
goblin.armor = 13
goblin.init = 17

slime = Monster()
slime.name = "Slime"
slime.hp = 30
slime.attack = "1d6"
slime.armor = 5
slime.init = 7

rat = Monster()
rat.name = "Rat"
rat.hp = 10
rat.attack = "1d4"
rat.armor = 5
rat.init = 10

monsterList = (goblin, slime, rat)

# Basic Hero stats
hero = Hero()
hero.name = ""
hero.hp = 100
hero.accuracy = 20
hero.attack = 10
hero.armor = 15
hero.init = 20

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
			e = (randint(0,10))
			if e >= 3:
				print("The coast is clear... for now.")
				vo = input("Venture onward, " + hero.name + "? ")
				if vo == 'n':
					game = False
					sys.exit("Fare thee well, coward...")
					# display scores here
			else:
				enemy = monsterList[(e)]
				print("A " + enemy.name + " has appeared!")
				while enemy.hp > 0:
					action = input("What will you do? ")
					if action == "attack":
						print("you trade blows with the " + enemy.name + "!")
						if hero.accuracy > enemy.armor:
							attack = randint(1, hero.attack)
							enemy.hp = enemy.hp - attack
							print("You deal a mighty blow, causing " + str(attack) + " damage, leaving it with " + str(enemy.hp) + " health!")
					elif action == "run":
						then() # hero speed vs monster speed, if monster speed greater than hero speed, monster attack before flee.
					elif action == "wait":
						then() # monster action

	