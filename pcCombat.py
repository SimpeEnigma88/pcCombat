import random


class PC:
    def __init__(self, Name, Str, Dex, Con, Intel, Wis, Chr, Class, Level, armor, shield, sizeMods):
        self.Name = Name
        self.Str = Str
        self.Dex = Dex
        self.Con = Con
        self.Intel = Intel
        self.Wis = Wis
        self.Chr = Chr
        self.Class = Class
        self.Level = Level

class PCfighter(PC):
    def __init__(self, Name, Str, Dex, Con, Intel, Wis, Chr, Class, Level, armor, shield, sizeMod):
        PC.__init__(self, Name, Str, Dex, Con, Intel, Wis, Chr, Class, Level, armor, shield, sizeMod)
        self.AC = 10 + armor + shield + sizeMod
        self.HP = 0
        x = 1
        while x <= self.Level:
            self.HP += (random.randint(1, 10) + StatBonus(self.Con))
            x = x + 1
    def meleeAtk(self, mod = 0):
        return (random.randint(1, 20) + StatBonus(self.Str) + mod)

    

def StatBonus(stat):
    if stat >= 10:
        return ((stat - 10) // 2)
    elif stat <= 9 and stat >= 1:
        return ((-5) + (stat // 2))

def Initiative(pc1, pc2):
    pc1roll = random.randint(1, 20) + StatBonus(pc1.Dex)
    pc2roll = random.randint(1, 20) + StatBonus(pc2.Dex)
    if pc1roll > pc2roll:
        return True
    else:
        return False


def Combat(firstPC, secondPC):
    if Initiative(firstPC, secondPC) == True:
        pc1 = firstPC
        pc2 = secondPC
    else:
        pc1 = secondPC
        pc2 = firstPC

    rnd = 0
    
    while pc1.HP > 0 and pc2.HP > 0:
        rnd += 1
        print('Round ', rnd, '!!')
        print(pc1.Name, ' attacks!')
        roll = pc1.meleeAtk()
        print(pc1.Name, 'rolls a ', roll, '!')
        if roll > pc2.AC:
            pc2.HP -= 
        try:
            input('Press Enter to Continue...')
        except SyntaxError:
            pass
        
    

pesky = PCfighter('Pesky', 12, 18, 16, 18, 14, 11, 'Fighter', 5, 5, 2, 0)
diablo = PCfighter('Diablo', 8, 12, 10, 16, 12, 11, 'Fighter', 3, 3, 0, 2)

Combat(pesky, diablo)
