t = "a","b","c"

print(t)
print("a","b","c")
print(("a","b","c"))

t = ("a","b","c")
print(t)

print(t[1])

welcome = "Welcome to my Nightmare","Alice Cooper",1975
bad = "Bad company","Bad company",1974
budgie = "Nightflight", "Budgie",1981
imelda = "More Mayhem","Emilda May",2011
metallica = "Ride the Lightning","Metallica",1984

print(metallica)
print(metallica[0])

#Changes in Tuple

imelda = imelda[0],"Imelda May",imelda[2]

imelda = imelda[0],"Hello how are you",imelda[2]

print(imelda)

#Unpacking the tuples

title, artist , year = imelda
print(title)
print(artist)
print(year)

welcome = "Welcome to my Nightmare","Alice Cooper",1975
bad = "Bad company","Bad company",1974
budgie = "Nightflight", "Budgie",1981
imelda = "More Mayhem","Imilda May",2012, ((1,"Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
metallica = "Ride the Lightning","Metallica",1984

title, artist, year, tracks = imelda
tracks = imelda[3]

print(title)
print(artist)
print(year)
print(tracks)
print("")
for i in imelda:
    print(i)

imelda = "More Mayhem","Imilda May",2011, (
    (1,"Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

#Lists in tuple

imelda = "More Mayhem","Imilda May",2011, [
    (1,"Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]

for i in imelda:
    print(imelda[0], ",", imelda[1],",",imelda[2])
    break
for h in imelda[3]:
    print("\t Track number is {} and song is {}".format(h[0],h[1]))