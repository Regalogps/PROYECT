from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label


class Example(Frame):
    def __init__(self, master, path, *args):
        Frame.__init__(self, master, *args)

        self.image = Image.open(path)
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


def change_images(index):
    if index >= len(img_lst):
        index = 0
    img_lst[index].lift()
    root.after(1000, change_images, index + 1)
    


path_lst = ['pause_btn.png', 'play_btn.png', 'space.jpg']  # change/add paths here
img_lst = []

root = Tk()

for path in path_lst:
    e = Example(root, path)
    e.place(x=0, y=0, relwidth=1, relheight=1)
    img_lst.append(e)

change_images(0)

root.mainloop()