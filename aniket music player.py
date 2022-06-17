import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resume")
    mixer.music.unpause()

root=Tk()
root.title("Ani Music player")

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="lime",font=('Times New Roman',14),width=55)
playlist.grid(columnspan=5)

os.chdir(r'D:\music songs')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('Times New Roman',14),bg="green",fg="white",padx=3,pady=3)
playbtn.grid(row=1,column=0)

playbtn=Button(root,text="Pause",command=pausesong)
playbtn.config(font=('Times New Roman',14),bg="royalblue",fg="white",padx=3,pady=3)
playbtn.grid(row=1,column=1)

playbtn=Button(root,text="Stop",command=stopsong)
playbtn.config(font=('Times New Roman',14),bg="red",fg="white",padx=3,pady=3)
playbtn.grid(row=1,column=2)

playbtn=Button(root,text="Resume",command=resumesong)
playbtn.config(font=('Times New Roman',14),bg="tan",fg="white",padx=3,pady=3)
playbtn.grid(row=1,column=3)

mainloop()


