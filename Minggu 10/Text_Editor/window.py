from tkinter import *
from tkinter.messagebox import showerror
from os import path

class Window(Tk):
    #create and configure window
    def __init__(self):
        super().__init__()
        self.software.title("B.A.D TextEditor ~ Untitled")
        imgpath = path.dirname(__file__)
        self.iconphoto(True, PhotoImage(file= imgpath + '/assets/favicon-96.png'))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)
        self.minsize(height=800, width=885)

#vertical scrollbar
class Text_scroll():
    def __init__(self, cursor_type):
        self.bar = Scrollbar(cursor=cursor_type)
        self.grid = self.bar.grid(row=0, column=2, sticky="nsew")

if __name__ == '__main__':
    showerror(title="Warning!", message="Run Main.py")