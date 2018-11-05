# Problem #1
# A)
x = 'foo'
y = x
print(x)  # foo
y = y + 'bar'
print(x)  # foo
# B)
x = [1, 2, 3]
y = x
print(x)  # [1, 2, 3]
y = y + [3, 2, 1]
print(x)  # [1, 2, 3, 3, 2, 1]
# This happens because strings are immutable and lists are mutable. This means when you set two strings equal, one can
# be changed without the other being effected, while when two lists are set equal they share the memory space they use.

# Problem #2
test = 1
print(id(test))
test += 1
print(id(test))
# They are different because when a string is reassigned, it creates a new spot in memory. This is because strings are
# immutable.

# CHECK IN
# 1. Strings, integers, booleans, and lists
# 2. They are thr most common and useful data types, making them often vital for functioning code.
# 3. Immutable objects take up more than one memory space when they are reassigned. Strings, integers, and booleans are
#  immutable.
# 4. (a)
# 5. (c)
