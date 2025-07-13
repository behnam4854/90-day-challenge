"""Day 5 : build a command-line app the track daily expenses, and then add it to a csv file"""

# what do I need 1.the price or the amount I spend 2.the description
# lets build version 1
import csv
import os
from datetime import datetime


class Expense:
    def __init__(self, description, amount, date, category):
        self.description = description
        self.amount = amount
        self.date = date
        self.category = category

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')}: {self.description} - {self.amount:,} rials - {self.category}"


EXPENSES_FILE = "expense.csv"


def load_expenses():
    expenses = []
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                description, amount, date_str, category = row
                date = datetime.strptime(date_str, '%Y-%m-%d')
                expenses.append(Expense(description, int(amount), date, category))
    return expenses


def save_expenses(expenses):
    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense.description, expense.amount, expense.date.strftime('%Y-%m-%d'), expense.category])


def date_converter(date):
    """simple date converter for the app"""
    if not date:
        date = datetime.now()
    else:
        date = datetime.strptime(date, '%Y-%m-%d')
    return date


# todo how can i add category by the provided numbers in the console
cats = ["food", "entertainment", "sports", "technology", "utility", "car", "home_stuff"]


def add_expense(expenses):
    description = input("Enter the expense description: ")
    amount = int(input("Enter the expense amount: "))
    date_input = input("Enter the expense date (YYYY-MM-DD) or press Enter for today: ")
    date = date_converter(date_input)
    for idx, cat in enumerate(cats):
        print(f"{idx + 1}. {cat}")
    category = int(input("select the category of the expense : "))
    expenses.append(Expense(description, amount, date, cats[int(category-1)]))
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("Expenses:")
    for idx, expense in enumerate(expenses):
        print(f"{idx + 1}. {expense}")


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    index = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        deleted_expense = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted expense: {deleted_expense}")
    else:
        print("Invalid index.")


def total_expenses(expenses):
    sum_expenses = 0
    if not expenses:
        print("No expenses recorded.")
        return
    start_date = input("Enter the start date (YYYY-MM-DD) or press Enter for today: ")
    end_date = input("Enter the end date (YYYY-MM-DD) or press Enter for today: ")

    start_date = date_converter(start_date)
    end_date = date_converter(end_date)

    for idx, expense in enumerate(expenses):
        if start_date <= expense.date <= end_date:
            sum_expenses += expense.amount

    print("total expenses in Rial:", sum_expenses)


def main():
    expenses = load_expenses()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expense")
        print("5. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            total_expenses(expenses)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
