import tkinter as tk
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title('Text to speech')
root.geometry('900x450+200+200')
root.resizable(False,False)
root.configure(bg='#305065')


#icon
image_icon=PhotoImage(file='/home/dev/Desktop/aws_dynamo/s.png')
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg='white',width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file='/home/dev/Desktop/aws_dynamo/s.png')
#Lable(Top_frame,bg='white').place(x=10,y=5)
Label(Top_frame,image=Logo,bg='white').place(x=10, y=5)
Label(Top_frame,text='TEXT TO SPEECH',font='arial 20 bold',bg='white',fg='black').place(x=100,y=3)
root.mainloop()