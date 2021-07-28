import tkinter as tk
import glob
from PIL import Image, ImageTk
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from io import BytesIO


def svg_png(widget, filename, w, h, row, column):
    "Svg to png to PIL, resize like the window"
    # root.update()
    drawing = svg2rlg(filename)
    mem_png = BytesIO()
    renderPM.drawToFile(drawing, mem_png, fmt="PNG")
    im = Image.open(mem_png)
    im = im.resize((w,h), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    im.image = img
    widget.configure(image=img, bg="yellow", width=w, height=h)
    widget.grid(row=row, column=column)
    return img

root = tk.Tk()

lab = tk.Label(root)
img = svg_png(lab, "label.svg", 200, 50, 0, 0)

font = "Arial 20"
b = tk.Button(
    root,
    bd=0,
    relief="groove",
    activeforeground="red",
    compound="center",
    text="click",
    font=font)
img2 = svg_png(b, "nice.svg", 200, 100, 1, 0)

root.mainloop()
