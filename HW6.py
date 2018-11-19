# Write a function that counts the number of occurrences of each character in a string.
# Example: "hello" has 1 "h", 1 "e", 2 "l"s, 1 "o"
# Q: what kind of data structure would you use to represent the output?
# A: A dictionary
#
# side note: this was fun, but i made it super over-complicated to match the example syntax perfectly. sorry if that\
# makes it hard to read!


def count(x):
    num_dict = {}  # ex: {"h": 1, "e": 1, "l": 2, "o": 1} {"character": num of times}
    num_said = {}  # to prevent saying the same thing twice
    to_return = ""
    for c in x:  # for counting characters
        try:
            num_dict.update({c: (num_dict[c] + 1)})
        except KeyError:
            num_dict.update({c: 1})
    for c in x:  # for proper output
        if c == x[0]:
            if num_dict[c] > 1 and c not in num_said:
                to_return = "\"{0}\" has {1} \"{2}\"s".format(x, num_dict[x[0]], x[0])
                try:
                    num_said.update({c: (num_said[c] + 1)})
                except KeyError:
                    num_said.update({c: 1})

            elif num_dict[c] <= 1:
                to_return = "\"{0}\" has {1} \"{2}\"".format(x, num_dict[x[0]], x[0])
            else:
                pass
        else:
            if num_dict[c] > 1 and c not in num_said:
                to_return += ", {1} \"{0}\"s".format(c, num_dict[c])
                try:
                    num_said.update({c: (num_said[c] + 1)})
                except KeyError:
                    num_said.update({c: 1})
            elif num_dict[c] <= 1:
                to_return += ", {1} \"{0}\"".format(c, num_dict[c])
            else:
                pass
    return to_return


print(count('hello'))  # Output: 'hello' has 1 'h', 1 'e', 2 'l's, 1 'o'

# Write a function to reverse a tuple. You may not use any built in Python functions to do the reversal.
# Do not modify any inputs to the function.
# Example: (1, 3, 2, 7, 4)
# Q: Will you need to create a new tuple to ensure that inputs aren't modified? Why or why not?
# A: You do have to create a new tuple because tuples are immutable.


def rev(x):
    reverse = []
    for e in x:
        reverse.insert(0, e)
    return tuple(reverse)


print(rev((1, 3, 2, 7, 4)))  # Output: (4, 7, 2, 3, 1)

# Write a function to find the maximum and the minimum value in a set.


def max_min(x):
    mm = [x[0], 0]
    for i in x:
        if int(i) < mm[0]:
            del mm[0]
            mm.insert(0, i)
        elif int(i) > mm[1]:
            del mm[1]
            mm.insert(1, i)
    return mm


print(max_min((1, 2, 4, 1, 5, 7, 3, -9)))

# Write a function that accepts a string and calculate the number of upper case letters and lower case letters.
# Q: How do we determine if a letter is upper case or lower case? Does Python have a function that does this? Can we
# also do this without using built-in functions?
# Hint: ASCII table
# A: compare the symbol in the string to what it would be if it was uppercase or lowercase and see if its the same. You\
#  could do this using the ASCII table by determining the ASCII value, therefore determining if it was capitalized.


def calc(x):
    low = 0
    high = 0
    for i in x:
        if i == " " or i == "." or i == ",":
            pass
        elif i == i.upper():
            high += 1
        elif i == i.lower():
            low += 1
    ret = "Number of Lowercase letters: {0}\nNumber of Uppercase letters: {1}".format(low, high)
    return ret


print(calc("FiGHt mE"))

# Write a function to print all even numbers from a given list.
# Q: What operator can we use to easily tell us if a number is even or not?
# A: x % 2 == 0


def even(x):
    for i in x:
        if i % 2 == 0:
            print(i)


even([1, 2, 3, 4, 5])
