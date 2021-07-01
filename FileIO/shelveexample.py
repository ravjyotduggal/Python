import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit['lemon'])
#     print(fruit['grape'])

# with shelve.open("bike") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250
#
#     print(bike["engine_size"])
#     print(bike["colour"])

# fruit = shelve.open('ShelfTest')
#
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"
#
# sorted_list = list(sorted(fruit.keys()))
#
# for i in sorted_list:
#     print(i + " - " + fruit[i])
# while True:
#     shelf_key = input("Please enter a fruit ")
#     if shelf_key == "quit":
#         break
#     if shelf_key in fruit:
#         decription = fruit.get(shelf_key, "This fruit is not in the dect")
#         print(decription)
#     else:
#         print("We are not able to find {}".format(shelf_key))

# for i in fruit:
#     print(i + ": " + fruit[i])

# fruit.close()