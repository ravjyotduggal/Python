for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

#Formatting

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

#Left aligned

for i in range(1,13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i **3))

#Right aligned

for i in range(1,13):
    print("No. {0:2} squared is {1:>4} and cubed is {2:>4}".format(i, i ** 2, i **3))

#Center aligned

for i in range(1,13):
    print("No. {0:2} squared is {1:>4} and cubed is {2:^4}".format(i, i ** 2, i **3))

print("Today")

for i in range(1,13):
    print("no. {2:<2} squared is {0:>1} and cubed is {1:^4}".format(i, i ** 2, i ** 3))

#Float

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

print()

print("pi value is approximately {0}".format(22 / 7))
print("pi value is approximately {0:6f}".format(22 / 7))
print("pi value is approximately {0:12.50f}".format(22 / 7))
print("pi value is approximately {0:65.50f}".format(22 / 7))
print("pi value is approximately {0:75.55f}".format(22 / 7))
print("")
for i in range(1,13):
    print(i)
print("day" in "Friday")