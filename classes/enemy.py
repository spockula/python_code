class enemy:
    def __init__(self, attackl, attackh): #attackl = attack low, attackh = attack high
        self.max_attackl = attackl
        self.max_attackh = attackh
        self.attackl = attackl
        self.attackh = attackh

    def get_attack(self):
        print (self.attackl, self.attackh)

