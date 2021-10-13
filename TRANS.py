





from tkinter import *

from PIL import ImageTk, Image
#import pyautogui as pg


root = Toplevel()
root.overrideredirect(1)
root.configure(bg="white")
root.attributes("-topmost", 1)
root.attributes("-transparentcolor", "white")
root.geometry("1000x300+200+300")

f = Frame(root)
f.pack()

label = Label(root, height=900, width=900, bg="white", border=0)
label.pack()


b = Button(f, text='closed', command= lambda: root.destroy())
b.pack()

b = Button(f, text='closefffd', state='disabled', disabledforeground='green', disabledbackground='blue' )
b.pack()


img = Image.open("SSS.png")

imagem = ImageTk.PhotoImage(img)
label.configure(image=imagem)

root.mainloop()