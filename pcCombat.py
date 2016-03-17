import random


class PC:
    def __init__(self, Name, Str, Dex, Con, Intel, Wis, Chr, Class, Level, armor, shield, sizeMod):
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
            x += 1
            
    def meleeAtk(self, mod = 0):
        return (random.randint(1, 20) + self.Level + StatBonus(self.Str) + mod)

    def meleeDmg(self, numDie = 1, dieType = 8, mod = 0):
        return numDie * random.randint(1, dieType) + mod

def StatBonus(stat):
    if stat >= 10:
        return (stat - 10) // 2
    elif stat <= 9 and stat >= 1:
        return (-5) + (stat // 2)

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
    print('Combat has begun between', pc1.Name, 'and', str(pc2.Name) + '!')
    print(pc1.Name, 'has', pc1.HP, 'hitpoints and', pc2.Name, 'has', pc2.HP, 'hitpoints!')
    print('')
    while pc1.HP > 0 and pc2.HP > 0:
        rnd += 1
        print('Round ' + str(rnd) + '!!')
        print(pc1.Name, 'attacks', pc2.Name + '!')
        roll = pc1.meleeAtk()
        print(pc1.Name, 'rolls a ' + str(roll) + '!')
        if roll > pc2.AC:
            dmg = pc1.meleeDmg()
            pc2.HP -= dmg
            print(pc1.Name, 'hits for', dmg, 'points!', pc2.Name, 'is down to', pc2.HP, 'hit points!')
        else:
            print(pc1.Name, 'missed!')
        try:
            input('Press Enter to Continue...')
            print('')
        except SyntaxError:
            pass
        if pc1.HP > 0 and pc2.HP > 0:
            print(pc2.Name, 'attacks', pc1.Name + '!')
            roll = pc2.meleeAtk()
            print(pc2.Name, 'rolls a ' + str(roll) + '!')
            if roll > pc1.AC:
                dmg = pc2.meleeDmg()
                pc1.HP -= dmg
                print(pc2.Name, 'hits for', dmg, 'points!', pc1.Name, 'is down to', pc1.HP, 'hit points!')
            else:
                print(pc2.Name, 'missed!')
            try:
                input('Press Enter to Continue...')
                print('')
            except SyntaxError:
                pass
        

pesky = PCfighter('Pesky', 12, 18, 16, 18, 14, 11, 'Fighter', 5, 5, 2, 0)
diablo = PCfighter('Diablo', 10, 10, 10, 10, 10, 11, 'Fighter', 5, 5, 2, 0)
Combat(pesky, diablo)
