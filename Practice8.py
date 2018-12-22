import random
import time

# ACTIVITY #1
# class ChessBoard():
# coordinates for everything
# which side each piece belongs to
# Whose turn it is

# class ChessPiece():
# properties of each piece
# captured pieces

# ACTIVITY 2
moves = 0


class Healer:
    # Check = shows all of the character's attributes like:
    # level
    # name
    # starting health
    # defense
    # attack
    # Heal self = + 50-100 health to self (character specific; dictated by lv)
    # Hit = invoked by an attacker when they attack
    # Fiery Chasm + Pyroclastic Rain = attacks
    def __init__(self, level, name, orientation):
        self.level = level  # 3
        self.name = name
        self.health = 100 + ((level + 1) * 10)
        self.defense = (level + 1) * 3
        self.attack = (level + 1) * 5
        if orientation == "f":
            self.pos_pronoun = "her"
        elif orientation == "m":
            self.pos_pronoun = "his"
        else:
            self.pos_pronoun = "their"

    def check(self):
        print("\n\n", self.name, "is checking", self.pos_pronoun, "stats...\nMage Level:", self.level, "\nName:",
              self.name, "\nMax Health:", self.health, "\nDefense:", self.defense, "\nAttack:", self.attack)

    def heal_self(self):
        self.health += random.randint(10, 20) * (self.level + 1)
        if self.health > 100 + ((self.level + 1) * 10):
            self.health = 100 + ((self.level + 1) * 10)
        print("\n", self.name, "cast 'Heal self'!\n", self.name + "'s Health:", str(self.health) + "/" +
              str(100 + ((self.level + 1) * 10)), "(" + str((self.health * 100) // (100 + ((self.level + 1) * 10))) +
              "%)")

    def hit(self, damage, cause, attacker):
        print("\n", self.name, "took {} damage from '{}' by the hand of {}!\n".format(damage, cause, attacker),
              self.name + "'s Health:", str(self.health) + "/" + str(100 + ((self.level + 1) * 10)), "(" +
              str((self.health * 100) // (100 + ((self.level + 1) * 10))) + "%)")

    def fiery_chasm(self, target):
        self_hit = random.randint(-3, 1)
        old_health = target.health
        target.health -= self.attack + random.randint(-15, 15)
        damage = old_health - target.health
        target.hit(damage, "Fiery Chasm", self.name)
        if self_hit is True:
            self.health -= round((damage / 2) - self.defense)
            print("\nClytemnestra took", str(round((damage / 2) - self.defense)), "damage by her own hand after falling\
 into", self.pos_pronoun, "own 'Fiery Chasm'!\n", self.name + "'s Health:", self.health)

    def pyro_rain(self, target):
        old_health = target.health
        target.health -= self.attack + random.randint(0, 20)
        damage = old_health - target.health
        target.hit(damage, "Pyroclastic Rain", self.name)


class DPS:
    # Check = shows all of the character's attributes like:
    # level
    # name
    # starting health
    # defense
    # attack
    # Defend = lose 5 health, get nothing, or gain 6-18 (character specific; dictated by lv)
    # Hit = invoked by an attacker when they attack
    # Spin Strike + Spear Throw = attacks
    def __init__(self, level, name, orientation):
        self.level = level  # 4
        self.name = name
        self.health = 100 + ((level + 1) * 5)
        self.defense = (level + 1) * 3
        self.attack = (level + 1) * 10
        if orientation == "f":
            self.pos_pronoun = "her"
        elif orientation == "m":
            self.pos_pronoun = "his"
        else:
            self.pos_pronoun = "their"

    def check(self):
        print("\n\n", self.name, "is checking", self.pos_pronoun, "stats...\nWarrior Level:", self.level, "\nName:",
              self.name, "\nMax Health:", self.health, "\nDefense:", self.defense, "\nAttack:", self.attack)

    def defend(self):
        defended = random.randint(-1, 3) * (self.defense + 1)
        self.health += defended
        if self.health > 100 + ((self.level + 1) * 5):
            self.health = 100 + ((self.level + 1) * 5)
        if defended <= 0:
            print("\n", self.name, "'defended,' but it didn't help!\n", self.name + "'s Health:", str(self.health) + "/"
                  + str(100 + ((self.level + 1) * 5)), "(" + str((self.health * 100) // (100 + ((self.level + 1) * 5)))
                  + "%)")
        else:
            print("\n", self.name, "'defended'!\n", self.name + "'s Health:", str(self.health) + "/" +
                  str(100 + ((self.level + 1) * 5)), "(" + str((self.health * 100) // (100 + ((self.level + 1) * 5))) +
                  "%)")

    def hit(self, damage, cause, attacker):
        print("\n", self.name, "took {} damage from '{}' by the hand of {}!\n".format(damage, cause, attacker),
              self.name + "'s Health:", str(self.health) + "/" + str(100 + ((self.level + 1) * 5)), "(" +
              str((self.health * 100) // (100 + ((self.level + 1) * 5))) + "%)")

    def spin_strike(self, target):
        old_health = target.health
        target.health -= ((self.attack + random.randint(-5, 15)) - target.defense)
        damage = old_health - target.health
        target.hit(damage, "Spinning Strike", self.name)

    def spear_throw(self, target):
        old_health = target.health
        target.health -= ((self.attack + random.randint(-7, 20)) - target.defense)
        damage = old_health - target.health
        target.hit(damage, "Spear Throw", self.name)


C = Healer(4, "Clytemnestra", "f")
O = DPS(4, "Orestes", "m")
C.check()
time.sleep(random.randint(5, 10))
O.check()
time.sleep(random.randint(5, 10))
while C.health > 0 and O.health > 0:
    if C.health < 50:
        C.heal_self()
    elif O.health >= 63:
        C.fiery_chasm(O)
    elif O.health < 63:
        C.pyro_rain(O)
    time.sleep(random.randint(3, 8))
    moves += 1
    if O.health <= 0:
        break
    elif O.health < 40:
        O.defend()
    elif C.health >= 75:
        O.spin_strike(C)
    elif C.health < 75:
        O.spear_throw(C)
    time.sleep(random.randint(3, 8))
    moves += 1
if C.health > 0 and O.health > 0:
    print("\"Never excuse—for when the players are all\\dead, there needs none to be blamed,\" - Shakespeare, A \
Midsummer Night's Dream (5.1.346-347).")
elif C.health > 0:
    print("\n", O.name, "has perished at", O.health, "health!\n", C.name, "stands victorious with", C.health,
          "health remaining after", str(moves), "moves!")
elif O.health > 0:
    print("\n", C.name, "has perished at", C.health, "health!\n", O.name, "stands victorious with", O.health,
          "health remaining after", str(moves), "moves!")
