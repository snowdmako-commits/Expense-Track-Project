from exceptions import invalidExpense

CATEGORIES = [
    "Food",
    "Shopping",
    "Education",
    "Health",
    "Entertainment",
    "Other"
]

def validateTitle(title):
    title = title.strip()

    if not title:
        invalidExpense("Title cannot be empty!")

    return title

