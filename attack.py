import random
from classes.enemy import enemy

Enemy = enemy(30,100)# assign a variable named 'Enemy' to be used in assigning values to the imported 'enemy' class
#Enemy.get_attack() #use 'Enemy' variable to call the attackl and attckh methods, in this case assigned '30' and hundred in previous line.


playerhp = 260


while playerhp > 0:
    dmg = random.randrange(Enemy.attackl, Enemy.attackh)
    #functions from the 'random' library initially imported is used to pick random numbers from the variable 'playerhp'
    #which was assigned the value of '260'. the range for picking these random numbers as required by the 'random' module
    #is determined by the values of 'attackl' and 'attackh' which was assigned to the variable 'Enemy' in line '4'
    #these values are '30' for attackl, and '100' for attackh. check to confirm.

    playerhp = playerhp-dmg #At this point, the deduction happens, random numbers from the enemy class picked by 
    #the 'random' module is deducted from the player health power (Playerhp) value of '260' until conditions
    #in the following 'IF' statements are met.

    if playerhp <=30:
        playerhp = 30
    
    print("enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp > 30:
        continue

    print("your health is in bad shape, you are being teleported to an inn for immediate healthcare ")
    break