import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Voicify")
root.geometry("900x450")
root.resizable(0, 0)
root.configure(bg="#ae4b50")

engine = pyttsx3.init()

# Function to voicify the texts
def speakNow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed= speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setVoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    
    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setVoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setVoice()
        else:
            engine.setProperty('rate', 80)
            setVoice()
            
    
# Function to download the recorded voices
def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed= speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setVoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
    
    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setVoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setVoice()
        else:
            engine.setProperty('rate', 80)
            setVoice()

# icon
image_icon = PhotoImage(file="speaker logo.png")
root.iconphoto(False, image_icon)

# Top frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file = "speaker logo.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="VOICIFY", font="arial 20 bold", bg="white", fg="black").place(x=100, y=30)

###########

text_area = Text(root, font="Robote 14", bg="white",relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#ae4b50", fg="white").place(x=565, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#ae4b50", fg="white").place(x=745, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 11", state="r", width=14)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 11", state="r", width=14)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

imageicon = PhotoImage(file="speak.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=130, font="arial 12 bold", command=speakNow)
btn.place(x=550, y=280)

imageicon2 = PhotoImage(file="download.png")
save_btn = Button(root, text="Save", compound=LEFT, image=imageicon2, width=130,bg="#eee148", font="arial 12 bold", command=download)
save_btn.place(x=730, y=280)



root.mainloop()