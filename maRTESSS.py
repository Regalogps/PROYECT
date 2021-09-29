from tkinter import *

import time
import os

class Application(Frame):
    def __init__(self, parent):
       Frame.__init__(self,parent)
       self.pack(fill=BOTH)

       self.create_widgets()

    def create_widgets(self):
        self.borderFrame = Frame(self, width=500, height=600, bg="Gray")
        self.borderFrame.pack_propagate(False)
        self.borderFrame.pack(side=TOP)

        self.holderFrame = Frame(self.borderFrame, width=500, height=570, bg="blue")
        self.holderFrame.pack_propagate(False)
        self.holderFrame.pack(side=BOTTOM)

        self.close = Label(self, font=("Arial", 11), bg="Gray", anchor=CENTER, text="X", cursor="hand2")
        self.close.place(x=460, y=0, width=40, height=30)

        self.min = Label(self, font=("Arial", 11), bg="Gray", anchor=CENTER, text="_", cursor="hand2")
        self.min.place(x=420, y=0, width=40, height=30)

        def hoverMin(event):
            event.widget.config(bg="lightBlue")

        def unHoverMin(event):
            event.widget.config(bg="Gray")

        self.min.bind("<Enter>", hoverMin)
        self.min.bind("<Leave>", unHoverMin)
        self.min.bind("<Button-1>", self.minimize)

        def hover(event):
            event.widget.config(bg="red")

        def unhover(event):
            event.widget.config(bg="Gray")

        self.close.bind("<Enter>", hover)
        self.close.bind("<Leave>", unhover)
        self.close.bind("<Button-1>", self.exitProgram)

        self.borderFrame.bind("<Button-1>", self.startMove)
        self.borderFrame.bind("<ButtonRelease-1>", self.stopMove)
        self.borderFrame.bind("<B1-Motion>", self.moving)

        self.borderFrame.bind("<Map>",self.frame_mapped)

    def startMove(self, event):
        self.x = event.x
        self.y = event.y

    def stopMove(self, event):
        self.x = None
        self.y = None

    def moving(self,event):
        x = (event.x_root - self.x - self.borderFrame.winfo_rootx() + self.borderFrame.winfo_rootx())
        y = (event.y_root - self.y - self.borderFrame.winfo_rooty() + self.borderFrame.winfo_rooty())
        root.geometry("+%s+%s" % (x, y))

    def frame_mapped(self,e):
        print(self,e)
        root.update_idletasks()
        root.overrideredirect(True)
        root.state('normal')


    def minimize(self, event):
        root.update_idletasks()
        root.overrideredirect(False)
        #root.state('withdrawn')
        root.state('iconic')

    def exitProgram(self, event):
        os._exit(0)

root = Tk()
root.title("Draggable Root")
root.geometry("500x600")
root.overrideredirect(True)

app = Application(root)

root.mainloop()