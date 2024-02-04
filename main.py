from tkinter import *
from tkinter import messagebox

main = Tk()
main.title("Payment UI")
main.configure(bg="#f4f4f4")
main.geometry("500x500")
main.resizable(False, False)

frame = Frame(bg="#f4f4f4")
window2 = Frame(bg="#f4f4f4")
window3= Frame(bg="#f4f4f4")


PASSWORD = "Codetown"
amount_var = StringVar()
card_var = StringVar()
password_var = StringVar()
payment_data = []

def validate_and_process_payment():
    # Retrieve values from Entry widgets
    amount_due = amount_var.get()
    credit_card_number = card_var.get()

    # Validate the entered values
    if not amount_due:
        messagebox.showerror("Error", "Invalid input. Please enter amount")
    elif not credit_card_number.isdigit() or len(credit_card_number) != 16:
             messagebox.showerror("Error:",  "The credit card number must consist of 16 digits without spaces or other characters")    
    else:
        # Record payment details in a list of dictionaries
        payment_data.append({"Amount Due": amount_due, "Credit Card Number": credit_card_number})
        
        # Display a confirmation message
        messagebox.showinfo("Payment Successful", "Thank you for your payment!")
        
        # Reset the main interface to its default state
        amount_var.set("")
        card_var.set("")

def validate_password():

     # Retrieve values from Entry widgets
    password = password_var.get()
   
    if password == PASSWORD:
         open_window_3() 
    else:     
        messagebox.showerror("Error", "")
        print(password)
        print(PASSWORD)
         
def open_window_2(): 
    # ################################# PASSWORD SCREEN #################################
    heading = Label(window2, text="Password Required to Proceed", fg="#000", bg="#f4f4f4", pady=20, font=("", 13))
    heading.grid(row=0, column=0, columnspan=2, sticky="w")

    passwordLabel = Label(window2, text="Enter Your Password", fg="black", bg="#f4f4f4", highlightthickness=0, font=("", 20))
    passwordLabel.grid(row=1, column=0, sticky="w")

    passwordTextField = Entry(window2, show="*", bg="white", fg="black", font=("", 20), textvariable=password_var, highlightbackground="black", highlightcolor="#777", highlightthickness=.5)
    passwordTextField.grid(row=1, column=2, sticky="ew", pady=20)

    divider = Frame(window2, bg="red")
    divider.grid(row=3, column=2, columnspan=2, pady=10)

    submit_btn = Button(window2, text="Submit", border=1, pady=10, padx=30, font=("", 20),command=validate_password)
    submit_btn.grid(row=4, column=2, columnspan=2, sticky="e")

    frame.destroy()
    window3.destroy()

def open_window_3(): 
    # ################################# SUMMARY SCREEN #################################
    heading = Label(window3, text="Summary", fg="#000", bg="#f4f4f4", pady=20, font=("", 13))
    heading.grid(row=0, column=0, columnspan=2, sticky="w")
    
    submit_btn = Button(window3, text="Back to Home", border=1, pady=10, padx=30, font=("", 20),command=open_window_2)
    submit_btn.grid(row=4, column=2, columnspan=2, sticky="e")

    frame.destroy()
    window2.destroy()


# ################################# CARD SCREEN ################################# 
heading = Label(frame, text="Self Check in Payments", fg="#000", bg="#f4f4f4", pady=20, font=("", 13))
heading.grid(row=0, column=0, columnspan=2, sticky="w")

amountLabel = Label(frame, text="Amount Due", fg="black", bg="#f4f4f4", highlightthickness=0, font=("", 20))
amountLabel.grid(row=1, column=0, sticky="w")

cardNoLabel = Label(frame, text="Credit Card Number", fg="black", bg="#f4f4f4", highlightthickness=0, font=("", 20))
cardNoLabel.grid(row=2, column=0, sticky="w")

amountTextField = Entry(frame, bg="white", fg="black", font=("", 20), textvariable=amount_var, highlightbackground="black", highlightcolor="#777", highlightthickness=.5)
amountTextField.grid(row=1, column=2, sticky="ew", pady=20)

cardTextField = Entry(frame, bg="white",  fg="black", font=("", 20), textvariable=card_var,  highlightbackground="black", highlightcolor="#777", highlightthickness=.5)
cardTextField.grid(row=2, column=2, sticky="ew")

divider = Frame(frame, bg="red")
divider.grid(row=3, column=2, columnspan=2, pady=20)

pay_now = Button(frame, text="Pay", border=1, pady=10, padx=30, font=("", 20), command=validate_and_process_payment)
pay_now.grid(row=4, column=2, columnspan=2, sticky="e")

operator_mode_btn = Button(main, text="Operator Mode", border=0, pady=10, padx=30, command=open_window_2)
operator_mode_btn.place(x=0, y=455)


frame.pack()
window2.pack()
window3.pack()
main.mainloop()
