even_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)

new_list = [even,odd]

for i in new_list:
    print(i)
    for j in i:
        print(j)

# digits = sorted("432985617")
# print(digits)
#
# digits[1:3] = "23"
# print(digits)

# even.extend(odd)
# print(even)
#
# even.sort()
# print(even)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print("")
#
# print(len(even))
# print(len(odd))
#
# print()
#
# print("Mississippi".count("S".casefold()))
# print("Mississippi".count("ssi"))
