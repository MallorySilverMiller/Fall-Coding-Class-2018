# Problem #1
greeting = "Hello"
name = "Ben Bitdiddle"
# print(greeting, ",", name)
# print(greeting.center(28, '*'))
# print(greeting, greeting, name, greeting, "!")
print("{0} , {1}".format(greeting, name))
print("{:*^28}".format(greeting))
print("{0} {0} {1} {0} !".format(greeting, name))
print()

# Challenge #1
a = 24.16927
x = 5
b = 20
y = 69282100
print("{:.3%}".format((x + b) / 100))
# 25.000%
print("{:#<15.2f}".format(a))
# 24.17##########
print("{:,}".format(y))
# 69,282,100
print("{:*^15.1e}".format(b))
# ****2.0e+01****
