import cv2
import numpy as np
import pyautogui
import platform
import shutil
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile as save_as
from tkinter import simpledialog
import os
import webbrowser


t= Tk()

t.title("Screen")
t.geometry("220x250")
t.resizable(0,0)
k=os.listdir()

#function for releasing recorded video
def rls():
    t = save_as()
    l="video/"+str(len(os.listdir("video"))-1)+".avi"
    if (t == None):
        messagebox.showerror("Error","You need to enter filename")
    else:
        t = t.name+".avi"
        shutil.copy(l,t)
        shutil.rmtree("video")
        os.mkdir("video")
        p3.place(x=150,y=1000)
        messagebox.showinfo("File saved","Your file has been saved")

#checking the presence of cache file in file system
if ("cache" in k):
    open("cache","w").write("")
else:
    open("cache","a").write("")

#For start recording, this function writes "" in cache file, due to which the main.py file starts recording the screen
def ply():
    if("win" in platform.system()):
        os.startfile("main.py")
    elif(platform.system() == "Linux"):
        os.open("main.py")
    else:
        messagebox.showinfo("Problem","This app has no support for "+platform.system())
    open("cache","w").write("")
    p2.place(x=15,y=80)
    p1.place(x=150,y=1000)

#For stop recording, this function writes "stop" in cache file, due to which the main.py file stop recording the screen
def stp():
    open("cache","w").write("stop")
    p1.place(x=15,y=80)
    p3.place(x=15,y=150)
    p2.place(x=150,y=1000)

def ghb():
    try:
        webbrowser.open("https://github.com/abhineetraj1")
    except Exception as ss:
        try:
            messagebox.showerror("Error",str(ss))
        except:
            messagebox.showerror("Error","Not able to open your default browser, kindly examine your system's default browser!")

Label(t, background="#659bdf", height=3, width=500).place(x=0,y=0)
Label(t, background="#659bdf", text="Screen recorder",  font=('Comic sans MS', 19)).place(x=10,y=0)
Label(t, background="white", height=30, width=500).place(x=0,y=50)

p1= Button(t, text="Start recording",font=('Comic sans MS',15) , command=ply, background="#659bdf",foreground="white", activebackground="white", activeforeground="black")
p2= Button(t, text="Stop recording", font=('Comic sans MS',15) , command=stp, background="#659bdf",foreground="white", activebackground="white", activeforeground="black")
p3= Button(t, text="Release video",  font=('Comic sans MS',15) , command=rls, background="#659bdf",foreground="white", activebackground="white", activeforeground="black")

Button(t, text="By Abhineet Raj",  font=('Comic sans MS',13) , command=ghb, background="black",foreground="white", activebackground="white", activeforeground="black").place(x=10,y=210)


p1.place(x=15,y=80)
p2.place(x=1500,y=1000)
t.mainloop()
