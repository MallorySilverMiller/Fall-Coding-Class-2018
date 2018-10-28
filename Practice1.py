print("My favorite number is " + str(1))

square_size = input("#'s per side of the square? ")


def square(square_side_size):
    square_side_size = int(square_side_size)
    print("# " * square_side_size)
    for i in range(0, square_side_size - 2):
        print("#" + " " * ((square_side_size * 2) - 3) + "#")
    print("# " * square_side_size)


square(square_size)
