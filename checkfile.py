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

