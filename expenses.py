import uuid
from datetime import date
from storage import saveExpenses , loadExpenses
from validation import validateTitle , validateAmount , validateCategory
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

def getAllExpenses():
    return loadExpenses()

def searchExpense(expenseID):
    expenses = loadExpenses()

    for expense in expenses:
        if expense["id"] == expenseID:
            return expense

    raise expensesNotFound("Expense not found!")

def updateExpense(expenseID, title, amount, category):
    expenses = loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            e["title"] = validateTitle(title)
            e["amount"] = validateAmount(amount)
            e["category"] = validateCategory(category)

            saveExpenses(expenses)
            return e

    raise expensesNotFound("Expense not found!")

def deleteExpense(expenseID):
    expenses = loadExpenses()
    
     
    found = False
    for expense in expenses:                     # silende silinmedi deye foundla yazdim alindi
        if expense["id"] == expenseID:
            expenses.remove(expense)
            found = True
            break  

    if found:
        saveExpenses(expenses)  
        return True
    else:
        raise expensesNotFound("Expense not found!")