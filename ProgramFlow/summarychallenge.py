first = "Learn Python"
second = "Learn Java"
third = "Go swimming"
fourth = "Have Dinner"
fifth = "Go to bed"
sixth = "Exit"

selection = "-"

while selection != 0:

    if selection == 1:
        print("You have selected {}".format(selection))
    elif selection == 2:
        print("You have selected {}".format(selection))
    elif selection == 3:
        print("You have selected {}".format(selection))
    elif selection == 4:
        print("You have selected {}".format(selection))
    elif selection == 5:
        print("You have selected {}".format(selection))
    else:
        print("Please choose your option from the list below: \n 1. {} \n 2. {} \n 3. {} \n 4. {} \n 5. {} \n 0. {}".format(first,second,third,fourth,fifth,sixth))
    selection = int(input("Please enter the number: "))
else:
    print("You have been exited")

