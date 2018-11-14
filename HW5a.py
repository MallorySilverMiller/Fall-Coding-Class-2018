# Challenge #1
fname = input("What's your first name? ")
lname = input("What's your last name? ")
byear = input("In what year were you born? ")
greet = "Hello {} {}!".format(fname, lname)
age = 2018 - int(byear)
mperc = (int(byear) / 2018) * 100
fwell = "Goodbye!"
print(greet.center(50, "*"))
print("You were born in", byear.rjust(8, "0"), ".")
print("The current year is: {:.3e}".format(2018))
print("You are", str(age), "years old.")
print("Magic: ", "{:.4f}".format(mperc), "%")
print(fwell.rjust(50))
