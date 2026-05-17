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
        