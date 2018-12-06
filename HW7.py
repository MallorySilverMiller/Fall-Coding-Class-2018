# LESSON 5: ARITHMETIC OPERATORS HW
myMarbles = 17
myMarbles -= 15
myMarbles += 12
jennyMarbles = 7 * 3
totalMarbles = jennyMarbles + myMarbles
print("We have {} marbles!".format(totalMarbles))

# LESSON 6 LOGIC HW:

# Challenge #1
# 1. True
# 2. True
# 3. False
# 4. False
# 5. True
# 6. True

# Challenge #2
# 1. True = True or (False and True)
# 2. False = False and False and True or False
# 3. False = False or False and True and False
# 4. True = True or not(True) and False and not(True)
# 5. True = not(True) and not(False) or not(False) or not(True)

# Challenge #3
# True True: False
# True False: True
# False True: True
# False False: False
# This can show if an or statement is redundant.

# LESSON 7 CONDITIONALS HW:

inp = int(input("Please input a number: "))
if inp % 3 == 0 and inp % 5 == 0:
    print("Divisible by both")
elif inp % 3 == 0:
    print("Divisible by 3")
elif inp % 5 == 0:
    print("Divisible by 5")
else:
    print("Divisible by neither")

# LESSON 9 FUNCTIONS HW:


def print_book(book_title, author, num_copies, price, rev):
    print("Title: {}\nAuthor: {}\nNumber of Copies: {}\nPrice per Copy: ${}\nRevenue: ${}"
          .format(book_title, author, str(num_copies), str(price), str(rev)))


print_book("I Know Why the Caged Bird Sing", "Maya Angelou", 100, 20, 2000)
