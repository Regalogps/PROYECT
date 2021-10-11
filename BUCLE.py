
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
               lambda top1: Class1(top1, 1, arg1, arg2, path),
               lambda top2: Class2(top2, 1, arg1, arg2, path),
               lambda top3: Class3(top3, 1, arg1, arg2, path)))

    lst[2].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 2, arg1, arg2, path),
               lambda top2: Class2(top2, 2, arg1, arg2, path),
               lambda top3: Class3(top3, 2, arg1, arg2, path)))

    lst[3].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 3, arg1, arg2, path),
               lambda top2: Class2(top2, 3, arg1, arg2, path),
               lambda top3: Class3(top3, 3, arg1, arg2, path)))

    lst[4].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 4, arg1, arg2, path),
               lambda top2: Class2(top2, 4, arg1, arg2, path),
               lambda top3: Class3(top3, 4, arg1, arg2, path)))

    lst[5].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 5, arg1, arg2, path),
               lambda top2: Class2(top2, 5, arg1, arg2, path),
               lambda top3: Class3(top3, 5, arg1, arg2, path)))

    lst[6].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 6, arg1, arg2, path),
               lambda top2: Class2(top2, 6, arg1, arg2, path),
               lambda top3: Class3(top3, 6, arg1, arg2, path)))

    lst[7].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 7, arg1, arg2, path),
               lambda top2: Class2(top2, 7, arg1, arg2, path),
               lambda top3: Class3(top3, 7, arg1, arg2, path)))

    lst[8].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 8, arg1, arg2, path),
               lambda top2: Class2(top2, 8, arg1, arg2, path),
               lambda top3: Class3(top3, 8, arg1, arg2, path)))

    lst[9].config(command=lambda: self.windows(
               lambda top1: Class1(top1, 9, arg1, arg2, path),
               lambda top2: Class2(top2, 9, arg1, arg2, path),
               lambda top3: Class3(top3, 9, arg1, arg2, path)))

   
    
      
