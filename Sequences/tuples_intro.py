welcome = "Welcome to my Nightmare","Alice Cooper",1975
bad = "Bad Company", "Bad Company",1974
budgie = "Nightflight","Budgie",1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning","Metallica", 1984

# print(metallica)
#
# print(metallica[1][2])
#
# metallica_2 = list(metallica)
# print(metallica_2)

albums = [
    ("Welcome to my Nightmare","Alice Cooper",1975),
    ("Bad Company", "Bad Company",1974),
    ("Nightflight","Budgie",1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning","Metallica", 1984)
    ]

for name, artist, year in albums:
     print("Ablum: {}, Artist: {}, Year: {}".format(name, artist, year))


