from tkinter import *

class TipCal():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator")
        window.geometry("380x300")
        window.resizable(width = False, height = False)
        window.configure(background = "SteelBlue4")

        tip_percentage_lbl = Label(window, text = "Tip Percentages", bg = "yellow", fg = "black", width = 15)
        tip_percentage_lbl.grid(row = 0, column = 0, padx = 14, pady = 14)

        bill_amount_lbl = Label(window, text = "Bill Amount", bg = "cyan2", fg = "black", width = 15)
        bill_amount_lbl.grid(row = 0, column = 1, padx = 10)

        self.mealcost = StringVar()
        bill_amount_entry = Entry(window, textvariable = self.mealcost, width = 14)
        bill_amount_entry.grid(row = 0, column = 2, padx = 7)

        self.tippercent = IntVar()
        five_percent = Radiobutton(window, text = "5%", variable = self.tippercent, value = 5 )
        five_percent.grid(row = 1, column = 0)

        ten_percent = Radiobutton(window, text = "10%", variable = self.tippercent, value = 10)
        ten_percent.grid(row = 2, column = 0)

        fifteen_percent = Radiobutton(window, text = "15%", variable = self.tippercent, value = 15)
        fifteen_percent.grid(row = 3, column = 0)

        tweny_percent = Radiobutton(window, text = "20%", variable = self.tippercent, value = 20)
        tweny_percent.grid(row = 4, column = 0)

        twentyfive_percent = Radiobutton(window, text = "25%", variable = self.tippercent, value = 25)
        twentyfive_percent.grid(row = 5, column = 0)

        thirty_percent = Radiobutton(window, text = "30%", variable = self.tippercent, value = 30)
        thirty_percent.grid(row = 6, column = 0)

        tip_amount_lbl = Label(window, text="Tip Amount", bg = "wheat1", fg = "black", width = 15)
        tip_amount_lbl.grid(row = 2, column = 1, padx = 10 )

        self.tipamount = StringVar()
        tip_amount_entry = Entry(window, textvariable=self.tipamount, width=14)
        tip_amount_entry.grid(row = 2, column = 2, padx = 7)

        bill_total_lbl = Label(window, text = "Bill Total", bg = "IndianRed1", fg = "black", width = 15)
        bill_total_lbl.grid(row = 5, column = 1, padx = 7 )

        self.billtotal = StringVar()
        bill_total_entry = Entry(window, textvariable = self.billtotal, width = 14)
        bill_total_entry.grid(row = 5, column = 2, padx = 7)

        calculate_button = Button(window, text = "Calculate", bg = "grey36", fg = "black", width = 10, command = "")
        calculate_button.grid(row = 7, column = 1, padx = 15, pady = 10)

        clear_button = Button(window, text = "Clear", bg = "thistle", fg = "black", width = 10, command = "")
        clear_button.grid(row = 7, column = 2, padx = 15, pady = 10)


        window.mainloop()

TipCal()