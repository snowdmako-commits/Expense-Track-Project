# 💰 Expense Tracker (CLI)

A clean, modular, and robust command-line interface (CLI) application built with Python to efficiently manage, track, and analyze your personal daily expenses. 

---

## 🚀 Key Features

- **Add Expense:** Easily record new expenses by providing a title, amount, and category. Automatically assigns a unique short UUID and timestamp.
- **View All Expenses:** Display a complete history of all recorded expenses stored in the system.
- **Edit Expense:** Update existing expense details (title, amount, or category) by referencing its unique ID.
- **Search Expense:** Quickly look up specific expense records using their unique ID.
- **Delete Expense:** Remove unwanted or incorrect expense entries from the system.
- **Total Expenses Report:** Instantly calculate and display the total sum of all recorded expenses.
- **Category Management:** View the list of all allowed and predefined expense categories.
- **CSV Export:** Export your entire expense ledger into a structured CSV file for external analysis or backup.
- **Persistent Storage:** Automatically saves and loads all data locally using JSON format.

---

## 🛠️ Project Structure

The project follows a clean, modular Python architecture, separating business logic, validation, storage, and reporting:

```text
ExpenseTracker/
│
├── data/
│   ├── expenses.json     # Local JSON database for storing expenses
│   └── expenses.csv      # Exported CSV report file
│
├── main.py               # Main CLI controller and interactive user menu
├── expenses.py           # Core business logic (add, search, update, delete)
├── storage.py            # File handling operations (JSON read/write)
├── validation.py         # Input validation rules for title, amount, and category
├── reports.py            # Summary calculations and CSV export functions
└── exceptions.py         # Custom exception definitions (ValueError, LookupError)

!!! WARNING !!!
run code after u type "mkdir data" on Terminal in python
