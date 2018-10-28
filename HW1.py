

def circle(w):  # Question 3
    w = int(w)
    print(" " * (w + 1) + "@" * (w + 2))
    print(" " + "@" * w + " " * (w + 2) + "@" * w)
    print("@" * w + " " * (w + 4) + "@" * w)
    print(" " + "@" * w + " " * (w + 2) + "@" * w)
    print(" " * (w + 1) + "@" * (w + 2))


print("During this class I am most excited to get projects to work on with a purpose rather than having to make up what\
 I'm working on myself.")  # Question 1
print(str(5) + " days")  # Question 2
wideness = input("Wideness/Thickness of circle? (one value) ")  # Question 3
circle(wideness)
