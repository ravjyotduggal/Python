for i in range(1,21):
    print("i is now {0}".format(i))

for i in range(10):
    if i != 0:
        print("i value is {0}".format(i))
for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,0,-2):
    print(i)

age = int(input("Please enter your age: "))

if age in range(16,66):
    print("Have a nice day")
else:
    print("You are nice")

for i in range(0,100):
    if i / 7  in (1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0):
        print(i)

for i in range(1,71):
    if i % 7 == 0:
        print(i)

for i in range(10,0,-2):
    print("The value of i is {0}".format(i))
