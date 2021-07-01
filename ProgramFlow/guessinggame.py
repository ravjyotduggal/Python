answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess<answer:
    print("Please guess higher")
elif guess>answer:
    print("Please guess lower")
else:
    print("You got it first time right")

if guess<answer:
    print("Please guess higher")
    guess=int(input())
    if guess==answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess>answer:
    print("Please guess lower")
    guess=int(input())
    if guess==answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guesses correctly")
else:
    print("You got it first time right")

#Using Operators

if guess != answer:
    if guess<answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess=int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time right")

#Challenge

if guess==answer:
    print("You got it first time right")
else:
    if guess<answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess=int(input())
    if guess==answer:
        print("Well done, you got it right")
    else:
        print("Sorry, you have not guesses correctly")










