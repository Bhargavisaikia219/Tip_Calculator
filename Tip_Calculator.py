from tkinter import *

class TipCal():
    def __init__(self):
        window =  Tk()
        window.title("Tip Calculator")
        window.geometry("380x300")
        window.resizable(width=False, height= False)
        window.configure(background="SteelBlue4")

        tip_percentage=Label(window, text="Tip Percentages", bg="yellow", fg="black", width=15)
        tip_percentage.grid(row=0, column=0, padx=14, pady=14)

        bill_amount=Label(window, text="Bill_amount", bg="cyan2", fg="black", width=15)
        bill_amount.grid(row=0, column=1, padx=10)

        self.mealcost=StringVar()
        bill_amount_entry=Entry(window, textvariable=self.mealcost, width=14)
        bill_amount_entry.grid(row=0, column=3, padx=7)

        window.mainloop()


TipCal()