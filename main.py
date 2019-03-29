from classes.game import bcolors, person

magic = [
        {"name": "fire", "cost": 10, "dmg": 200},
        {"name": "thunder", "cost": 10, "dmg": 1300},
        {"name": "lightning", "cost": 10, "dmg": 100},
]
player = person(480, 65, 60, 34, magic)
enemy = person(1200, 65, 45, 25, magic)
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
