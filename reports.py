import csv
from expenses import getAllExpenses

def totalExpenses():
    expenses = getAllExpenses()
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

def exportToCSV():
    expenses = getAllExpenses()
    filePath = "data/expenses.csv"

    fieldnames = ["id", "title", "amount", "category", "date"]

    with open(filePath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)

        return filePath
