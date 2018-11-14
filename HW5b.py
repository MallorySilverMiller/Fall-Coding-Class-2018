# Challenge #2
xcoor = float(input("Glarkonians, what is the latest x coordinate? "))
ycoor = float(input("Glarkonians, what is the latest y coordinate? "))
zcoor = float(input("Glarkonians, what is the latest z coordinate? "))
store = int(input("Computer , how many digits can I store? ")) // 3
print(("{" + ":.{}f".format(store) + "}").format(xcoor))
print(("{" + ":.{}f".format(store) + "}").format(ycoor))
print(("{" + ":.{}f".format(store) + "}").format(zcoor))
