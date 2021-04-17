from tkinter import *

#defining a class
class TipCal():

    #init method or constructor
    def __init__(self):
        window = Tk()                                         #create a new window and assign it to the variable 'window'
        window.title("Tip Calculator")                        #sets the title of the window
        window.geometry("380x300")                            #creating fixed geometry of the tkinter window
        window.resizable(width = False, height = False)       #freezes the window width and height
        window.configure(background = "SteelBlue4")           #sets the background of tkinter window

        #to create a textbox named Tip Percentages
        tip_percentage_lbl = Label(window, text = "Tip Percentages", bg = "yellow", fg = "black", width = 15)
        tip_percentage_lbl.grid(row = 0, column = 0, padx = 14, pady = 14)

        #to create a textbox named Bill Amount
        bill_amount_lbl = Label(window, text = "Bill Amount", bg = "cyan2", fg = "black", width = 15)
        bill_amount_lbl.grid(row = 0, column = 1, padx = 10)

        #to create a textbox to enter the meal cost or bill amount
        self.mealcost = StringVar()     #holds a string; default value ""
        bill_amount_entry = Entry(window, textvariable = self.mealcost, width = 14)
        bill_amount_entry.grid(row = 0, column = 2, padx = 7)

        self.tippercent = IntVar()      #holds an integer; default value 0

        #creating option list for tip using Radiobutton
        five_percent = Radiobutton(window, text = "5%", variable = self.tippercent, value = 5 )             #for five percent tip
        five_percent.grid(row = 1, column = 0)

        ten_percent = Radiobutton(window, text = "10%", variable = self.tippercent, value = 10)             #for ten percent tip
        ten_percent.grid(row = 2, column = 0)

        fifteen_percent = Radiobutton(window, text = "15%", variable = self.tippercent, value = 15)         #for fifteen percent tip
        fifteen_percent.grid(row = 3, column = 0)

        tweny_percent = Radiobutton(window, text = "20%", variable = self.tippercent, value = 20)           #for twenty percent tip
        tweny_percent.grid(row = 4, column = 0)

        twentyfive_percent = Radiobutton(window, text = "25%", variable = self.tippercent, value = 25)      #for twenty-five percent tip
        twentyfive_percent.grid(row = 5, column = 0)

        thirty_percent = Radiobutton(window, text = "30%", variable = self.tippercent, value = 30)          #for thirty percent tip
        thirty_percent.grid(row = 6, column = 0)

        tip_amount_lbl = Label(window, text="Tip Amount", bg = "wheat1", fg = "black", width = 15)
        tip_amount_lbl.grid(row = 2, column = 1, padx = 10 )

        #to create a textbox to display the  tip amount after calculating the tip percent and bill amount
        self.tipamount = StringVar()
        tip_amount_entry = Entry(window, textvariable=self.tipamount, width=14)
        tip_amount_entry.grid(row = 2, column = 2, padx = 7)

        #to create a textbox named Bill Total
        bill_total_lbl = Label(window, text = "Bill Total", bg = "IndianRed1", fg = "black", width = 15)
        bill_total_lbl.grid(row = 5, column = 1, padx = 7 )

        #to create a textbox to display the meal cost or bill amount
        self.billtotal = StringVar()
        bill_total_entry = Entry(window, textvariable = self.billtotal, width = 14)
        bill_total_entry.grid(row = 5, column = 2, padx = 7)

        #to add calculate and clear button
        calculate_button = Button(window, text = "Calculate", bg = "grey36", fg = "black", width = 10, command = self.calculate)     #command calls calculate function
        calculate_button.grid(row = 7, column = 1, padx = 15, pady = 10)

        clear_button = Button(window, text = "Clear", bg = "thistle", fg = "black", width = 10, command = self.clear)                #clear calls calculate function
        clear_button.grid(row = 7, column = 2, padx = 15, pady = 10)

        #runs the application
        window.mainloop()

    #declaring funciton for Calculate button
    def calculate(self):
        meal_cost = float(self.mealcost.get())          #get the bill amount entered by the user
        percentage = self.tippercent.get() / 100        #get the tip percentage selected by the user
        tip_amount_entry = meal_cost * percentage       #calculating tip
        self.tipamount.set(tip_amount_entry)            #seting the calculated tip to the desired entry field

        final_bill = meal_cost + tip_amount_entry       #calculating total bill
        self.billtotal.set(final_bill)

    #declaring funciton for Clear button to clear all the fields
    def clear(self):
         self.billtotal.set("")        #sets an empty string
         self.mealcost.set("")
         self.tipamount.set("")

#calling the class which also contain mainloop() that runs the application until you exit
TipCal()