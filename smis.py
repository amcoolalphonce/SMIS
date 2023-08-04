import tkinter as tk
from tkinter import  ttk

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("University of Nairobi SMI System")

title_label = tk.Label(win , text="University of Nairobi SMI System", font=("Segoe UI", 30, "bold"),border=12., relief=tk.GROOVE, bg="blue", foreground="white")
title_label.pack(side=tk.TOP, fill=tk.X)
detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Segoe UI", 20), bg="grey", foreground="black")
detail_frame.place(x=20, y= 80, width=420, height=620)



win.mainloop()