# string = "1234567890"
#
# my_iterator = iter(string)
#
# print(next(my_iterator))
# print(next(my_iterator))

a = [1,2,3,4,5,6,7,8,9,0]
b = iter(a)

for i in range(0,len(a)):
    print(next(b))

