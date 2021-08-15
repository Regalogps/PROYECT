class Creator(Frame):

    def __init__(self,*args, **kwargs):
        Frame.__init__(self,*args, **kwargs)

        self.LIST=[]          # label list
        for index, i in enumerate(self.master.Images):
            img=Label(self, image= i)
            img.bind('<Configure>', lambda e, lbl=img, index=index: self.resize(e, lbl, index))
            img.pack(fill=BOTH, expand=YES)
            self.LIST.append(img)

    def resize(self,event, label, index):

        new_width =event.width
        new_height=event.height
        img = self.master.Images_copy[index].resize((new_width, new_height))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)