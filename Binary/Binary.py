#For Binary
for i in range(17):
    print("{0:>2} in Binary is {0:>08b}".format(i))

#For Hexadecimal

for i in range(17):
    print("{0:<2} in hex in {0:02x}".format(i))

#Challenge

powers = []

for power in range(15, -1, -1):
    powers.append(2 ** power)
# 2 is for Binary, 8 for octal
print(powers)

x = int(input("Please enter a number: "))
printing = False

for power in powers:
    bit = x // power
    if bit != 0:
        printing = True
    if printing:
        print(x//power, end='')
    x %= power
