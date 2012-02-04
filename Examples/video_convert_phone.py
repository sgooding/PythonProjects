# File: image_manipulator.py
#
# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_text-method

###########################################
## Imports
###########################################
from Tkinter import *

import Dialog
import os
import tkFileDialog
import subprocess

from multiprocessing import Process

from PIL import Image, ImageTk

###########################################
## Project Dialog Class
###########################################
class MyDialog:
    mProjectName = ""

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Project Name").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        #print "value is", self.e.get()
        self.mProjectName = self.e.get()
        self.top.destroy()
                                
def run_program(command):
    print "Running DVD Fab"
    os.system(command)
                                
###########################################
## App Class
###########################################
class App:
    #current_image = Image
    frame = Frame
    mProjectName = ""
    mRootDir = "C:\Users\Sean\Videos"
    mTitle = ""
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()

        self.mTitle = StringVar()
        self.mTitle.set("New Project")
        Label(master,textvariable=self.mTitle).pack()
       
        self.button = Button( master,
                              text="QUIT",
                              fg="red",
                              command=self.frame.quit )
        
        self.button.pack(side=TOP)

        self.hi_there = Button(master,text="Project Name",command=self.say_hi)
        self.hi_there.pack(side=TOP)
        

        self.open_dvdfab = Button(master,text="Run DVDFab",command=self.open_dvd_fab)
        self.open_dvdfab.pack(side=TOP)

        self.open_handbrake = Button(master,text="Run Handbrake",command=self.open_handbrake)
        self.open_handbrake.pack(side=TOP)

        
        self.convert_file = Button(master,text="Convert to phone",command=self.convert)
        self.convert_file.pack(side=TOP)
                

    def say_hi(self):
        print "hi there, everyone!"
        d = MyDialog(self.frame)
        self.frame.wait_window(d.top)
        self.mProjectName = d.mProjectName

        print "project name = "
        print self.mProjectName
        self.mTitle.set(self.mProjectName)



    def open_dvd_fab(self):
        # New Command c:\Program Files (x86)\DVDFab 6>DVDFab.exe /MODE "DVDGENERIC" /SRC "E:\VIDEO_TS\
        # " /DEST "C:\Users\Sean\Videos\FullDisks\" /CLOSE
        #command = "\"%PROGRAMFILES(X86)%\DVDFab\ 6\DVDFab.exe\""
        command = "DVDFab.exe"
        command += " /MODE \"DVDGENERIC\" /SRC \"E:\\VIDEO_TS\\ \""
        command += " /DEST \""
        command += self.mRootDir
        #command += "\\"
        #command += self.mProjectName
        command += "\\ \""
        command += " /CLOSE"
        #print command
        process = Process(target=run_program,args=(command,));
        process.start()
        #process.join()
        #os.system(command)
 
    def open_handbrake(self):
        
        command = "\"C:\Program Files (x86)\Handbrake\HandBrakeCLI.exe\""
        command += " -i "
        input_dir = tkFileDialog.askdirectory();
        command += input_dir
        command += " -o "
        command += self.mRootDir
        command += "\\"
        command += self.mProjectName
        command += ".mp4"
        process = Process(target=run_program,args=(command,));
        process.start()
        #print " -o movie.mp4 --preset=\"Normal\""   

        #os.system(command)

    def convert(self):
        ffmpeg_path = "C:\\Users\\Sean\\Downloads\\MediaConversion\\ffmpeg-r16537-gpl-static-win32.tar\\ffmpeg-r16537-gpl-static-win32\\bin\\"
        command = ffmpeg_path
        command += "ffmpeg.exe -i "
        command += self.mRootDir
        command += "\\"
        command += self.mProjectName
        command += ".mp4"
        command += " -s qcif -vcodec libx264 -acodec libfaac -ac 1 -r 25 -ab 128000 -s 480x320 -y "
        command += self.mRootDir
        command += "\\"
        command += self.mProjectName
        command += ".3gp"
        print command
        process = Process(target=run_program,args=(command,));
        process.start()
        
     
###########################################

###########################################
## Main Entry
###########################################        

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
    root.destroy()

###########################################
