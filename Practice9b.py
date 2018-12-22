import random
import time


# 2.2 ACTIVITY #1
class Car:
    def factory(type):
        if type == "SportsCar":
            return SportsCar()
        if type == "Van":
            return Van()
        if type == "Truck":
            return Truck()
        assert 0, "Bad car creation: " + str(type)

    def move(self):
        self.traveled += self.pace  # it has a problem with this, but it works fine, so...
        self.gas -= 1
        print("The", self.name, "has travelled", self.traveled, "unit(s) with", self.gas, "gallon(s) of gas left.")


class Van(Car):
    def __init__(self):
        self.gas = 15
        self.traveled = 0
        self.pace = 3
        self.name = "Van"


class SportsCar(Car):
    def __init__(self):
        self.gas = 10
        self.traveled = 0
        self.pace = 5
        self.name = "Sports Car"


class Truck(Car):
    def __init__(self):
        self.gas = 25
        self.traveled = 0
        self.pace = 1
        self.name = "Truck"


t = Truck()
t.move()
r = SportsCar()
r.move()
v = Van()
v.move()


# 2.2 ACTIVITY #2
# this was the same as last time, so I just did it a little different!]
class Tank:
    def __init__(self, level, name, orientation, skill):
        self.moves = 0
        self.level = level  # 3
        self.name = name
        self.health = 100 + ((level + 1) * 3)
        self.defense = (level + 1) * 10
        self.attack = (level + 1) * 5
        self.double_def = None
        if orientation == "f":
            self.pos_pronoun = "her"
        elif orientation == "m":
            self.pos_pronoun = "his"
        else:
            self.pos_pronoun = "their"
        if orientation == "f":
            self.pronoun = "she"
        elif orientation == "m":
            self.pronoun = "he"
        else:
            self.pronoun = "they"
        if skill == "d":
            self.shadow_skill = True
        elif skill == "l":
            self.shadow_skill = False
        else:
            self.shadow_skill = None

    def check(self):
        print("\n\n", self.name, "is checking", self.pos_pronoun, "stats...\nTank Level:", self.level, "\nName:",
              self.name, "\nMax Health:", self.health, "\nDefense:", self.defense, "\nAttack:", self.attack)
        self.moves += 1

    def hit(self, damage, cause, attacker):
        if self.double_def == self.moves and damage > 1:
            damage //= 2
            self.health += damage
            print("\n", self.name, "took {} damage from '{}' by the hand of {}, which could have been {} damage if {} \
hadn't had a buff!\n".format(damage, cause, attacker, damage * 2, self.pronoun),
                  self.name + "'s Health:", str(self.health) + "/" + str(100 + ((self.level + 1) * 8)), "(" +
                  str((self.health * 100) // (100 + ((self.level + 1) * 8))) + "%)")
        else:
            print("\n", self.name, "took {} damage from '{}' by the hand of {}!\n".format(damage, cause, attacker),
                  self.name + "'s Health:", str(self.health) + "/" + str(100 + ((self.level + 1) * 8)), "(" +
                  str((self.health * 100) // (100 + ((self.level + 1) * 8))) + "%)")
        self.moves += 1

    def shield(self):
        self.double_def = self.moves + 1
        if self.shadow_skill is False:
            print("\n", self.name, "summoned a 'Blinding Buckler'! \n", self.name, "doubled", self.pos_pronoun,
                  "defense for 1 turn.")
        elif self.shadow_skill is True:
            print("\n", self.name, "summoned a 'Moon Mantlet'! \n", self.name, "doubled", self.pos_pronoun,
                  "defense for 1 turn.")
        else:
            print("\n", self.name, "summoned a 'Kite Shield'! \n", self.name, "doubled", self.pos_pronoun,
                  "defense for 1 turn.")
        self.moves += 1

    def taunt(self, target):
        old_health = target.health
        target.health -= ((self.attack + random.randint(0, self.attack * 2)) - target.defense)
        damage = old_health - target.health
        if damage < 0:
            damage = 1
            target.health = old_health - 1
        if self.shadow_skill is False:
            target.hit(damage, "Distracting Beacon", self.name)
        elif self.shadow_skill is True:
            target.hit(damage, "Jeering Ghost", self.name)
        else:
            target.hit(damage, "Taunting Strike", self.name)
        self.moves += 1

    def throw(self, target):
        old_health = target.health
        target.health -= self.attack - target.defense
        damage = old_health - target.health
        if damage < 0:
            damage = 1
            target.health = old_health - 1
        if self.shadow_skill is False:
            target.hit(damage, "Glowing Glaive", self.name)
        elif self.shadow_skill is True:
            target.hit(damage, "Twilit Trident", self.name)
        else:
            target.hit(damage, "Just Javelin", self.name)
        self.moves += 1


moves = 0
a = Tank(4, "Sol", "n", "l")
b = Tank(4, "Umbra", "f", "d")
a.check()
moves += 1
time.sleep(random.randint(3, 8))
b.check()
moves += 1
time.sleep(random.randint(3, 8))
while not a.health <= 0 and not b.health <= 0:
    rand = random.randint(1, 3)
    if rand == 1:
        a.throw(b)
        time.sleep(random.randint(3, 8))
    elif rand == 2:
        a.taunt(b)
        time.sleep(random.randint(3, 8))
    else:
        a.shield()
        time.sleep(random.randint(3, 8))
    moves += 1
    rand = random.randint(1, 3)
    if rand == 1:
        b.throw(a)
        time.sleep(random.randint(3, 8))
    elif rand == 2:
        b.taunt(a)
        time.sleep(random.randint(3, 8))
    else:
        b.shield()
        time.sleep(random.randint(3, 8))
    moves += 1
if a.health > 0 and b.health > 0:
    print("\"Never excuse—for when the players are all\\dead, there needs none to be blamed,\" - Shakespeare, A \
Midsummer Night's Dream (5.1.346-347).\n {} moves have elapsed.".format(moves))
elif a.health > 0:
    print("\n", b.name, "has perished at", b.health, "health!\n", a.name, "stands victorious with", a.health,
          "health remaining after", str(moves), "moves!")
elif b.health > 0:
    print("\n", a.name, "has perished at", a.health, "health!\n", b.name, "stands victorious with", b.health,
          "health remaining after", str(moves), "moves!")
