import tkinter as tk
from tkinter import ttk

class SimpleBankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Bank - PH Peso Edition")
        self.root.geometry("550x550")

        self.lbl_balance = tk.Label(
            root,
            text="Balance: ₱0.00",
            font=("Arial", 20, "bold"),
            fg="green"
        )
        self.lbl_balance.pack(pady=15)

        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)

        tk.Label(
            frame_input,
            text="Amount: ₱",
            font=("Arial", 12)
        ).grid(row=0, column=0)

        self.ent_amount = tk.Entry(
            frame_input,
            font=("Arial", 12),
            width=15
        )
        self.ent_amount.grid(row=0, column=1, padx=5)

        frame_btns = tk.Frame(root)
        frame_btns.pack(pady=10)

        tk.Button(
            frame_btns,
            text="Deposit",
            width=10
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_btns,
            text="Withdraw",
            width=10
        ).pack(side=tk.RIGHT, padx=5)

        self.table = ttk.Treeview(
            root,
            columns=("DateTime", "Action", "Amount", "Balance"),
            show="headings",
            height=10
        )

        self.table.heading("DateTime", text="Date & Time")
        self.table.heading("Action", text="Action")
        self.table.heading("Amount", text="Amount")
        self.table.heading("Balance", text="Available Balance")

        self.table.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        import os
from tkinter import messagebox

BALANCE_FILE = "balance.txt"
HISTORY_FILE = "history.txt"

def load_balance_from_file():
    try:
        if os.path.exists(BALANCE_FILE):
            with open(BALANCE_FILE, "r", encoding="utf-8") as f:
                return float(f.read().strip())
    except Exception:
        pass

    return 0.0

def clear_history():
    if not os.path.exists(HISTORY_FILE):
        messagebox.showinfo("Info", "History is already empty.")
        return

    confirm = messagebox.askyesno(
        "Confirm",
        "Delete all transaction history?"
    )

    if confirm:
        try:
            os.remove(HISTORY_FILE)
            messagebox.showinfo("Success", "History cleared.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

            from datetime import datetime
from tkinter import messagebox

def save_data_to_files(balance, action, amount):
    try:
        with open("balance.txt", "w", encoding="utf-8") as f:
            f.write(f"{balance:.2f}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{timestamp},{action},₱{amount:.2f},₱{balance:.2f}\n"
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))

def refresh_table_display(table):
    for row in table.get_children():
        table.delete(row)

    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

            for line in reversed(lines):
                parts = line.strip().split(",")

                if len(parts) == 4:
                    table.insert("", "end", values=parts)

    except:
        pass