fruit = {"orange": "a sweet, organge, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

f_tuple = tuple(fruit.items())

for snack in f_tuple:
    item, description = snack
    print(item + " is a " + description)

print(dict(f_tuple))

# print(fruit)
# print(fruit["apple"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# print(fruit["lime"])
#
# fruit["hello"] = "How are you"
# print(fruit["hello"])
#
# #fruit.clear()
# #del fruit["pear"]
# print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a {}".format(dict_key))

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     decription = fruit.get(dict_key, "We don't have a {}".format(dict_key))
#     print(decription)

# fruit["hello"] = "How are you"
# print(fruit)
#
# print(fruit.get("lemon"))
#
# for snack in fruit:
#     print(fruit[snack])

#print(fruit.keys())

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for i in ordered_keys:
#     print(i + "- " + fruit[i])

# for i in sorted(fruit.keys()):
#     print(i + " - " + fruit[i])
#
# for i in fruit.values():
#     print(i)
#
# print(fruit.keys())
# print(fruit.values())
#
# del fruit["hello"]
# print(fruit)

