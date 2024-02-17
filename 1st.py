import sys, datetime, random

class player:
    name = 'a'
    hp = 1000
    level = 1
    attack = 1 
    defence = 1
    theism = (0, 0, 'athiest')
    armour = [['leather cap', 'leather shirt', 'leather trousers', 'leather shoes'],
              [1,1,1,1]]
    p1 = 1
    p2 = 1
    A1, A2 = 1,1

    def __init__(self, hp, attack,defence, name, theism, p1, p2, A1, A2):
        self.hp = hp
        self.attack = (attack + theism[0])
        self.defence = defence
        self.name = name
        self.theism = theism
        self.p1 = p1
        self.p2 = p2
        self.A1 = A1
        self.A2 = A2

    def localarea(self, area, A1, A2, p1, p2):
        printarea(area,A1, A2, p1, p2)

    def statcall(self):
        print(f'''{self.name} has {self.hp} hp,
is at level {self.level},
attack = {self.attack}
defence = {self.defence}
''')
        if self.theism[2] != 'athiest':
            print(f'follows {self.theism[2]}')

    def theismcall(self):
        print(f'''{self.name} follows the {self.theism[2]} theism
{self.theism[2]} grants a bonus {self.theism[0]} to attack and a
bonus {self.theism[1]} to defense
''')


class enemy:
    hp = int()
    level = int()

def initarea():
    subarea = [['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U'],
                ['U','U','U','U','U','U','U','U','U','U']
               ]

    area = [[subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea],
            [subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea,subarea]
            ]

    displarea = [['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored'],
                 ['unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored','unexplored']
                 ]

##    for A in range(len(area[0])):
##        print('ooooof')
##        B,C,D = 0,0,0
##        for B in range(len(area[0])):
##            C,D = 0,0
##            print('chunk')
##            print(A,B,C,D)
##            for C in range(len(area[0])):
##                print('mini')
##                D = 0
##                for D in range(len(area[0])):
##                    print(area[D][C][B])
    
    return(area, displarea)

def printarea(area, A1, A2, p1, p2):
    print(A1, A2, p1, p2)
    numberList = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for i in range(len(area[A1][A2])):
        if int(i) == int(p2):
            this = i
    blank = '      '
    for n in range(this - 1):
        blank = (blank + '     ')
    print('  ',blank, 'v')
    numberList = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(area[A1][A2])):
        if int(i) == int(p1):
            print(' >', area[A1][A2][i],'<')
        else:
            print('',i, area[A1][A2][i])
    for i in range(len(area[A1][A2])):
        if int(i) == int(p2):
            numberList[i] = '^'
    print('  ',numberList)

temp = input('choose a name ')

pc = player(65432, 4, 3, temp, (0, 0, 'athiest'),random.randint(0,9) ,random.randint(0,9) ,random.randint(0,9),random.randint(0,9) )
del temp

area, displarea = initarea()
pc.statcall()
pc.theismcall()
print(pc.A1, pc.A2)
pc.localarea(area, pc.A1, pc.A2, pc.p1, pc.p2)

