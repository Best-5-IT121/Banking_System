try:
    with open("balance.txt", "r") as file:
        balance = float(file.read())
except:
    balance = 0
    with open("balance.txt", "w") as file:
        file.write(str(balance))


def deposit():
    global balance
    amount = entry.get()

    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Error", "Invalid amount")
            return

        balance += amount
        update_balance()
        save_transaction(f"Deposited: {amount}")
        messagebox.showinfo("Success", "Deposit successful")
    except:
        messagebox.showerror("Error", "Enter numbers only")


def withdraw():
    global balance
    amount = entry.get()

    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Error", "Invalid amount")
            return
        if amount > balance:
            messagebox.showerror("Error", "Insufficient balance")
            return

        balance -= amount
        update_balance()
        save_transaction(f"Withdrawn: {amount}")
        messagebox.showinfo("Success", "Withdrawal successful")
    except:
        messagebox.showerror("Error", "Enter numbers only")


def show_transactions():
    try:
        with open(TRANSACTION_FILE, "r") as f:
            transactions = f.read()

        if transactions.strip() == "":
            transactions = "No transactions yet."

        history_window = tk.Toplevel(root)
        history_window.title("Transaction History")
        history_window.geometry("600x400")

        text_area = tk.Text(history_window, font=("Arial", 11))
        text_area.pack(fill="both", expand=True)

        text_area.insert("1.0", transactions)
        text_area.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def reset_account():
    confirm = messagebox.askyesno(
        "Confirm Reset",
        "Are you sure you want to reset the account?"
    )

    if confirm:
        save_balance(0)

        with open(TRANSACTION_FILE, "w") as f:
            pass

        update_balance_label()

        messagebox.showinfo("Reset", "Account has been reset.")

initialize_files()

root = tk.Tk()
root.title("GUI Banking System")
root.geometry("500x450")
root.resizable(False, False)

# TITLE
title_label = tk.Label(
    root,
    text="BANKING SYSTEM",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

# BALANCE LABEL
balance_label = tk.Label(
    root,
    text="Current Balance: ₱0.00",
    font=("Arial", 16)
)
balance_label.pack(pady=10)

update_balance_label()

# BUTTONS
deposit_button = tk.Button(
    root,
    text="Deposit Money",
    font=("Arial", 14),
    width=20,
    command=deposit_money
)
deposit_button.pack(pady=10)

withdraw_button = tk.Button(
    root,
    text="Withdraw Money",
    font=("Arial", 14),
    width=20,
    command=withdraw_money
)
withdraw_button.pack(pady=10)

history_button = tk.Button(
    root,
    text="Transaction History",
    font=("Arial", 14),
    width=20,
    command=show_transactions
)
history_button.pack(pady=10)

reset_button = tk.Button(
    root,
    text="Reset Account",
    font=("Arial", 14),
    width=20,
    command=reset_account
)
reset_button.pack(pady=10)

exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 14),
    width=20,
    command=root.destroy
)
exit_button.pack(pady=10)

# FOOTER
footer_label = tk.Label(
    root,
    text="Tkinter GUI Banking System Project",
    font=("Arial", 10)
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()

