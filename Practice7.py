# LESSON 5:
# Activity 1
mysum = 1 + 2
remainder = mysum % 2
print("\n", remainder)

# Activity 2
finalAnswer = 8 * 8
finalAnswer *= 3

# Activity 3
# Money For Bananas = 5 * 4
# Money For Apples = 3 * 8
# Money For Oranges = 5 * 3 * 3
totalMoney = (3 * 8) + (5 * 4) + (5 * 3 * 3)

# Add. Practice
quotient = 7 / 3
remainder = 7 - 3 * 2
print("\n", remainder)

# Adv. Practice
initial = int(input("What is your first favorite number? "))
secondary = int(input("What is yur second favorite number? "))
print("\n", initial, "+", secondary, "=", initial + secondary, "\n", initial, "*", secondary, "=", initial * secondary,
      "\n", initial, "-", secondary, "=", initial - secondary, "\n", initial, "/", secondary, "=", initial / secondary,
      "\n", initial, "%", secondary, "=", initial % secondary)

# LESSON 6:
# Activity 1
# Q1: True
# Q2: True
# Q3: True
# Q4: False
# Q5: True
# Q6: False

# LESSON 7
# Activity 1
feeling = input("\nHow are you feeling today? ")
if feeling == "sad":
    print("Hope you feel better soon!")
elif feeling == "happy":
    print("Glad to hear it!")
elif feeling == "tired":
    print("Take a nap!")

# Activity 2
temp = int(input("\nWhat temperature in Fahrenheit is it today? "))
if temp <= 32:
    print("It is far too cold!")
else:
    print("It is warm.")

# Activity 3
numberA = 5
numberB = 6
if numberA + numberB == 10:
    print("\nI've lived for a decade!")
elif numberA + numberB > 10:
    print("\nYes! I'm a teenager.")
else:
    print("\n:(")

# Adv. Practice
name = input("\nWhat is your name? (ALL LOWERCASE) ")
score = 0
for x in name:
    if x == "x" or x == "q" or x == "z":
        score += 11
    elif x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        score += 10
print(score)

# LESSON 9
# Activity 1


def hello_name(uname):
    return "\nHello " + uname + "!"


print(hello_name("Adilah"))

# Activity 2


def mult(z, y):
    result = z * y
    print("\nYou input the values " + str(x) + " and " + str(y) + ". Multiplied them for " + str(result) + ".")


mult(2, 7)
mult(12, 1)
mult(3, 3)

# Activity 3


def lotsa_math(z, y):
    print("\n")
    print(z + y)
    print(z - y)
    print(z * y)
    print(z / y)
    print(z % y)


lotsa_math(10, 5)
lotsa_math(17, 5)
lotsa_math(18748, 547)

# Add. Practice
# Q1: None
# Q2: (2, 3): 6, (4, 5): 20, (9, 10): 90

# Adv. Practice


def is_even(x):
    if x % 2 == 1:
        return True
    else:
        return False


numOfEvens = 0
for i in range(1, 10):
    if is_even(i):
        numOfEvens += 1
print("\n", numOfEvens)

#