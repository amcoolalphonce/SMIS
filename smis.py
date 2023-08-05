import tkinter as tk
from tkinter import  ttk

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("University of Nairobi SMI System")
win.config(bg="lightgreen")

title_label = tk.Label(win , text="University of Nairobi SMI System", font=("Segoe UI", 30, "bold"),border=12., relief=tk.GROOVE, bg="blue", foreground="white")
title_label.pack(side=tk.TOP, fill=tk.X)
detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Segoe UI", 20), bg="grey", foreground="black", bd=12, relief=tk.FLAT)
detail_frame.place(x=20, y= 110, width=420, height=560)

data_frame = tk.LabelFrame(win, bd=12, bg="lightgrey", relief=tk.RIDGE)
data_frame.place(x=440, y=110, width=810,height=560)

win.mainloop()