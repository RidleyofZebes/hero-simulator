#-------------------------------------------------------------------------
# Hero Simulator v0.03alpha                                              #
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
	speed = ""
	
	def attack(self):
		print("attack")
	
class Hero:
	name = ""
	level = ""
	hp = ""
	xp = 0
	killcount = 0
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
goblin.armor = 13
goblin.speed = 17
goblin.xp = 300

slime = Monster()
slime.name = "Slime"
slime.hp = 30
slime.maxhp = 30
slime.attack = 6
slime.armor = 5
slime.speed = 7
slime.xp = 250

rat = Monster()
rat.name = "Rat"
rat.hp = 10
rat.maxhp = 10
rat.attack = 4
rat.armor = 5
rat.speed = 10
rat.xp = 150

bandit = Monster()
bandit.name = "Bandit"
bandit.hp = 40
bandit.maxhp = 40
bandit.attack = 8
bandit.armor = 17
bandit.speed = 15
bandit.xp = 600

dragon = Monster()
dragon.name = "Dragon"
dragon.hp = 500
dragon.maxhp = 500
dragon.attack = 20
dragon.armor = 20
dragon.speed = 10
dragon.xp = 10000

monsterList = (goblin, slime, rat, bandit, dragon)

# Basic Hero stats
hero = Hero()
hero.name = ""
hero.hp = 100
hero.accuracy = 20
hero.attack = 10
hero.armor = 15
hero.speed = 15
hero.killcount = 0
# D&D5e Hero Stats - don't know if they'll be used yet, but they're here for reference.
# Eventually, if it would be simpler, I'd like to see everything done like this.
hero.str = ""
hero.dex = ""
hero.con = ""
hero.int = ""
hero.wis = ""
hero.cha = ""

# Functions?!
def enemy_attack():
	if randint(1, 20) > hero.armor: # random attack bonus.
		mobattack = (randint(1, 20) + enemy.attack)
		hero.hp = hero.hp - mobattack
		print("The " + enemy.name + " strikes you for " + str(mobattack) + " damage, leaving you with " + str(hero.hp) + " health!")
	else:
		print("You narrowly avoid the " + enemy.name + "'s blow! ")
		
def hero_attack():
	if hero.accuracy > enemy.armor:
		attack = randint(1, hero.attack)
		enemy.hp = enemy.hp - attack
		print("You deal a mighty blow, causing " + str(attack) + " damage, leaving it with " + str(enemy.hp) + " health!")		

def hero_death():
	print("I'm sorry " + hero.name + ", you appear to have died.")
	game = False
	print("In the end, you slew " + str(hero.killcount) + " monsters and earned " + str(hero.xp) + "xp.")
	sys.exit()
	
def enemy_death():
	print("The " + enemy.name + " is slain!")
	hero.xp = hero.xp + enemy.xp # Grant hero experience points
	hero.killcount = hero.killcount + 1 # Add up the kill count
	print("You gain " + str(enemy.xp) + "xp, for a total of " + str(hero.xp) + "xp!") # Then tell the player
	print("<<<DEV: resetting " + enemy.name + " to " + str(enemy.maxhp) + ".>>>") # This is just so I can make sure it's working.
	enemy.hp = enemy.maxhp
	
#def Save_Game():
	
#def Load_Game():

# Begin game text and collect hero name
game = True
while game:
	print("Welcome, Hero! Your destiny awaits.")
	hero.name = input("What may we call you? ")
	print("Then welcome, " + hero.name + ", may the Gods guide you in your trials.")
	input("Press Enter to continue...")
	os.system('cls')
	# Begin the Adventure
	vf = input("Venture forth, " + hero.name + "? ")
	if vf == 'n':
		print("Fare thee well, coward...")
		# display scores here
	else:
		quest = True
		while quest:
			e = (randint(0,10)) # picks a random number, 1 - 10
			if e >= 5: # Numbers 0, 1, 2, 3, & 4 correspond to mobs in the monsterList. 5 and above, no monster. Adds suspense?
				print("The coast is clear... for now.")
				vo = input("Venture onward, " + hero.name + "? ")
				if vo == 'n':
					print("Fare thee well, " + hero.name + "...")
					print("In the end, you slew " + str(hero.killcount) + " monsters and earned " + str(hero.xp) + "xp.")		
					sys.exit()
			else:
				enemy = monsterList[(e)] # get random enemy
				print("A " + enemy.name + " has appeared!")
				while enemy.hp > 0: # check if the enemy is still alive
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
								break
						else:
							print("You have the upper hand!")
							hero_attack()					
							if enemy.hp <= 0: # If the enemy is dead...
								enemy_death()
								break
							else:
								enemy_attack()
								if hero.hp <= 0:
									hero_death()
					elif action == "run":
						if randint(1, hero.speed) < randint(1, enemy.speed): # hero speed vs monster speed, if monster speed greater than hero speed, monster attack before flee.
							print("You turn to run, but you are not fast enough!")
							enemy_attack()
						else:
							print("You turn to run, escaping nimbly into the darkness. \n Your body is uninjured, but your pride has taken a mortal blow.")
							break
					elif action == "wait":
						print("After a moment of uncertainty, the " + enemy.name + " strikes!")
						enemy_attack()	
						if hero.hp <= 0:
							hero_death()