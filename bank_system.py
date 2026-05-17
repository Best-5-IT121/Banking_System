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