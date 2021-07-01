farm_animal = {"sheep","cow","hen"}

for animal in farm_animal:
    print(animal)

print("=" * 40)

wild_animal = set(["lion","tiger","panther","elephant","hare"])
print(wild_animal)
for animal in wild_animal:
    print(animal)

farm_animal.add("horse")
print(farm_animal)

# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# empty_set2[1] = "a"
# print(empty_set)
# print(empty_set2)

# even = set(range(0,40,2))
# print(even)
# print(len(even))
#
# square_tuple = (4,6,9,16,25)
# squares = set(square_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
# print(even.intersection(squares))
# print(len(even.intersection(squares)))
#
# print(even & squares)
# print(squares & even)

#Difference Method

even = set(range(0,40,2))

square_tuple = (4,6,9,16,25)
square = set(square_tuple)
# print(even.difference(square))
# print(even - square)
#
# print(square.difference(even))
#
# print(square.difference(even))
#
# print(even)
# even.difference_update(square)
# print(square)
# print(even)
# square.difference_update(even)
# print(square)

#Symmetric Difference
print(even.difference(square))
print(even.symmetric_difference(square))

square.discard(4)
print(square)
try:
    square.remove(8)
except KeyError:
    print("Error occured: There is no 8 in the set")
