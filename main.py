from tkinter import *
from tkinter import messagebox

main = Tk()
main.title("Payment UI")
main.configure(bg="#f4f4f4")
main.geometry("600x600")
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
        password_var.set("")
    else:     
        messagebox.showerror("Error", "Invalid credentials")

def format_card_number(card_number):
    # Add hyphen after every four characters
    return '-'.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])

def handle_back_home():
    window3.destroy()
    window2.destroy()   
    default_frame()
         

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
    window3.pack_forget()
    window2.pack()

def open_window_3(): 
    # ################################# SUMMARY SCREEN #################################
    heading = Label(window3, text="List of Payment Transactions", fg="#000", bg="#f4f4f4", pady=20, font=("", 13))
    heading.grid(row=0, column=0, sticky="w")

    # Display payment data using a Text widget
    summary_text = Text(window3, fg="#000", bg="#f4f4f4", pady=20, width=300, height=300, border=0, borderwidth=0, font=("", 15, 'bold'), highlightthickness=0, wrap=WORD)
    summary_text.grid(row=2, column=0, padx=10, pady=10)

    if not len(payment_data) > 0:
        summary_text.insert(END, f"No Payments Made yet...")
    else: 
        for payment in payment_data:
            summary_text.insert(END, f"Credit Card N.: {format_card_number(payment['Credit Card Number'])} -  Payment Made: ${payment['Amount Due']}\n\n")

    frame.destroy()
    window2.pack_forget()
    window3.pack()

def default_frame():
    if not hasattr(default_frame, "frame_created"):
        global frame
        frame = Frame(bg="#f4f4f4")

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
        operator_mode_btn.place(x=2, y=555)

        default_frame.frame_created = True
    frame.pack()

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
operator_mode_btn.place(x=2, y=555)

home_btn = Button(main, text="Back to Home", border=0, highlightthickness=0, pady=5, padx=10, font=("", 16), command=handle_back_home)
home_btn.place(x=445, y=2)


frame.pack()

main.mainloop()
