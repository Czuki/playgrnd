import random

class Character:
    def __init__(self):
        self.strength = self.dice_throw()
        self.dexterity = self.dice_throw()
        self.constitution = self.dice_throw()
        self.intelligence = self.dice_throw()
        self.wisdom = self.dice_throw()
        self.charisma = self.dice_throw()
        self.hitpoints = self.modifier() + 10


    def dice_throw(self):
        throw = sorted([random.randint(1, 6) for i in range(0, 4)])
        return sum(throw[1:])

    def modifier(self):
        return int((self.constitution - 10) / 2)

a = Character()
print(a.strength)
print(a.dexterity)
print(a.constitution)
print(a.charisma)
print(a.hitpoints)
print(a.intelligence)
print(a.wisdom)

