import sqlite3
import tkinter

def getGenre():
    con = sqlite3.connect("cdregal.db")
    cur = con.cursor()
    cur.execute("Select * from genre order by genre_name")
    glist=cur.fetchall()
    con.close()
    print(glist)
    return glist

def getArtist(evt):
    lbxArtist.delete(0, tkinter.END)
    con = sqlite3.connect("cdregal.db")
    cur = con.cursor()
    cur.execute(f"select distinct artist_name from artist\
                    INNER JOIN track on track.artist_id = artist.artist_id\
                    INNER JOIN genre on genre.genre_id = track.genre_id\
                    where genre.genre_name like '%{lbxGenre.get(lbxGenre.curselection())}%'")
    artlist=cur.fetchall()
    print(artlist)
    con.close()
    for artist in artlist:
        lbxArtist.insert(tkinter.END, str(artlist[0]).strip("('',)"))


genres=getGenre()
# artists=getArtist()

app = tkinter.Tk()

app.geometry('1000x500')
app.configure(background='Brown')

lbxGenre=tkinter.Listbox(font=('Tahoma', 12))
lbxArtist=tkinter.Listbox(font=('Tahoma', 12))
lbxAlbum=tkinter.Listbox(font=('Tahoma', 12))
lbxTrack=tkinter.Listbox(font=('Tahoma', 12))

lbxGenre.bind('<<ListboxSelect>>', getArtist)

lblGenre=tkinter.Label(text="Genre", background="Brown", font=('Tahoma', 15), fg="White")
lblArtist=tkinter.Label(text="Artist", background="Brown", font=('Tahoma', 15), fg="White")
lblAlbum=tkinter.Label(text="Album", background="Brown", font=('Tahoma', 15), fg="White")
lblTrack=tkinter.Label(text="Track", background="Brown", font=('Tahoma', 15), fg="White")

lblFilter=tkinter.Label(text="Filter:", background="Brown", font=('Tahoma', 15), fg="White")

inFilterGenre=tkinter.Entry(font=('Tahoma', 15))
inFilterArtist=tkinter.Entry(font=('Tahoma', 15))
inFilterAlbum=tkinter.Entry(font=('Tahoma', 15))
inFilterTrack=tkinter.Entry(font=('Tahoma', 15))

lbxGenre.place(relx=0.01, rely=0.09, relwidth=0.15, relheight=0.7)
lbxArtist.place(relx=0.17, rely=0.09, relwidth=0.25, relheight=0.7)
lbxAlbum.place(relx=0.43, rely=0.09, relwidth=0.25, relheight=0.7)
lbxTrack.place(relx=0.69, rely=0.09, relwidth=0.30, relheight=0.7)

lblFilter.place(relx=0.03, rely=0.82)

lblGenre.place(relx=0.05,rely=0.02)
lblArtist.place(relx=0.27,rely=0.02)
lblAlbum.place(relx=0.50,rely=0.02)
lblTrack.place(relx=0.8,rely=0.02)

inFilterGenre.place(relx=0.01, rely=0.9, relwidth=0.15)
inFilterArtist.place(relx=0.17, rely=0.9, relwidth=0.25)
inFilterAlbum.place(relx=0.43, rely=0.9, relwidth=0.25)
inFilterTrack.place(relx=0.69, rely=0.9, relwidth=0.30)

for genre in genres:
    lbxGenre.insert(tkinter.END, genre[1])

app.mainloop()