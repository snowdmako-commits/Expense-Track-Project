import uuid
from datetime import date
from storage import *
from validation import *
from exceptions import expensesNotFound

def addExpense(title, amount, category):
    expenses = loadExpenses()

    expense = {
        "id": str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmount(amount),
        "category": validateCategory(category),
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    saveExpenses(expenses)

    return expense