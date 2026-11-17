from expenses import *
from validation import CATEGORIES
from reports import *

def showMenu():
    print("=" * 40)
    print("           EXPENSE TRACKER")
    print("=" * 40)
    print("""
        1. Add Expense
        2. Show All Expenses
        3. Edit Expense
        4. Search Expense
        5. Delete Expense
        6. Show Total Expenses
        7. Show Categories
        8. Export to CSV

        0. Exit
    """)
    print("=" * 40)