from multiprocessing import*
import cv2
import numpy as np
from time import sleep
import pyautogui
import platform
import shutil
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile as save_as
from tkinter import simpledialog
import os
import webbrowser


def record_screen_v():
    SCREEN_SIZE = tuple(pyautogui.size())
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # frames per second
    fps = 12.0
    # create the video write object
    out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))
    # the time you want to record in seconds
    record_seconds = 100000
    for i in range(int(record_seconds * fps)):
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # if the user clicks the button stop recording, it exits
        if (open("cache","r").read() == "stop"):
            open("cache","w").write("")
            break
    cv2.destroyAllWindows()
    out.release()

def rec():
    if ("__cache__" in os.listdir()):
        open("__cache__","w").write("")
    else:
        open("__cache__","a").write("")
    while(0<1):
        y=open("__cache__","r").read()
        if (y == "do"):
            record_screen_v()
        else:
            sleep(2)

#function for releasing recorded video
def main_l():
    def rls():
        t = save_as()
        l="output.avi"
        if (t == None):
            messagebox.showerror("Error","You need to enter filename")
        else:
            t = t.name+".avi"
            shutil.copy(l,t)
            p3.place(x=150,y=1000)
            messagebox.showinfo("File saved","Your file has been saved")
    
    #checking the presence of cache file in file system
    if ("cache" in os.listdir()):
        open("cache","w").write("")
    else:
        open("cache","a").write("")
    
    ##export the video is random name in .avi format
    #filename = str(len(os.listdir("video")))+".avi"
    
    #For start recording, this function writes "" in cache file, due to which the main.py file starts recording the screen
    def ply():
        open("__cache__","w").write("do")
        open("cache","w").write("")
        p2.place(x=15,y=80)
        p1.place(x=150,y=1000)
    
    #For stop recording, this function writes "stop" in cache file, due to which the main.py file stop recording the screen
    def stp():
        open("__cache__","w").write("")
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
    t= Tk()
    t.title("Screen")
    t.geometry("220x250")
    t.resizable(0,0)
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

if __name__ == '__main__':
    t= Process(target=main_l)
    t2=Process(target=rec)
    t.start()
    t2.start()
    t.join()