import sys
import cv2
import numpy as np
import pyautogui
import os

if ("video" in os.listdir()):
    f="t"
else:
    os.mkdir("video")

def record_screen_v(outputavi, num1):
    SCREEN_SIZE = tuple(pyautogui.size())
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # frames per second
    fps = 12.0
    # create the video write object
    out = cv2.VideoWriter(outputavi, fourcc, fps, (SCREEN_SIZE))
    # the time you want to record in seconds
    record_seconds = num1

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

#export the video is random name in .avi format
filename = str(len(os.listdir("video")))+".avi"

record_screen_v("video/"+filename,10000)