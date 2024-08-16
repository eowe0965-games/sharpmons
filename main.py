'''*attack
25% miss -> 0% attack
25% graze -> 25% attack
35% hit -> 100% attack
10% direct hit -> 120% attack
5% crit -> 150% attack

Compare attack vs defense

If attack is % of defense:
0% - 19%: Do no dmg
20 - 39%: Do random dmg up to 10% of attack
40 - 59%: do 2x random dmg up to 10% of attack each
Etc
100+%: do 4x random dmg up to 10% of attack each, plus attack - defense

I.e. for every 20% of defense, do random dmg up to 10% of attack value.
'''


import random
import os
import time
name1 = ["Flame", "Helio", "Cryo", "Electro", "Geo", "Anemo", "Dendro",]
name2 = ["bolt", "blade", "razor", "point", "dude", "flash", "man"]
bam = ["fury hit", "walloping whack", "inferno fist"]
boom = ["electro ray", "ice beam", "mist shot"]
def percent(part, whole):
    return 100 * float(part)/float(whole)
print("sharp monsters!!!\n\n\n")

opponent = (random.choice(name1))+(random.choice(name2))
opphp = 100
opplvl = random.randint(1,100)
oppatk = random.randint(1,opplvl)
oppdef = random.randint(1,opplvl)
oppspatk = random.randint(1,opplvl)
oppspdef = random.randint(1,opplvl)
print("opponent's sharpmon is", opponent)
print("level", opplvl)
print("atk", oppatk)
print("def", oppdef)
print("sp def", oppspdef)
print("sp atk", oppspatk)

print("\n")

player = (random.choice(name1))+(random.choice(name2))
hp = 100
lvl = random.randint(1,100)
atk = random.randint(1,lvl)
defense = random.randint(1,lvl)
spatk = random.randint(1,lvl)
spdef = random.randint(1,100)
print("your sharpmon is", player)
print("level", lvl)
print("atk", atk)
print("def", defense)
print("sp def", spdef)
print("sp atk", spatk)
time.sleep(1)
input("\n\npress enter to continue")

bp1 = random.randint(10,20)
bp2 = random.randint(10,20)
phys = random.choice(bam)
sp = random.choice(boom)
while not opphp <= 0 or not hp <= 0:
  while True:
    os.system("clear")
    print("it's your turn to attack!")
    attackType = input("do you use:\n(p)PHYS: " + phys + " " + str(bp1) + "\n(s)SPE: " + sp + " " + str(bp2) + "\n")
    atkmod = random.randint(1,100)
    if attackType == "p":
      if atkmod <= 25:
        basemod = 0
        print("your attack missed!")
      elif atkmod <= 50:
        basemod = atk*0.25
      elif atkmod <= 85:
        basemod = atk*1.00
      elif atkmod <= 95:
        basemod = atk*1.25
      else:
        basemod = atk*1.50
      if percent(basemod, oppdef) <= 19:
        print("your attack missed!")
      elif percent(basemod, oppdef) <= 39:
        print("your attack grazed the opponent!")
        opphp = opphp - random.randint(1, basemod)
      elif percent(basemod, oppdef) <= 59:
        print("your attack hit the opponent!")  
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
      elif percent(basemod, oppdef) <= 79:
        print("you landed a square hit on the opponent!")
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
      elif percent(basemod, oppdef) <= 100:
        print("your landed a critical hit on the opponent!")
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
      break
    elif attackType == "s":
      if atkmod <= 25:
        basemod = 0
      elif atkmod <= 50:
        basemod = spatk*0.25
      elif atkmod <= 85:
        basemod = spatk*1.00
      elif atkmod <= 95:
       basemod = spatk*1.25
      else:
        basemod = spatk*1.50
      if percent(basemod, oppdef) <= 19:
        print("your attack missed!")
      elif percent(basemod, oppdef) <= 39:
        print("your attack grazed the opponent!")
        opphp = opphp - random.randint(1, basemod)
      elif percent(basemod, oppdef) <= 59:
        print("your attack hit the opponent!")  
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
      elif percent(basemod, oppdef) <= 79:
        print("your landed a square hit on the opponent!")
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
      elif percent(basemod, oppdef) <= 100:
        print("your landed a critical hit on the opponent!")
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
        opphp = opphp - random.randint(1, basemod)
      break
    else:
      print("invalid attack. use (p) or (s)")
      time.sleep(1)
  
  print(opponent,"'s hp is", opphp)
  time.sleep(1)
  input("\n\npress enter to continue")

  os.system("clear")
  
  print("it's the opponent's turn to attack!")
  time.sleep(1)
  print("the opposing", opponent, "used", phys)
  if random.randint(1,2) == 1:
    atkmod = random.randint(1,100)
    if atkmod <= 25:
      basemod = 0
      print("the opponent's attack missed!")
    elif atkmod <= 50:
      basemod = oppatk*0.25
    elif atkmod <= 85:
      basemod = oppatk*1.00
    elif atkmod <= 95:
      basemod = oppatk*1.25
    else:
      basemod = atk*1.50
    if percent(basemod, defense) <= 19:
      print("the opponent's attack missed!")
    elif percent(basemod, defense) <= 39:
      print("you were grazed by your opponent's attack!")
      hp = hp - random.randint(1, basemod)
    elif percent(basemod, defense) <= 59:
      print("the opponent hit you!")  
      hp = hp - random.randint(1, basemod)
      hp = hp - random.randint(1, basemod)
    elif percent(basemod, defense) <= 79:
      print("the opponent landed a square hit on you!!")
      hp = hp - random.randint(1, basemod)
      hp = hp - random.randint(1, basemod)
      hp = hp - random.randint(1, basemod)
    elif percent(basemod, defense) <= 100:
      print("the opponent landed a critical hit on you!")
      hp = hp - random.randint(1, basemod)
      hp = hp - random.randint(1, basemod)
      hp = hp - random.randint(1, basemod)
      hp = hp - random.randint(1, basemod)
  else:
    if atkmod <= 25:
      basemod = oppspatk*0
    elif atkmod <= 50:
      basemod = oppspatk*0.25
    elif atkmod <= 85:
      basemod = oppspatk*1.00
    elif atkmod <= 95:
     basemod = oppspatk*1.25
    else:
      basemod = oppspatk*1.50
    if percent(basemod, spdef) <= 19:
       print("the opposing", opponent, "'s attack missed!")
    elif percent(basemod, spdef) <= 39:
       print("you were grazed by the opposing ", opponent, "'s attack!")
       hp = hp - random.randint(1, basemod)
    elif percent(basemod, spdef) <= 59:
       print("the opposing", opponent, "hit you!")  
       hp = hp - random.randint(1, basemod)
       hp = php - random.randint(1, basemod)
    elif percent(basemod, spdef) <= 79:
       print("the opposing", opponent, "landed a square hit on your", player, "!")
       hp = hp - random.randint(1, basemod)
       hp = hp - random.randint(1, basemod)
       hp = hp - random.randint(1, basemod)
    elif percent(basemod, spdef) <= 100:
       print("the opposing", opponent, "landed a critical hit on your", player, "!")
       hp = hp - random.randint(1, basemod)
       hp = hp - random.randint(1, basemod)
       hp = hp - random.randint(1, basemod)
       hp = hp - random.randint(1, basemod)
    print("your health is now", hp)
    time.sleep(1)
    input("\n\npress enter to continue")
    os.system("clear")

os.system("clear")
if opphp <= 0:
  print("the winner of this sharpmon battle is", player,"!")
else:
  print("the winner of this sharpmon battle is", opponent,"!")
