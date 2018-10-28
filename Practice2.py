### Activity 1 ###

# Problem: Create a program that asks the user to enter their name and their age.
#          Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Translate the following pseudocode into code

# 1. prompt user to enter name
# 2. get name from user input
# 3. prompt user to enter age
# 4. get age from user input
# 5. convert age from string to a number
# 6. add 100 to age
# 7. print a message with the user's name and computed age

name = input("What's your name? ")
age = input("How old are you? ")
age = int(age)
age += 100
print(name + " will be " + str(age) + " in 100 years.")
