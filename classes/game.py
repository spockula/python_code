import random


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[m"

class person:
    def __init__(self, hp, mp, attack, defence, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attackh = attack + 10
        self.attackl = attack -10
        self.defence = defence
        self.magic = magic
        self.actions = ["Attack", "Magic"]
    def damage(self):
        return random.randrange(self.attackl, self.attackh)
    def spell(self, i):
        mgl = self.magic[i]["dmg"]-5
        mgh = self.magic[i]["dmg"]+5
        return random.randrange(mgl, mgh)
    
    def take_damage(self, dmg):
        self.hp-=dmg
        if self.hp <0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp-=cost

    def get_spellname(self, i):
        return self.magic[i]["name"]

    def get_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("Actions:")
        for item in self.actions:
            print(str(i) + ":", item)
            i +=1

    def choose_magic(self):
        i = 1
        print("Magic:")
        for spell in self.magic:
            print(str(i)+ ":", spell["name"], "(cost:", str(spell["mp"])+")")
            i += 1