from tkinter import *

class Move():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._unmovable = []
        
    def make_unmovable(self, *widgets):
        self._unmovable.extend(widgets)
        
    def _is_movable(self, widget):
        return widget not in self._unmovable

    def start_move2(self, event):        
        self._x = event.x
        self._y = event.y

    def stop_move2(self, event):
        self._x = None
        self._y = None

    def on_move2(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        win = event.widget.winfo_toplevel()

        new_position = "+{}+{}".format(win.winfo_x() + deltax, win.winfo_y() + deltay)
        if not self._is_movable(event.widget):
         #return
    
            win.geometry(new_position) 

        #print('print:', event.widget.winfo_parent())
        if event.widget.winfo_parent() == '.!a1.!toplevel.!frame.!frame.!label':
            print('You found me but you have 0')


class A1 (Frame, Move):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        Move.__init__(self)
        self.master = master
        self.btn = Button(self, text='opens', command=self.open)
        self.btn .pack()

        self.bind_all("<ButtonPress-1>", self.start_move2)
        self.bind_all("<B1-Motion>", self.on_move2)
        self.bind_all("<ButtonRelease-1>", self.stop_move2)

    def open(self):
        self.w1 = Toplevel(self)
        self.w1 .overrideredirect(1)
        self.w1 .wm_attributes ('-topmost', True)        
        self.w2 = Toplevel(self)
        self.w2 .overrideredirect(1)
        self.w2. wm_attributes ('-topmost', True) 

        self.w1 .geometry('300x150')
        self.w2 .geometry('300x150')

        self.frame_1 = Frame(self.w1, bg='green')
        self.label_1 = Label(self.frame_1, text='___windows 1___', bg='green2', width=50)
        self.btn_1 = Button(self.label_1, text='AAAAAAA')

        self._frame_1 = Frame(self.frame_1, bg='green')
        self._label_1 = Label(self._frame_1, text='windows 1', bg='green2', width=50)
        self._btn_1 = Button(self._label_1, text='button 2 - A')   #
        self._bbn_11 = Button(self._label_1, text='button 3 - A')

        self.frame_2 = Frame(self.w2, bg='green')
        self.label_2 = Label(self.frame_2, text='___windows 2___', bg='green2', width=50)
        self.btn_2 = Button(self.label_2, text='BBBBBBB')

        self._frame_2 = Frame(self.frame_2, bg='green')
        self._label_2 = Label(self._frame_2, text='windows 1', bg='green2', width=50)
        self._btn_2 = Button(self._label_2, text='button 2 - B')
        self._bbn_22 = Button(self._label_2, text='button 3 - B')

        self.frame_1 .pack()
        self.label_1 .pack()
        self.btn_1 .pack()
        self._frame_1 .pack()
        self._label_1 .pack()
        self._btn_1 .pack()
        self._bbn_11 .pack()
        
        self.frame_2 .pack()
        self.label_2 .pack()
        self.btn_2 .pack()
        self._frame_2 .pack()
        self._label_2 .pack()
        self._btn_2 .pack()
        self._bbn_22 .pack()

        self.make_unmovable(self._btn_1, self._btn_2)

root = Tk()
app = A1(root, bg='black')
app .pack(side=BOTTOM, fill=BOTH)
root .mainloop()