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

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()    


button1 = tkr.Button(player,width=5,height=3, text="PLAY",command=Play)
button2 = tkr.Button(player,width=5,height=3, text="STOP",command=ExitPlayer)
button3 = tkr.Button(player,width=5,height=3, text="PAUSE",command=Pause)
button4 = tkr.Button(player,width=5,height=3, text="UNPAUSE",command=UnPause)


var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)

songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
songtitle.pack()
playlist.pack(fill="both", expand="yes")


player.mainloop()


