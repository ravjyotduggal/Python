# avaliable_parts = ["computer","monitor","keyboard","mouse","mouse mat","hdmi cable"]
#
# valid_choices = []
# for i in range(1, len(avaliable_parts) + 1):
#     valid_choices.append(str(i))
# print(valid_choices)
# current_choice = "-"
# computer_parts = []
#
# while current_choice != '0':
#     if current_choice in valid_choices:
#         print("Adding {}".format(current_choice))
#         index = int(current_choice) -1
#         chosen_part = avaliable_parts[index]
#         computer_parts.append(chosen_part)
#     else:
#         print("Please add options from the list below: ")
#         for number, part in enumerate(avaliable_parts):
#             print("{0}: {1}".format(number + 1, part))
#
#     current_choice = input()
#
# print(computer_parts)

avaliable_parts = ["computer","monitor","keyboard","mouse","mouse mat","hdmi cable"]

current_choice = "-"
options= []
for i in range(1, len(avaliable_parts) + 1):
    options.append(str(i))

print(options)

user_cart = []

while current_choice != '0':
    if current_choice in options:
        product_name = avaliable_parts[int(current_choice)-1]
        if product_name in user_cart:
            print("Removing {}".format(product_name))
            user_cart.remove(product_name)
        else:
            print("You have selected {}".format(current_choice))
            user_cart.append(product_name)
        print("Your list now contains {}".format(user_cart))
    else:
        print("Please select the product from below: ")
        for number, part in enumerate(avaliable_parts):
                print("{}: {}".format(number + 1, part))

    current_choice = str(input("Please enter the order number: "))

print(user_cart)




