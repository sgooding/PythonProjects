# File: tkinter_hello_world_2.py
#
# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_text-method

from Tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self, master,image):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame,text="Hello",command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.canvas = Canvas(master, width=2592, height=1944)
        self.canvas.pack(side=BOTTOM)
        #self.canvas.create_line(0,0,200,100)



        self.canvas.create_image(350,350,image=photo)
        
        
        

    def say_hi(self):
        print "hi there, everyone!"
        self.canvas.create_text(110,110,text="hi everyone")

root = Tk()
image = Image.open("evie.jpg")
sizex, sizey = image.size;
print image.size
image = image.resize( (sizex/4,sizey/4) )
image = image.transpose( Image.ROTATE_270 )
#print image
photo = ImageTk.PhotoImage(image)

app = App(root,photo)

root.mainloop()
