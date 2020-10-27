import pygame
import tkinter as tkr
import os

player = tkr.Tk()


player.title("mp3 Player")
player.geometry("300x600")

os.chdir("C:\Users\Chris' PC\Downloads\mp3 playlist")
songlist = os.listdir()



pygame.init()
pygame.mixer.init()

def Play():
    
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()


Button1 = tkr.Button(player,width=5,height=3, text="PLAY",command=Play)
Button2 = tkr.Button(player,width=5,height=3, text="STOP",command=ExitPlayer)

contents1 = tkr.Label(label1, text=file)

Button1.pack(fill="x")
Button2.pack(fill="x")
contents1.pack()


player.mainloop()


