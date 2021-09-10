            elif self.toplevel_RIGHT.winfo_ismapped() == 0:
                self.toplevel_LEFT.deiconify()   
                self.toplevel_RIGHT.deiconify()
                self.toplevel_STUF.deiconify()
                print('bbb')

            elif self.toplevel_STUF.winfo_ismapped() == 0:
                self.toplevel_LEFT.deiconify()   
                self.toplevel_RIGHT.deiconify()
                self.toplevel_STUF.deiconify()
                print('ccc')

            elif self.toplevel_LEFT.winfo_ismapped() == 0 and self.toplevel_RIGHT.winfo_ismapped() == 0:
                self.toplevel_LEFT.deiconify()   
                self.toplevel_RIGHT.deiconify()
                self.toplevel_STUF.deiconify()
                print('a y b')

            elif self.toplevel_LEFT.winfo_ismapped() == 0 and self.toplevel_STUF.winfo_ismapped() == 0:
                self.toplevel_LEFT.deiconify()   
                self.toplevel_RIGHT.deiconify()
                self.toplevel_STUF.deiconify()
                print('a y c')
            
            elif self.toplevel_RIGHT.winfo_ismapped() == 0 and self.toplevel_STUF.winfo_ismapped() == 0:
                self.toplevel_LEFT.deiconify()   
                self.toplevel_RIGHT.deiconify()
                self.toplevel_STUF.deiconify()
                print('b y c')