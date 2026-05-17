import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Banking System")
root.geometry("500x500")


title_label = tk.Label(root, text="Simple Banking System",
                       font=("Arial", 18, "bold"))
title_label.pack(pady=10)

balance_label = tk.Label(root, text="Balance: ₱0.00",
                         font=("Arial", 14))
balance_label.pack(pady=10)


amount_entry = tk.Entry(root, font=("Arial", 14))
amount_entry.pack(pady=10)


deposit_button = tk.Button(root, text="Deposit",
                           font=("Arial", 12),
                           width=15)

deposit_button.pack(pady=5)

withdraw_button = tk.Button(root, text="Withdraw",
                            font=("Arial", 12),
                            width=15)

withdraw_button.pack(pady=5)

history_button = tk.Button(root, text="Show History",
                           font=("Arial", 12),
                           width=15)

history_button.pack(pady=5)