# Import tkinter
from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("400x400")

# Creates variables for prices
soccer = 40
movie = 75
theater = 100

# Creates Tkinter widgets
variable_type= StringVar()
numb = Entry(window, width=20)
choices = ttk.Combobox(window, textvariable=variable_type, width=20, value=["Soccer", "Movie", "Theater"])
reason_price = ttk.Spinbox(window, from_=0, to=20, state="readonly")
cell_number = Label(window, text="Cellphone number:")

ticket_cat = Label(window, text="Ticket Category:")

numbers_ticket = Label(window, text="Number of tickets:")

ans_lb = Label(window)


#Creates class
class clsTiketSales:
    def __init__(self, celno, nrtkts, price):
         self.celno = celno
         self.nrtkts = nrtkts
         self.price = price
         return

# Creates function for button
def cal():
    ticket_sale = clsTiketSales(numb.get(), float(reason_price.get()), choices.get())

    if choices.get() == "Soccer":
        scprice = soccer * int(reason_price.get()) + (14/100)
        ans_lb.config(text="Price:" + str(scprice) + "\n" + "tickets:"+str(reason_price.get()) + "\n" +"Number:"+ str(numb.get()))

    if choices.get() == "Movie":
        mvprice = movie * int(reason_price.get()) + (14/100)
        ans_lb.config(text="Price:"+ str(mvprice) + "\n" + "tickets:"+str(reason_price.get()) + "\n" +"Number:"+ str(numb.get()))

    if choices.get() == "Theater":
        thprice = theater * int(reason_price.get()) + (14/100)
        ans_lb.config(text="Price:"+ str(thprice) + "\n" + "tickets:"+str(reason_price.get()) + "\n" +"Number:"+ str(numb.get()))

#Creates button
btn = Button(window, text="calculate", command=cal, width=20, height=1)

# Adds widgets
cell_number.grid(row=0, column=0, sticky=W)
ticket_cat.grid(row=1, column=0, sticky=W)
numbers_ticket.grid(row=2, column=0, sticky=W)
numb.grid(row = 0, column=1)
choices.grid(row=1, column=1)
reason_price.grid(row=2, column=1)
ans_lb.grid(row=4, column=0)
btn.grid(row=5, column=0)


window.mainloop()
