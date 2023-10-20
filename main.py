import serial
import serial.tools.list_ports
import types
import time
import tkinter as tk
from Packages.LabDevice import RND320KA3005
from Packages.RNDCommands import CommandList

def print_selected_item(listboxelement):
    for i in listboxelement.curselection():
        print(listboxelement.get(i))
    return

# dev.AddInstruction("IDN", RNDCommands.IDN)
# dev.IDN = types.MethodType(RNDCommands.IDN, dev)
# setattr(dev, "IDN", RNDCommands.IDN)

test_list = ["asd 1", "asdasd", "gsdgsd"]

if __name__ == "__main__":
    ports = serial.tools.list_ports.comports()

    for port in ports:
        print(port)
        
    serial = serial.Serial(port="COM3", baudrate=9600, timeout=1)

    # data = "ISET1:0.050"
    # check = "ISET1?"
    data = "*IDN?"

    dev = RND320KA3005.RND320KA3005P(serial=serial)
    print(dev.port)
    print(dev.id)
    # greeting = tk.Label(text="Hello, Tkinter")
    # greeting.pack()
    window = tk.Tk()
    window.title("LabTools")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(1, weight=7)
    window.geometry("800x480")
    window.minsize(300, 120)
    
    right_panel = tk.Frame(window, highlightbackground="blue", highlightthickness=2)
    right_panel.rowconfigure(0, weight=1)
    right_panel.grid(column=1, row=0, sticky=(tk.S, tk.W, tk.E, tk.N))
    
    
    
    label_rp = tk.Label(right_panel, text="RP Label")
    label_rp.grid(column=0, row=0, sticky=(tk.N, tk.W))
    
    left_panel = tk.Frame(window, highlightbackground="red", highlightthickness=2)
    left_panel.rowconfigure(0, weight=1)
    left_panel.rowconfigure(1, weight=9)
    left_panel.rowconfigure(2, weight=1)
    left_panel.columnconfigure(0, weight=1)
    left_panel.grid(column=0, row=0, sticky=(tk.S, tk.W, tk.E, tk.N))
    
    left_panel_1 = tk.Frame(left_panel, highlightbackground="cyan", highlightthickness=2)
    left_panel_1.grid(column=0, row=0, sticky=(tk.S, tk.W, tk.E, tk.N))
    label = tk.Label(left_panel_1, text="top")
    label.pack(side="left")
    
    listboxframe = tk.Frame(left_panel, highlightbackground="green", highlightthickness=2)
    listboxframe.columnconfigure(0, weight=1)
    listboxframe.rowconfigure(0, weight=1)
    listboxframe.grid(column=0, row=1, sticky=(tk.S, tk.W, tk.E, tk.N))
    
    var_type = tk.Variable(value=ports)
    dropdown = tk.Listbox(listboxframe, listvariable=var_type, height=8, selectmode=tk.SINGLE)
    dropdown.pack(side="top", fill="both")
    
    left_panel_3 = tk.Frame(left_panel, highlightbackground="yellow", highlightthickness=2)
    left_panel_3.grid(column=0, row=2, sticky=(tk.S, tk.W, tk.E, tk.N))
    bottom_button = tk.Button(left_panel_3, text="Print listbox active", command=lambda: print_selected_item(dropdown))
    bottom_button.pack(side="top")
    window.mainloop()
    