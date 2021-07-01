menu = [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam","Tomato","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","bacon","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"]
]

for meal in menu:
    for i in range(len(meal)-1):
        if meal[i] != "spam":
            print(meal[i],end=" ")
    print("")
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#     else:
#         for i in meal:
#             if i == "spam":
#                 meal.remove(i)
#         print(meal)
#
# for meal in menu:
#     for item in range(len(meal) -1, -1, -1):
#         if meal[item] == "spam":
#             del meal[item]
#     print(", ".join(meal))



