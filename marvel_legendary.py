import random


def random_num(number):
   rand_num = random.randrange(0,number)
   return rand_num
   
heroes = ["Captain America", "Black Widow", "Iron Man", "Thor", "Wolverine", "Gambit", "Storm", "Rogue", "Hulk", "Spiderman"]
masterminds = ["Loki", "Red Skull", "Zola"]
mm_leads = {"Loki": "Enemies of Asgard", "Zola": "Super Smart Baddies", "Red Skull": "Hydra Baddies"}
villain_groups = ["Enemies of Asgard", "Super Smart Baddies", "Hydra Baddies"]
henchmen = ["Doombots", "Sentinels"]
schemes = ["Scheme1", "Scheme2", "Scheme3"]

mm = masterminds[random_num(len(masterminds))]
print "The mastermind is " + mm

vg1 = mm_leads[mm]
print mm + " always leads " + vg1

villain_groups.remove(vg1)

vg2 = villain_groups[random_num(len(villain_groups))]
print "This time " + mm + " also controls " + vg2

hm = henchmen[random_num(len(henchmen))]
print "As well as " + hm

scheme = schemes[random_num(len(schemes))]
print "The mastermind's evil plan is " + scheme

count=0
while count<5:
    hero = heroes[random_num(len(heroes))]
    heroes.remove(hero)
    print "One of the heroes is " + hero
    count += 1