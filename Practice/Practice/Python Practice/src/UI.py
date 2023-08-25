from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Welcome Choose an Option:").grid(column=1, row=0)
ttk.Button(frm, text="Write").grid(column=1, row=1, pady=25, ipadx=15)
ttk.Button(frm, text="Read").grid(column=1, row=2, pady=5, ipadx=15)
root.mainloop()
 