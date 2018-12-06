from random import *
import time
while True:
    perm = input("\nWould you like to roll the dice? Y/N \n")
    if perm == "N" or perm == "n":
        break
    else:
        print("\nYou rolled a...")
        roll = str(randint(1, 7))
        for i in range(0, int(roll)):
            print("...")
            time.sleep(1)
        print(roll + "!")
