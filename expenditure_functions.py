import sys

expenditure_log = {
    1: {"Amount": 50.75, "Category": "Groceries", "Description": "Weekly grocery shopping at the supermarket"},
    2: {"Amount": 120.00, "Category": "Utilities", "Description": "Electricity bill payment for August"},
    3: {"Amount": 15.99, "Category": "Entertainment", "Description": "Monthly subscription to a streaming service"},
    4: {"Amount": 200.00, "Category": "Rent", "Description": "Monthly rent for the apartment"},
    5: {"Amount": 30.00, "Category": "Transportation", "Description": "Gasoline for the car"},
    6: {"Amount": 12.50, "Category": "Dining", "Description": "Lunch at a local cafe"},
    7: {"Amount": 75.00, "Category": "Health", "Description": "Annual check-up at the clinic"},
    8: {"Amount": 40.00, "Category": "Clothing", "Description": "New shoes purchased online"},
    9: {"Amount": 25.00, "Category": "Education", "Description": "Online course subscription fee"},
    10: {"Amount": 60.00, "Category": "Entertainment", "Description": "Concert tickets for a weekend show"}
}

def log_expense():
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <= 0:
                raise ValueError("Amount must be a positive number")
            break
        except ValueError as e:
            print("Please enter a valid number.")

    while True:
        category = input("From this list of valid categories:\n"
                "Utilities, Entertainment, Rent, Transportation, Dining, Health, Clothing, Education, Groceries\n"
                "Enter the expense category: ").capitalize()

        valid_category = ["Utilities", "Entertainment", "Rent", "Transportation", "Dining", "Health", "Clothing", "Education", "Groceries"]
        if category not in valid_category:
            print(f"Invalid category, please pick from this list: {valid_category}")
        else:
            break

    while True:
        description = input("Enter the expense description: ").strip()
        if len(description) == 0:
            print("Please write a description of the expenditure.")
        else:
            break

    entry_id = len(expenditure_log) + 1
    expenditure_log[entry_id] = {"Amount": amount, "Category": category, "Description": description}

    print(f"Expense logged: Amount: {amount}, Category: {category}, Description: {description}")
    print("Entry added to Expenditure Tracker.")
    print(f"Thank you for using this app.")

def view_expenditure_list():
    view_options = ("1. Total Expenditure", "2. Expenditure by Category", "3. Expenditure with details")
    for i in view_options:
        print(i)

    user_view_option = input("Please type the number of the service you would like: ").strip()

    sum_of_expenditure = sum(info["Amount"] for info in expenditure_log.values())

    if user_view_option == "1":
        print(f"Total amount spent: {sum_of_expenditure}")

    elif user_view_option == "2":
        def expenditure_per_category():
            category_totals = {
                category: sum(info["Amount"] for info in expenditure_log.values() if info["Category"] == category)
                for category in set(info["Category"] for info in expenditure_log.values())
            }
            for category, total in category_totals.items():
                print(f"Category: {category}, Total: {total}")

        expenditure_per_category()

    elif user_view_option == "3":
        for entry_id, info in expenditure_log.items():
            amount = info["Amount"]
            category = info["Category"]
            description = info["Description"]
            print(f"Entry ID: {entry_id}, Amount: {amount}, Category: {category}, Description: {description}")
            print()

    else:
        sys.exit()
