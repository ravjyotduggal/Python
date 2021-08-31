import sqlite3
import tkinter


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):

        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):

        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None
        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)
            self.cursor.execute(self.sql_select + self.sql_sort)

        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)
            index = self.curselection()[0]

            print("Index value is {}".format(index))
            value = self.get(index),
            print("value is {}".format(value))
            if self.link_value:
                value = value[0], self.link_value
                sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            else:
                sql_where = " WHERE " + self.field + "=?"
            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            print(self.sql_select)
            print(self.field)
            print(link_id)
            self.linked_box.requery(link_id)
        # alist = []
        # for row in conn.execute("select albums.name from albums where albums.artist = ? order by albums.name", artist_id):
        #     alist.append(row[0])
        # albumLV.set(tuple(alist))
        # songsLV.set("Please choose an album")
        # holdvalue = index

# def get_albums(event):
#     global holdvalue
#     lb = event.widget
#     try:
#         index = lb.curselection()[0]
#     except IndexError:
#         index = holdvalue
#     artist_name = lb.get(index),
#     artist_id = conn.execute("select artists._id from artists where artists.name = ?", artist_name).fetchone()[0]
#     albumList.requery(artist_id)
#     # alist = []
#     # for row in conn.execute("select albums.name from albums where albums.artist = ? order by albums.name", artist_id):
#     #     alist.append(row[0])
#     # albumLV.set(tuple(alist))
#     # songsLV.set("Please choose an album")
#     # holdvalue = index


# def get_songs(event):
#     lb = event.widget
#     try:
#         index = int(lb.curselection()[0])
#         album_name = lb.get(index),
#         album_id = conn.execute("select _id from albums where name = ?", album_name).fetchone()
#         alist = []
#         for songs in conn.execute("select title from songs where album = ?", album_id):
#             alist.append(songs[0])
#         songsLV.set(tuple(alist))
#     except IndexError:
#         songsLV.set("Please choose an album")

if __name__ == '__main__':
    conn = sqlite3.connect("music.sqlite")
    mainWindow = tkinter.Tk()
    mainWindow.title("Music DB Browser")
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1) # Spacer column on right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    holdvalue = 0

    #labels

    tkinter.Label(mainWindow, text="Aritsts").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    #Artists Listbox

    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
    artistList.config(border=2, relief='sunken')

    # for artist in conn.execute("select * from artists order by artists.name"):
    #     artistList.insert(tkinter.END, artist[1])

    artistList.requery()
    #artistList.bind('<<ListboxSelect>>', get_albums)
    #Albums Listbox

    albumLV = tkinter.Variable(mainWindow)
    albumLV.set("Choose an artist")
    # albumList = Scrollbox(mainWindow, listvariable=albumLV)
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    #albumList.requery()
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
    albumList.config(border=2,relief='sunken')

    #albumList.bind("<<ListboxSelect>>", get_songs)
    artistList.link(albumList, "artist")

    #Songs Listbox
    songsLV = tkinter.Variable(mainWindow)
    songsLV.set("Choose an album")
    #songList = Scrollbox(mainWindow, listvariable=songsLV)
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    #songList.requery()
    songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList,'album')

    # for i in conn.execute("Select * from artists"):
    #     artistList.insert(tkinter.END, i[1])

    mainWindow.mainloop()
    print("Closing database connection")
    conn.close()


