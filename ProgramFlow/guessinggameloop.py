import random

answer = random.randint(1,10)
i = None
for j in range(10):
    while i != answer:
        i = int(input("Please enter the number to test: "))
        if i == 0:
            print("Game over")
            break
        if i < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
    if i != 0:
        print("Yes, the answer is correct - {0}".format(i))
        break





