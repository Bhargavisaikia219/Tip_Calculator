from tkinter import *

class TipCal():
    def __init__(self):
        window =  Tk()
        window.title("Tip Calculator")
        window.geometry("380x300")
        window.resizable(width=False, height= False)
        window.configure(background="light blue")
        window.mainloop()

TipCal()