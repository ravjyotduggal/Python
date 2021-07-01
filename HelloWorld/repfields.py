age = 24

print("My age is " + str(age) + " years")

print("my age is " + str(age) + " Years")

#Replacement Fields

print("My age is {0} years".format(age))

print("There are {0} days in {1},{2},{3},{4},{5},{6} and {7}"
      .format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))

print("""Jan: {0} \
Feb : {1} \
Mar: {0} \
April: {2} \
May: {2}""".format(31,28,30))

print("Jan: {0}, \n Feb {1}, \n Mar {2}".format(20,22,34) )