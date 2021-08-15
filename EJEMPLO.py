from tkinter import *
from PIL import ImageTk, Image
import cv2
import os 
import imutils



class Applications(Tk):

    def __init__(self): 
        Tk. __init__(self)   
        self.title("PRINCIPAL")

        self.path="E:/1-RICHI/MovilesDB"  
           
        self.Images_init=self.files(self.path, "ever")   # list one
        self.Images_copy_init=self.files(self.path, "partial")  # list two
       # self._toplevel()
        #self.frame=Creator(self)
        #self.frame .pack()

        

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

   # def _toplevel(self):
      #  self.top1=Toplevel(self)
      #  self.top1.title("segundaria")
      #  self.frame=Creator()
      #  self.frame.pack()

        

        


class Creator(Frame):
    def __init__(self,*args, **kwargs): 
        Frame.__init__(self,*args, **kwargs)

        self.LIST=[]          # label list
        for index, i in enumerate(self.master.Images_init):
            img=Label(self, image= i)
            img.bind('<Configure>', lambda e, lbl=img, index=index: self.resize(e, lbl, index))
            img.pack(fill=BOTH, expand=YES)
            self.LIST.append(img)
        print(len(self.LIST))

    def resize(self,event, label, index):

        new_width =event.width
        new_height=event.height
        img = self.master.Images_copy_init[index].resize((new_width, new_height))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
            

if __name__=="__main__":  
    app_1 =Applications()    
    app_1.mainloop()