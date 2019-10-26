from os import name
import tkinter as tk
import controller

class View:
    def __init__(self, master):
        self.board_labels = []
        for x in range(3):
            line = []
            master.grid_columnconfigure(x, minsize=150)
            for y in range(3):
                master.grid_rowconfigure(y, minsize=150)
                font_size = 120
                if name == 'nt':
                    font_size = 90
                l = tk.Label(master, text='_', font=('Helvetica', font_size),
                             padx=5, pady=5)
                l.grid(column=x, row=y)
                line.append(l)
            self.board_labels.append(line)
