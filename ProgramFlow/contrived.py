numbers = [1,45,31,52,60]

for number in numbers:
    if number % 8 == 0:
        print("These numbers are unacceptable")
        break
else:
    print("All those numbers are fine")

directions = ["north","south","east","west"]
search = ""
found_at = None

while search not in directions:
    search = input("{} is not in the list, Please enter the direction: ".format(search))

found_at = directions.index(search)
print("Your direction is {}".format(search))
print("The position is at {} ".format(found_at))


