import json
from datetime import datetime

# Load expenses
try:
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
except:
    expenses = []

def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)
    save_expenses()
    print(f"Added: {category} - ₹{amount}")

def save_expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def show_total():
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: ₹{total}")

def show_by_category():
    categories = {}
    for e in expenses:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]
    for cat, total in categories.items():
        print(f"{cat}: ₹{total}")

# Main program
while True:
    print("\n1. Add expense\n2. Show total\n3. Show by category\n4. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category (Food/Transport/Other): ")
        desc = input("Description: ")
        add_expense(amount, category, desc)
    elif choice == "2":
        show_total()
    elif choice == "3":
        show_by_category()
    elif choice == "4":
        break
