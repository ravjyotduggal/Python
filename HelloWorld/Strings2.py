parrot = "Norwegian Blue"

print(parrot[-4:-2])

print(parrot[11:9:-1])

print(parrot)

print(parrot[12])

print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

#Negative indexing

print(parrot[-1])
print()
print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

#Slicing (start:Stop:Step)

print(parrot[0:6])
print(parrot[3:5])

print(parrot[10:14])
print(parrot[10:])

#Norwegian Blue

print(parrot[:6] + parrot[6:])

print(parrot[:])

#Slicing Negative values

print(parrot[-4:2])

print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[-14:-8])

print(parrot[-14:6])

#Step

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number = "9,223,372,036,854,775,807"

print(parrot[::2])
print(number[1::4])

number = "9,223;372:036 854,775;807"

print(number[1::4])

seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int (val) for val in values] )