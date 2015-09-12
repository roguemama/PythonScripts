import random
import time

class Dragon(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Hero(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power
		
def intro(name):
    print ""
    print "Hello! What is your hero's name?"
    name = raw_input()
    return name
	
def d_diff(ddiff):
    print ""
    print "Do you fight easy, medium, or hard dragons? (Enter e, m, or h.)"
    d_difficulty = raw_input()
    difficulty = ''
    if d_difficulty.lower() == 'e':
        difficulty = 'e'
    elif d_difficulty.lower() == 'm':
        difficulty = 'm'
    elif d_difficulty.lower() == 'h':
        difficulty = 'h'
    else:
        print "Bad entry! Your dragon is hard."
        difficulty = 'h'
    return difficulty

def h_class(hc):
    print ""
    print "Are you a warrior or a rogue? (Either w or r.)"
    her_class = raw_input()
    hero_class = ''
    if her_class.lower() == 'w':
        hero_class = 'w'
    elif her_class.lower() == 'r':
        hero_class = 'r'
    else:
        print "Bad entry! You're a rogue."
        hero_class = 'r'
    return hero_class

	
def drag(diff):
    if diff == 'e':
        dragon_power = dragon_e.power
    elif diff == 'm':
        dragon_power = dragon_m.power
    elif diff == 'h':
        dragon_power = dragon_h.power
    else:
        print "Doh! Try again."
    return dragon_power

def drag_h(diff):
    if diff == 'e':
        dragon_health = dragon_e.health
    elif diff == 'm':
        dragon_health = dragon_m.health
    elif diff == 'h':
        dragon_health = dragon_h.health
    else:
        print "Doh! Try again."
    return dragon_health

def hero_p(hpower):
    if hpower == 'w':
        hero_power = hero_w.power
    elif hpower == 'r':
        hero_power = hero_r.power
    else:
        print "Doh! Try again."
    return hero_power

def hero_h(hhealth):
    if hhealth == 'w':
        hero_health = hero_w.health
    elif hhealth == 'r':
        hero_health = hero_r.health
    else:
        print "Doh! Try again."
    return hero_health

def cont(bend):
    print "Would you like to battle again? (y or n)"
    cont = raw_input()
    if cont == 'y':
        battle(hero_name, dragon_health, dragon_power, hero_health, hero_power)
    elif cont == 'n':
        print "Goodbye!"
        return
    else:
        print "I didn't catch that. Try again later."
        return
        
def loot(difficulty, hero_class):
    if difficulty == 'e':
        prize_level = 'silver'
    elif difficulty == 'm':
        prize_level = 'gold'
    elif difficulty == 'h':
        prize_level = 'dragon'
    
    loot_roll = random.randrange(0,2)
    
    if loot_roll == 0:
        prize = 'weapon'
    elif loot_roll == 1:
        prize = 'armor'
    
    if hero_class == 'w' and prize == 'weapon':
        final_prize = prize_level + "sword"
    elif hero_class == 'w' and prize == 'armor':
        final_prize = "set of " + prize_level + " " + prize
    elif hero_class == 'r' and prize == 'weapon':
        final_prize = prize_level + "dagger"
    elif hero_class == 'r' and prize == 'armor':
        final_prize = "set of " + prize_level + " " + prize
    else:
        final_prize = 'pouch of coins'
    
    return final_prize
    

def battle(hero_name, dragon_health, dragon_power, hero_health, hero_power):
    rnd = 0
    while (dragon_health > 0 and hero_health > 0):
        rnd+=1
        print "Round", rnd, "begins!"
        print ""
        hero_roll = random.randrange(1,7)
        print hero_name, "rolled a", hero_roll
        dragon_health -= (hero_roll * hero_power)
        print "Dragon's health is now", dragon_health
        print ""
        dragon_roll = random.randrange(1,7)
        print "The dragon rolled a", dragon_roll
        hero_health -= (dragon_roll * dragon_power)
        print hero_name, "now has a health of", hero_health
        print ""
        if (dragon_health <= 0 and hero_health <= 0):
            print hero_name, "killed the dragon but the dragon got in a final killing blow."
            print ""
            print ""
            cont("bend")
        elif (dragon_health <= 0):
            print hero_name, "defeated the dragon! And there was much rejoicing."
            loot_prize = loot(dragon_difficulty, player_class)
            print ""
            print ""
            print "Your prize is a " + loot_prize
            print ""
            print ""
            cont("bend")
        elif (hero_health <= 0):
            print "The dragon defeated", hero_name, "and had quite a brunch."
            print ""
            print ""
            cont("bend")
        else:
            print "The battle continues!"
            print ""
            print ""
        time.sleep(10)

        
dragon_e = Dragon(120, 10)
dragon_m = Dragon(140, 18)
dragon_h = Dragon(160, 23)

hero_w = Hero(90, 10)
hero_r = Hero(80, 15)

hero_name = intro('name')
dragon_difficulty = d_diff('ddiff')
player_class = h_class('hclass')
dragon_power = drag(dragon_difficulty)
dragon_health = drag_h(dragon_difficulty)
print ""
print "Dragon power is", dragon_power
print "Dragon health is", dragon_health
hero_power = hero_p(player_class)
hero_health = hero_h(player_class)
print ""
print "Hero power is", hero_power
print "Hero health is", hero_health
print ""
print ""
time.sleep(5)
battle(hero_name, dragon_health, dragon_power, hero_health, hero_power)