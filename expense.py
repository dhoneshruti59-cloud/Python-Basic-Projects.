expenses = []
budget = float(input("Enter Monthly Budget: "))

def add_expense():
    description = input("Enter Description: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date: ")

    if amount > 0:
        expenses.append({
            "description": description,
            "category": category,
            "amount": amount,
            "date": date
        })
        print("Expense Added Successfully...")
    else:
        print("Invalid Amount...")

def view_expenses():
    print("\nIndex\tDescription\tCategory\tAmount\tDate")

    for i, expense in enumerate(expenses, start=1):
        print(i, "\t",
            expense["description"], "\t",
            expense["category"], "\t",
            expense["amount"], "\t",
            expense["date"])

def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]
        else:
            summary[category] = expense["amount"]

    print("\nCategory Summary")

    for category, total in summary.items():
        print(category, ":", total)

def budget_report():
    total_spent = 0

    for expense in expenses:
        total_spent += expense["amount"]

    remaining = budget - total_spent
    percentage_used = (total_spent / budget) * 100

    print("\n*** BUDGET REPORT ***")
    print("Total Spent  : Rs.", total_spent)
    print("Budget Limit : Rs.", budget)
    print("Remaining    : Rs.", remaining)
    print("Used         :", round(percentage_used, 2), "%")

    if percentage_used >= 80:
        print("You have used", round(percentage_used, 2), "% of your budget!")

while True:
    print("\n*** PERSONAL EXPENSE TRACKER ***")
    print("1. Add Expense")
    print("2. View All")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        budget_report()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice...")    
        
        