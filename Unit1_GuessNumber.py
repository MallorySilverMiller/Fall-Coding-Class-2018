import random
win = False
number = random.randint(0, 100)
for i in range(1, 11):  # guessing the number
    guess = input("Your guess: ")
    if int(guess) == number:
        win = True
        break
    elif int(guess) < number:  # less than/more than
        print("The answer is more than {}!".format(guess))
    else:
        print("The answer is less than {}!".format(guess))
    print("You have made {} out of 10 guesses. You have {} remaining!".format(i, 10 - i))
if win is True:  # win/lose
    print("Congrats! You won!")
else:
    print("Better luck next time!\nAnswer: {}".format(str(number)))
