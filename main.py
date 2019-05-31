from locale import currency

from classes.game import bcolors, person
from classes.magic import spell

# creating black magic
fire = spell("Fire", 10, 100, "Black")
blizzard = spell("Blizzard", 15, 150, "Black")
meteor = spell("Meteor", 30, 300, "Black")
amadioha = spell("Amadioha", 50, 500, "Black")
ice = spell("Ice", 20, 200, "Black")

# create cure
cure = spell("cure", 12, 120, "Health")
cura = spell("cura", 15, 200, "Health")

magic = [
        {"name": "fire", "cost": 10, "dmg": 200},
        {"name": "thunder", "cost": 10, "dmg": 1300},
        {"name": "lightning", "cost": 10, "dmg": 100},
]
player = person(480, 65, 60, 34, [fire, blizzard, meteor, amadioha, ice, cure, cura])
enemy = person(1200, 65, 45, 25, [])
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("======================")
    player.choose_action()
    choice = input("choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.damage()
        enemy.take_damage(dmg)
        print("You attacked for:", dmg, "points of damage. Enemy HP", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        choice = int(input("Choose magic:")) - 1

        spell = player.magic[choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.OKGREEN + "\nHP: \n", str(player.get_hp()) + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.Type == "Health":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "Hit Points" + bcolors.OKGREEN + "\nHP: \n", str(player.get_hp()) + bcolors.ENDC)
        elif spell.Type == "Black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.OKGREEN + "\nHP: \n", str(player.get_hp()) + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.damage()

    player.take_damage(enemy_dmg)
    print("Enemy attacks for:", enemy_dmg, "points of damage. PLayer HP", player.get_hp())
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "you win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "Your enemy has defeated you! Ntorr!" + bcolors.ENDC)
        running = False
