from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    print("")
    choice = int(input("Please enter the Album number: "))
    if 1<=choice<=len(albums):
        for song_list in albums[choice -1][SONG_LIST_INDEX]:
            print("\t{}: {}".format(song_list[0],song_list[1]))
    else:
        break
    print("Please choose your song name: ")
    song_index = int(input())
    if 1<=song_index<=len(albums[choice -1][SONG_LIST_INDEX]):
        print("Playing: {}".format(albums[choice -1][SONG_LIST_INDEX][song_index -1][SONG_TITLE_INDEX]))
        print("*" * 40)



