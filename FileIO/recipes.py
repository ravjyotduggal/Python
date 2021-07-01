import shelve

blt = ["bacon","lettuce","tomato","bread"]
beans_on_toast = ["beans","bread"]
scrambled_eggs = ["eggs","butter","milk"]
soup = ["tin of soup"]
pasta = ["pasta","cheese"]

#with shelve.open('recipes',writeback=True) as recipes:
# with shelve.open('recipes') as recipes:
#     temp_list = recipes["pasta"]
#     temp_list.append("Ketchup")
#     recipes["pasta"] = temp_list
#
#     for snack in recipes:
#         print(snack, recipes[snack])
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup


    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    #recipes["soup"].append("courtons")

with shelve.open('recipes') as recipes:
    temp_list= recipes["soup"]
    temp_list.append("Hello")
    recipes["soup"] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])

