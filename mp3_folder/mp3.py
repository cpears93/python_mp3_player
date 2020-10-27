import pygame
import tkinter as tkr
import os

player = tkr.Tk()


player.title("mp3 Player")
player.geometry("300x600")

os.chdir("C:\Users\Chris' PC\Downloads\mp3 playlist")
print(os.getcwd)
songlist = os.listdir()

playlist = tkr.listbox(player,highlightcolor="blue",selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1


pygame.init()
pygame.mixer.init()

def Play():
    
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()


Button1 = tkr.Button(player,width=5,height=3, text="PLAY",command=Play)
Button2 = tkr.Button(player,width=5,height=3, text="STOP",command=ExitPlayer)


var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
songtitle.pack()
playlist.pack(fill="both", expand="yes")


player.mainloop()


