from tkinter import *
from PIL import ImageTk, Image
import cv2
import os 
import imutils

class Applications(Tk):

    def __init__(self): 
        Tk. __init__(self)   

        self.path="E:/1-RICHI/MovilesDB"      
        self.Images=self.files(self.path, "ever")   # list one
        self.Images_copy=self.files(self.path, "partial")  # list two
        self._toplevel()

    def files(self, path, option): 

        images=os.listdir(path)
        self.list_partial=[] 
        self.list_ever=[]  
        
        if option == "ever":
            for i in images:
                if ".jpg" in i:       

                    route=path + "/" + i
                    open=cv2.imread (route)
                    if open is None:                 
                        continue
                    RGB=cv2.cvtColor(open, cv2.COLOR_BGR2RGB)
                    objet=Image.fromarray(RGB)
                    photo=ImageTk.PhotoImage(objet)
                    self.list_ever.append(photo)

            return self.list_ever

        if option == "ever" :
            pass  
            # is the same as for total, but up to Image.fromarray

        if option == "parcial" :
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
        frame=Creator()
        frame.pack()


class Creator(Frame):
    def __init__(self,*args, **kwargs): 
        Frame.__init__(self,*args, **kwargs)

        self.LIST=[]
        for i in self.master.Images:
            img=Label(self, image= i)
            img.bind('<Configure>',self.resize)
            img.pack(fill=BOTH, expand=YES)
       
            self.LIST.append(img)

    def resize(self,event):

        new_width =event.width
        new_height=event.height
        for iter in self.LIST:
            ImageTk.PhotoImage(iter.resize((new_width,new_height)))
            

if __name__=="__main__":  
    app_1 =Applications()    
    app_1.mainloop()