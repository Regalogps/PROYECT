
def creator(self):
    lst = []
    arg1, arg2, = 0, 1,
    for i in range(9):   
        btn = Button(self, text='buttons')#
              #command=lambda: self.windows(
              #lambda top1: Class1(top1, i, arg1, arg2, path),
              #lambda top2: Class2(top2, i, arg1, arg2, path),
              #lambda top3: Class3(top3, i, arg1, arg2, path)))
        lst.append(btn)
    
    lst[0].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))
    
    lst[1].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))

    lst[2].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))

    lst[3].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))

    lst[4].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))

    lst[5].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))

    lst[0].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))

    lst[0].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 0, arg1, arg2, path),
               lambda top2: Class2(top2, 0, arg1, arg2, path),
               lambda top3: Class3(top3, 0, arg1, arg2, path)))

    
    
      
