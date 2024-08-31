from tkinter import * 
from PIL import Image,ImageTk,ImageSequence 
import time
import pygame 
from pygame import mixer
mixer.init()

root = Tk()
# root.geometry("1280x720")
root.attributes('-fullscreen', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("GUI2.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((screen_width, screen_height))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop() 