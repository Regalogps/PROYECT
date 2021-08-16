from tkinter import *
from PIL import ImageTk, Image
import cv2
import os 
import imutils

class Example(Frame):
    def __init__(self, master, array, *args):
        Frame.__init__(self, master, *args)

        self.image = Image.fromarray(array)
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill='both', expand=True)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)



class Applications(Tk):  
    def __init__(self):
        Tk. __init__(self)  
        self.path="E:/1-RICHI/MovilesDB"      
        self.Images=self.files(self.path, "ever")   # list one
        self.Images_copy=self.files(self.path, "partial")  # list two
        self._toplevel()

    def files(self, path, option): # here I generate the lists

        images=os.listdir(path) # route
        self.list_partial=[]  # internal list
        self.list_ever=[]      # internal list
        if option == "ever":
            for i in images:
                if ".jpg" in i:
                    route=path + "/" + i
                    open=cv2.imread (route)
                    if open is None:                 
                        continue
                    RGB=cv2.cvtColor(open, cv2.COLOR_BGR2RGB)
                    #objet=Image.fromarray(RGB)
                    #self.list_ever.append(objet)
            return self.list_ever

        if option == "partial" :
            for i in images:
                if ".jpg" in i:        
                    route=path + "/" + i               
                    open=cv2.imread(route)
                    if open is None:                                     
                        continue
                    RGB=cv2.cvtColor(open, cv2.COLOR_BGR2RGB)
                    objet=Image.fromarray(RGB)
                    self.list_partial.append(objet)
            return self.list_partial  

    def _toplevel(self):
        top1=Toplevel()
        frame=Creator(top1)
        frame.pack()  

class Creator(Frame):

    def __init__(self,*args, **kwargs): 
        Frame.__init__(self,*args, **kwargs)

        self.LIST=[]          # img_lst
        for i in self.master.Images:
            Example(self, i).place(x=0, y=0, relwidth=1, relheight=1)
       
if __name__=="__main__":
    app_1 =Applications()
    app_1.mainloop()