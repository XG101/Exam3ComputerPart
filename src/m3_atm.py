import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 6. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("ATM")

frm_a = tk.Frame(master=window)
frm_a.columnconfigure([0, 1, 2], weight=1, minsize=75)
frm_a.rowconfigure([0, 1, 2, 3], weight=1, minsize=75)

def handler_type(event):
    if event.char.isdigit():
        lbl_number['text'] = lbl_number['text'] + event.char
        
def handler_0():
    lbl_number['text'] = lbl_number['text'] + "0"

def handler_1():
    lbl_number['text'] = lbl_number['text'] + "1"

def handler_2():
    lbl_number['text'] = lbl_number['text'] + "2"

def handler_3():
    lbl_number['text'] = lbl_number['text'] + "3"

def handler_4():
    lbl_number['text'] = lbl_number['text'] + "4"

def handler_5():
    lbl_number['text'] = lbl_number['text'] + "5"

def handler_6():
    lbl_number['text'] = lbl_number['text'] + "6"

def handler_7():
    lbl_number['text'] = lbl_number['text'] + "7"

def handler_8():
    lbl_number['text'] = lbl_number['text'] + "8"

def handler_9():
    lbl_number['text'] = lbl_number['text'] + "9"

def handler_deposit():
    lbl_number['text'] = float(lbl_number['text'])
    lbl_current_number['text'] = float(lbl_current_number['text'])
    lbl_current_number['text'] = lbl_current_number['text'] + lbl_number['text']
    lbl_number['text'] = str(lbl_number['text'])
    lbl_current_number['text'] = str(lbl_current_number['text'])
    lbl_number['text'] = ""

def handler_withdraw():
    lbl_number['text'] = float(lbl_number['text'])
    lbl_current_number['text'] = float(lbl_current_number['text'])
    lbl_current_number['text'] = lbl_current_number['text'] - lbl_number['text']
    lbl_number['text'] = str(lbl_number['text'])
    lbl_current_number['text'] = str(lbl_current_number['text'])
    lbl_number['text'] = ""

lbl_current = tk.Label(master=window, text="Current Balence ($):")
lbl_current.pack()
lbl_current_number = tk.Label(master=window, text="1000")
lbl_current_number.pack()
lbl_user_amount = tk.Label(master=window, text="Amount ($):")
lbl_user_amount.pack()
lbl_number = tk.Label(master=window, text="")
lbl_number.pack()
frm_a.pack()

btn_0 = tk.Button(master=frm_a, text="0", fg="black", command=handler_0)
btn_1 = tk.Button(master=frm_a, text="1", fg="black", command=handler_1)
btn_2 = tk.Button(master=frm_a, text="2", fg="black", command=handler_2)
btn_3 = tk.Button(master=frm_a, text="3", fg="black", command=handler_3)
btn_4 = tk.Button(master=frm_a, text="4", fg="black", command=handler_4)
btn_5 = tk.Button(master=frm_a, text="5", fg="black", command=handler_5)
btn_6 = tk.Button(master=frm_a, text="6", fg="black", command=handler_6)
btn_7 = tk.Button(master=frm_a, text="7", fg="black", command=handler_7)
btn_8 = tk.Button(master=frm_a, text="8", fg="black", command=handler_8)
btn_9 = tk.Button(master=frm_a, text="9", fg="black", command=handler_9)
btn_withdraw = tk.Button(master=frm_a, text="Withdraw", fg="black", command=handler_withdraw)
btn_deposit = tk.Button(master=frm_a, text="Deposit", fg="black", command=handler_deposit)


btn_1.grid(row=0, column=0, sticky="nsew")
btn_2.grid(row=0, column=1, sticky="nsew")
btn_3.grid(row=0, column=2, sticky="nsew")
btn_4.grid(row=1, column=0, sticky="nsew")
btn_5.grid(row=1, column=1, sticky="nsew")
btn_6.grid(row=1, column=2, sticky="nsew")
btn_7.grid(row=2, column=0, sticky="nsew")
btn_8.grid(row=2, column=1, sticky="nsew")
btn_9.grid(row=2, column=2, sticky="nsew")
btn_0.grid(row=3, column=1, sticky="nsew")
btn_withdraw.grid(row=3, column=0, sticky="nsew")
btn_deposit.grid(row=3, column=2, sticky="nsew")

window.bind("<Key>", handler_type)
    
window.mainloop()
