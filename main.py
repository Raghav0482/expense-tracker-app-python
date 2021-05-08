from tkinter import *

main = Tk()
main.title("ExpenseTrackerByRaghav")


# creating label, entry, button
main_title = Label(main, text="                               Expense Tracker")

balance_title = Label(main, text="YOUR BALANCE                                  ")
balance_value = Label(main, text="$150.00                                              ")

income_label = Label(main, text="INCOME         ")
income_value = Label(main, text="$150.00         ")
expense_label = Label(main, text="EXPENSE         ")
expense_value = Label(main, text="$0.00         ")

history_heading = Label(main, text="History                                             ")
history_item1_Label = Label(main, text="Camera         ")
history_item1_Value = Label(main, text="+150")

transaction_heading = Label(main, text="Add new transaction                             ")

transaction_text_label = Label(main, text="Text                                 ")
transaction_text_Value = Entry(main)

transaction_amount_label = Label(main, text="Amount                           ")
transaction_amount_label2 = Label(main, text="                      (negative - expense, positive - income)")
transaction_amount_Value = Entry(main)


labelspace = Label(main, text = " ")
transaction_add_btn = Button(main, text="Add Transaction", width = 25)

# placing them in a grid
main_title.grid(column=0, row=0)

balance_title.grid(column=0, row=1)
balance_value.grid(column=0, row=2)

income_label.grid(column=0, row=3)
income_value.grid(column=0, row=4)

expense_label.grid(column=1, row=3)
expense_value.grid(column=1, row=4)

history_heading.grid(column=0, row=5)
history_item1_Label.grid(column=0, row=6)
history_item1_Value.grid(column=1, row=6)

transaction_heading.grid(column=0, row=7)
transaction_text_label.grid(column=0, row=8)
transaction_text_Value.grid(column=0, row=9)
transaction_amount_label.grid(column=0, row=10)
transaction_amount_label2.grid(column=0, row=11)
transaction_amount_Value.grid(column=0, row=12)
labelspace.grid(column = 0, row = 14)
transaction_add_btn.grid(column=0, row=15, padx = 30, pady = 15)
main.mainloop()