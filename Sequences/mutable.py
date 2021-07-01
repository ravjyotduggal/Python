shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(id(shopping_list))

a = b=c=d=e=f=another_list
print(a)

print("Adding Cream")
b.append("cream")

print(b)
print(d)

ip_address = input("Please enter your IP Address: ")
a = ip_address.count(".")

print("There are {} dots in your IP Address: {}".format(a,ip_address))