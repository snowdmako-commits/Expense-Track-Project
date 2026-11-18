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

def main():
    while True:
        showMenu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Enter title: ")
                amount = input("Enter amount: ")
                category = input("Enter category: ")

                expense = addExpense(title, amount, category)
                print("Expense added successfully!")
                print(expense)

            elif choice == "2":
                expenses = getAllExpenses()

                if not expenses:
                    print("No expenses found!")
                else:
                    for expense in expenses:
                        print(expense)

            elif choice == "3":
                expenseID = input("Enter expense ID: ")
                title = input("Enter new title: ")
                amount = input("Enter new amount: ")
                category = input("Enter new category: ")

                updateExpense(expenseID, title, amount, category)
                print("Expense updated successfully!")

            elif choice == "4":
                expenseID = input("Enter expense ID: ")
                print(searchExpense(expenseID))

            elif choice == "5":
                expenseID = input("Enter expense ID: ")
                deleteExpense(expenseID)
                print("Expense deleted successfully!")

            elif choice == "6":
                print("Total Expenses:", totalExpenses())

            elif choice == "7":
                for category in CATEGORIES:
                    print(category)

            elif choice == "8":
                print("Exported:", exportToCSV())

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")

        except (ValueError, LookupError) as e:
            print("Error:", e)

main()
