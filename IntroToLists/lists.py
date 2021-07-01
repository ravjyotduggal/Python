# Sum Function:
#
# ipaddress = input("Please enter an IP address: ")
# print(ipaddress.count("."))
#
# String List
# parrot_list = ["non pinin'","no more","a stiff","bereft of live"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# Number Lists
#
# even = [2,4,6,8]
# odd = [1,3,5,7,9]
#
# numbers = even + odd
# numbers.sort()
# print(sorted(numbers))
#
# list_1 = []
# list_2 = list()
#
# print(list("The lists are equal"))
#
# even = [2,4,6,8]
#
# another_even = even
# another_even.sort(reverse=True)
# print(even)
#
# odd = [1,3,5,7,9]
# another_even = even
# another_even.sort(reverse=True)
# print(even)
#
#
#
# numbers_new = [even,odd]
# print(numbers_new)
#
# for number_set in numbers_new:
#     print(number_set)
#
#     for values in number_set:
#         print(values)

#Spam:

menu = []
menu.append(["egg","spam","bacon"])
menu.append(["egg","sausage","bacon"])
menu.append(["egg","spam"])
menu.append(["egg","bacon","spam"])
menu.append(["egg","bacon","sausage","spam"])

for meal in menu:
    if not "spam" in meal:
        for m in meal:
            print(m)



