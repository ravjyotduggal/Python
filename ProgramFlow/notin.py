# activity = input("What would you like to do today? ")
#
# if "cinema" not in activity:
#     print("But i want to go to cinema")
# else:
#     print("ok")
#
# if "cinema" not in activity.casefold():
#     print("but i want to go to cinema")
# else:
#     print("Ok2")
#
# name = input("Please enter your name: ")
# age = int(input("Please enter your age"))
#
# if 18<=age<31:
#     print("Welcome club 18-30 holiday")
# else:
#     print("You are not allowed to enter")

# letters = "abcdefghijklmnopqrstuvwxyz"
# #v
# print(letters[21:-27:-1])
# print(letters[21:8:-1])

activity = input("Please enter your activity ")
youractivity = input("Please enter your fav activity")

if youractivity.casefold() not in activity:
    print("We have to do {0}".format(youractivity))
else:
    print("Yes, we are excited to do {0}".format(youractivity))


