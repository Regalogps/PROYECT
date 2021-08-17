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
        x=int(self.master.winfo_screenwidth()*0.7)
        y=int(self.master.winfo_screenheight()*0.7)
        z = str(x) +'x'+str(y)
        self.master.geometry(z)

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

        #print(self.background)


class Applications(Tk):  
    def __init__(self, master):
        Tk. __init__(self, master)  
        self.master = master
        self.title("11111")
        self.geometry("195x690")
        self.path = "E:/1-RICHI/MovilesDB"      
        self.Images = self.files(self.path, "ever")   
        self.Images_copy = self.files(self.path, "partial") 

        self.creator = Creator(self)
        self.creator.pack()
        #print(self.Images) 
        #self._toplevel()

    def _toplevel(self):

        self.top = Toplevel()
        self.creator = Creator(self.top)
        self.creator .pack()  

    def files(self, path, option): # Generate list

        images = os.listdir(path)

        self.list_partial= []  
        self.list_ever= []   

        if option == "ever":
            for i in images:

                if ".jpg" in i:
                    route= path + "/" + i

                    open = cv2.imread (route)
                    RGB = cv2.cvtColor(open, cv2.COLOR_BGR2RGB)
                    #objet = Image.fromarray(RGB)
                    #photo = ImageTk.PhotoImage(objet)

                    self.list_ever.append(RGB)

            return self.list_ever

        if option == "partial" :
            for i in images:

                if ".jpg" in i:        
                    route = path + "/" + i   

                    open = cv2.imread(route)
                    RGB = cv2.cvtColor(open, cv2.COLOR_BGR2RGB)
                    objet = Image.fromarray(RGB)

                    self.list_partial.append(objet)

            return self.list_partial  

class Creator(Frame):

    def __init__(self,*args, **kwargs): 
        Frame.__init__(self,*args, **kwargs)

        for i in self.master.Images:
            #print(self.master.Images)
            Example(self, i) .pack()
            

if __name__=="__main__":
    app_1 = Applications()
    app_1.mainloop()