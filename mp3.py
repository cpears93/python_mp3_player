import pygame
import tkinter as tkr

"""Create Window"""
player = tkr.Tk()

"""Edit Window"""
player.title("mp3 Player")
player.geometry("300x600")

"""Get Song"""
file = "Song.mp3"


"""Action Event"""
def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()

"""Register Buttons"""
Button1 = tkr.Button(player,width=5,height=3, text="PLAY",command=Play)
Button1.pack(fill ="x")
Button2 = tkr.Button(player,width=5,height=3, text="STOP",command=ExitPlayer)
Button2.pack(fill ="x")

"""Song Name"""
label1 = tkr.LabelFrame(player, text="Song Name")
label1.pack(fill="both", expand="yes")
contents1 = tkr.Label(label1, text = file)
contents1.pack()


"""Activate"""
player.mainloop()
