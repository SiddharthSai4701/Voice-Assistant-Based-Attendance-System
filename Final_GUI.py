'''
Code for GUI!!
'''
from tkinter import *
import pyttsx3
import pandas as pd
import pygame
from PIL import ImageTk, Image

root = Tk()

root.title("PhY - Borg")

p1 = PhotoImage(file = "D:\\College\\6th sem\\UPHY 608\\Project\\Finally\\icon.png")
root.iconphoto(False, p1)

greet = Label(root,text = 'Sairam from PhyBorg!',fg = "orange")
font_tuple = ("Comic Sans MS",20,"bold")
greet.configure(font=font_tuple)

img = ImageTk.PhotoImage(Image.open("D:\\College\\6th sem\\UPHY 608\\Project\\Finally\\2.jpg"))
frame = Frame(root)

global engine
engine = pyttsx3.init()
#Defining functions to perform various different tasks
def voice_control():
    # global engine
    # engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')      #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female and 0 for male

def SpeakText(command):
    # global engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def Attendance():
    #voice_control()
    import Integrated
    
def Pray():
    
    pry = Tk()
    pry.title("PraYer")
    head = Label(pry,text = 'PraYer', fg = "blue")
    head.config(font = ("Courier",20))

    #Use of Pygame for playing music
    def play():
        pygame.mixer.init()
        if clicked.get() == "Sarva Dharma Prayer":
            pygame.mixer.music.load("Sdp.mp3")
            pygame.mixer.music.play()
        elif clicked.get() == "Gayatri mantra":
            pygame.mixer.music.load("Gyt.mp3")
            pygame.mixer.music.play()
    def pause():
        pygame.mixer.music.pause()
        
    def resume():
        pygame.mixer.music.unpause()
        
    def stop():
        pygame.mixer.music.stop()

    #Dropdown
    clicked = StringVar()
    clicked.set("-Select-")
    options = ["Sarva Dharma Prayer","Gayatri mantra"]
    drop = OptionMenu(pry,clicked,*options)
    
    play = Button(pry,text = "PLAY",command = play, padx = 15,fg = "#FF1493")
    pause = Button(pry,text = "PAUSE",command = pause, padx = 15,fg = "#FF1493")
    resume = Button(pry,text = "RESUME",command = resume, padx = 15,fg = "#FF1493")
    stop = Button(pry,text = "STOP",command = stop, padx = 15,fg = "#FF1493")
    
    head.grid(row = 0, column = 1)
    drop.grid(row = 1, column = 1)
    play.grid(row = 2, column = 0)
    resume.grid(row = 2, column = 1)
    pause.grid(row = 2, column = 2)
    stop.grid(row = 3, column = 1)
    
    pry.mainloop()
    
atd = Button(root,text = "ATTENDANCE",command = Attendance, fg = 'blue', padx = 20, pady = 100)
pray = Button(root, text = "PRAYER", command = Pray, fg = 'red', padx = 30, pady = 100)

pic = Label(frame, image = img)

greet.grid(row = 0, column = 1)
atd.grid(row = 1, column = 0)
pray.grid(row = 1 , column = 2)

pic.grid(row = 1, column = 1)
frame.grid(row = 1, column = 1)

root.mainloop()