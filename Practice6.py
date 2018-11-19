# Write a funcion to concatenate a list of dictionaries to create a new one. Do not modify any input. Print it and retu\
# rn it.
# Input: a list of dictionaries
# Output: a single dictionary
# Q: How would you go about concatenating the two dictionaries? Would you add values to a new dictionary, or
#    add values from one dictionary to the other existing dictionary? What is the reason for your decision?
#    Hint: immutable vs. mutable

# for every entry in list add to new dict


def concat(x):
    y = {}
    for i in x:
        y.update(i)
    return y


print(concat([{"w": "hi", "x": "9", True: False}, {"k": "y", "p": "o"}]))
# Write a function to print all unique values in a dictionary.
# Example: {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009", "VIII":"S007"}
# Output: 'S005', 'S002', 'S007', 'S001', 'S009'
# Q: How would you keep track of values you have seen before? What kind of data structure would you use?
#    What data structure would be most suitable for the operations we will be using the most?


def unique(x):
    used = set()
    for k in x:
        if k in used:
            pass
        else:
            used.add(x[k])
    return used


print(unique({"M": "S001", "C": "S002", "VI": "S001", "X": "S005", "VII": "S005", "IV": "S009", "VIII": "S007"}))
# Write a function to combine two dictionaries by adding values for common keys. Do not modify any input. Print and ret\
# urn.
# Example: d1 = {'a': 100, 'b': 200, 'c':300}
#          d2 = {'a': 300, 'b': 200, 'd':400}
# Output:  {'a': 400, 'b': 400, 'd': 400, 'c': 300}


def comb(x, y):
    added = {}
    added.update(x)
    for k in y:
        try:
            added[k] += y[k]
        except KeyError:
            added.update({k: y[k]})
    return added


print(comb({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))
