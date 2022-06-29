from pathlib import Path
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from types import NoneType
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("B.A.D Text Editor")
window.geometry("800x650")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

class Button_act():
    # Constructor
    def __init__(self, root, txt_edit):
        self.__filename = None
        self.__txt_edit = txt_edit
        self.__root = root

    # New File Method
    def new_file(self):
        self.__filename = None
        self.__text.delete(1.0, END)
        self.__root.title("B.A.D TextEditor ~ Untitled")

    def open_file(self, *args):
        try:
            filepath = askopenfilename(
                defaultextension="txt",
                filetypes=[("Text Files", ".txt"), 
                ("All Files", ".*")],
            )
            with open(filepath, "r") as input_file:
                text = input_file.read()
            self.txt_edit.delete(1.0, END)
            self.txt_edit.insert(1.0, text)
            window.title(f"B.A.D TextEditor ~ {filepath}")
        except FileNotFoundError:
            print("No file exists")

    def save_file(self, *args):
        try:
            filepath = asksaveasfilename(
                defaultextension="txt",
                filetypes=[("Text Files", ".txt"),
                ("All Files", ".*")],
            )
            with open(filepath, "w") as output_file:
                text = self.txt_edit.get(1.0, END)
                output_file.write(text)
            window.title(f"B.A.D TextEditor ~ {filepath}")
        except FileNotFoundError:
            print("No file exists")

canvas.place(x = 0, y = 0)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=100.0,
    y=0.0,
    width=800.0,
    height=800.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    100.24652099609375,
    800.03076171875,
    fill="#C2C1D4",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("new_file.png"))
new_file = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Button_act.new_file(self),
    relief="flat"
)
new_file.place(
    x=10.0,
    y=13.0,
    width=80.0,
    height=45.0
)

open_image = PhotoImage(
    file=relative_to_assets("open.png"))
open = Button(
    image=open_image,
    borderwidth=0,
    highlightthickness=0,
    command=Button_act.open_file(self),
    relief="flat"
)
open.place(
    x=10.0,
    y=78.0,
    width=80.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("save_as.png"))
save_as = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Button_act.save_file(self),
    relief="flat"
)
save_as.place(
    x=10.0,
    y=143.0,
    width=80.0,
    height=45.0
)
window.resizable(True, True)
window.mainloop()
