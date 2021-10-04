**This class resizes the image**
```python
from tkinter importante *
from PIL import Image, ImageTk

class Array(Frame):
    def __init__(self, master, path, *args):
        Frame.__init__(self, master, *args)       self.image = Image.open(path)
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill='both', expand=True)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        self.image = self.img_copy .resize ((self.master .winfo_width(), self.master .winfo_height()))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

```


**Base class control**
```python
class Interface(Frame):
    def __init__(self, master, *args):
        Frame.__init__(self, master, *args)
        self._frame_1 = None
        self._open_1 = False
        self.button1 = Button(self, text='pack 1',
                      command= lambda:self.windows(Show_Image)
        self.button1 .pack()
        self.path_lst = ['_1.png', '_2.png', '_99.jpg']  # change/add paths 
        self.complet = self.frms()
        
    def frms(self):
        lst = []
        for i in (self.path_lst):
            e = Array(self, i)
            lst.append(i)
        return lst

    def windows(self, var_1):
        if not self._open_1:
            self.top1 = Toplevel(self.master)
            self.top1 .geometry('200x200')
                                
        container = var_1(self.top1)

        if self._frame_1 is not None:  
            self._frame_1 .destroy()
        self._frame_1 = container
        self._frame_1 .pack()
        self._open_1 = True

```
**This class should display 3 images in its frame, but I can't think of how to insert it, nor do I have the list of image container frames yet. This is a headache I have.**
```python
class Show_image(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)
        # I intend to display 3 images 
        # in this frame, but how 
        # should I do it?

root = Tk()
frm = Interface(root)
frm .pack()
root.mainloop()
```
