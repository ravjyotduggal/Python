locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"
             }

exits = [{"Q": 0},
         {"W": 2, "E": 3,"N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}
         ]
#Challenge1

exits = { 0: {"Q": 0},
         1: {"W": 2, "E": 3,"N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}
          }

#Challenge2

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"
}

loc = 1

for i in exits:
    print(i)

while True:
    available_Exits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are {} ".format(available_Exits))

    for word in vocabulary:
        if word in direction:
            direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Please choose correct exit")