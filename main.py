from tkinter import *

main = Tk()
main.title("ExpenseTrackerByRaghav")
main.geometry("400x450")

# mainlabel
main_title = Label(main, text="Expense Tracker")
main_title.grid(column=0, row=0, padx = 20)

balance_title = Label(main, text="YOUR BALANCE")
balance_value = Label(main, text="$150.00")
balance_title.grid(column=0, row=1, padx= 10)
balance_value.grid(column=0, row=2)

income_label = Label(main, text="INCOME")
income_value = Label(main, text="$150.00")
expense_label = Label(main, text="EXPENSE")
expense_value = Label(main, text="$0.00")
income_label.grid(column=0, row=3, pady=(10,0))
income_value.grid(column=0, row=4)
expense_label.grid(column=1, row=3, pady=(10,0))
expense_value.grid(column=1, row=4)


history_heading = Label(main, text="History", font='bold, 15')
history_heading.grid(column=0, row=5, pady = (10,0))
history = Listbox(main, height =15)
history.grid(row = 6, column = 0, columnspan = 3, rowspan = 5)


transaction_heading = Label(main, text="Add new transaction", font='bold, 15')
transaction_text_label = Label(main, text="Text")
transaction_text_Value = Entry(main)

transaction_amount_label = Label(main, text="Amount")
transaction_amount_label2 = Label(main, text="(negative - expense, positive - income)")
transaction_amount_Value = Entry(main)


# labelspace = Label(main, text = " ")
# transaction_add_btn = Button(main, text="Add Transaction", width = 25)

# # placing them in a grid








transaction_heading.grid(column=3, row=1)
transaction_text_label.grid(column=3, row=2)
transaction_text_Value.grid(column=3, row=3)
transaction_amount_label.grid(column=3, row=4)
transaction_amount_label2.grid(column=3, row=5)
transaction_amount_Value.grid(column=3, row=6)
# labelspace.grid(column = 0, row = 14)
# transaction_add_btn.grid(column=0, row=15, padx = 30, pady = 15)



main.mainloop()
