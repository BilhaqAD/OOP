import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

software = tk.Tk()
software.title("B.A.D TextEditor")
software.rowconfigure(0, minsize=800, weight=1)
software.columnconfigure(1, minsize=800, weight=1)

def Scroll_Bar():
    # Vertical Scrollbar
    global scroll_h, scroll_v
    scroll_v = tk.Scrollbar(software, orient=tk.VERTICAL)
    scroll_v.grid(row=0, column=2, sticky="nsew")
    
    # Horizontal Scrollbar
    scroll_h = tk.Scrollbar(software, orient=tk.HORIZONTAL)
    scroll_h.grid(row=1, column=1, sticky="nsew")
    
def config():
    scroll_v.config(command=txt_edit.yview)
    scroll_h.config(command=txt_edit.xview)

Scroll_Bar()
txt_edit = tk.Text(software, yscrollcommand = scroll_v.set, xscrollcommand= scroll_h.set)
config()
software.minsize(height=800, width=0)

# Create class Button_act
class Button_act():
    def new_file():
        txt_edit.delete(1.0, tk.END)
        software.title("B.A.D TextEditor ~ Untitled")

    def open_file():
        try:
            filepath = askopenfilename(
                defaultextension="txt",
                filetypes=[("Text Files", ".txt"), 
                ("All Files", ".*")],
            )
            with open(filepath, "r") as input_file:
                text = input_file.read()
            txt_edit.delete(1.0, tk.END)
            txt_edit.insert(1.0, text)
            software.title("B.A.D TextEditor ~ {}".format(filepath))
        except FileNotFoundError:
            print("No file exists")

    def save_as():
        try:
            filepath = asksaveasfilename(
                defaultextension="txt",
                filetypes=[("Text Files", ".txt"), 
                ("All Files", ".*")],
            )
            with open(filepath, "w") as output_file:
                text = txt_edit.get(1.0, tk.END)
                output_file.write(text)
            software.title("B.A.D TextEditor ~ {}".format(filepath))
        except FileNotFoundError:
            print("No file exists")

    
def Create_button():
    # Frame
    fr_buttons = tk.Frame(software, relief=tk.RAISED, bd=2, bg="#C2C1D4")
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    # Create Buttons
    btn_new = tk.Button(fr_buttons, text="New", command=Button_act.new_file)
    btn_open = tk.Button(fr_buttons, text="Open", command=Button_act.open_file)
    btn_save = tk.Button(fr_buttons, text="Save As", command=Button_act.save_as)

    # Grid Buttons
    btn_new.grid(row = 0, column = 0, sticky="ew", padx = 7, pady = 7)
    btn_open.grid(row = 1, column = 0, sticky="ew", padx = 7)
    btn_save.grid(row = 2, column = 0, sticky="ew", padx = 7, pady = 7)
 

# Object Button_act
Create_button()
software.resizable(True, True)
software.mainloop()

