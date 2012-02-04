# File: image_manipulator.py
#
# http://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_text-method

from Tkinter import *
from PIL import Image, ImageTk


class App:
    #current_image = Image
    photo = ImageTk
    frame = Frame
    mouse_pos = (0,0)
    def __init__(self, master):

        self.frame = Frame(master)
        master.bind("<Button-1>",self.mouse_click);
        master.bind("<B1-Motion>",self.mouse_move);
        self.frame.pack()

        scrollbar = Scrollbar(master)
        scrollbarx = Scrollbar(master,orient=HORIZONTAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        scrollbarx.pack(side=BOTTOM,fill=X)
        
        self.button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(self.frame,text="Hello",command=self.say_hi)
        self.hi_there.pack(side=LEFT)


        
        self.canvas = Canvas(master, width=500, height=600)
        self.canvas.pack(side=BOTTOM)
        #self.canvas.create_line(0,0,200,100)


        current_image = Image.open("evie.jpg")
        sizex, sizey = current_image.size;

        current_image = current_image.resize( (sizex/4,sizey/4) )
        current_image = current_image.transpose( Image.ROTATE_270 )

        #print image
        self.photo = ImageTk.PhotoImage(current_image)

        self.canvas.create_image(350,350,image=self.photo)
        self.canvas.config(scrollregion=self.canvas.bbox(ALL),
                           relief=SUNKEN,
                           yscrollcommand=scrollbar.set,
                           xscrollcommand=scrollbarx.set )
        scrollbar.config(command=self.canvas.yview)
        scrollbarx.config(command=self.canvas.xview)
        
        
       
        

    def say_hi(self):
        print "hi there, everyone!"
        self.canvas.create_text(110,110,text="hi everyone")

    def mouse_move(self,event):
        #self.frame.focus.set()
        print "clicked at", event.x, event.y
        print "begin ", self.mouse_pos
        current = (self.canvas.canvasx(event.x),
                   self.canvas.canvasy(event.y))
        self.canvas.create_line(
            self.mouse_pos[0],self.mouse_pos[1],
            current[0], current[1] )
        self.mouse_pos = current
       
    def mouse_click(self,event):
        #self.frame.focus.set()
        print "clicked at", event.x, event.y
        self.mouse_pos = ( self.canvas.canvasx(event.x),
                           self.canvas.canvasy(event.y) )

root = Tk()


app = App(root)

root.mainloop()
root.destroy()
