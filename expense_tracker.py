from expense import Expense
import calendar
import datetime

def main():
    print(f"Running Expense Tracker")
    expense_file_path="expenses.csv"
    # Get user input for expense
    expense = get_user_expense()
    
    # Write their expense into a file
    save_expense_to_file(expense,expense_file_path)

    # Read file and summrize expense
    summarize_expenses(expense_file_path,4000)

def get_user_expense():
    print(f"Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["Food","Home","Work","Fun","Misc"]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) -1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name,category=selected_category, amount = expense_amount)
            return new_expense
        else:
            print("Invalid category. please try again! ")
def save_expense_to_file(expense:Expense, expense_file_path):
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
def summarize_expenses(expense_file_path,budget):
    print(f"summarize user expense")
    expenses:list[Expense] = []
    with open(expense_file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name,expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense( name = expense_name,  category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)
        print(expenses)

        amount_by_category = {}
        for expense in expenses:
            key = expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key]= expense.amount
        print("Expenses By Category :")
        for key, amount in amount_by_category.items():
            print(f" {key}: ${amount:.2f}")
        
        total_spent = sum([x.amount for x in expenses])
        print(f"You've spent ${total_spent:.2f} this month!")

        remaing_budget = budget - total_spent
        print(f"Budget Remaining: ${remaing_budget:.2f}")

        # Get the current date
        now = datetime.datetime.now()

        # Get the number of days in the current month
        days_in_month = calendar.monthrange(now.year, now.month)[1]

        # Calculate the remaining number of days in the current month
        remaining_days = days_in_month - now.day

        daily_budget = remaing_budget/remaining_days
        print(green(f"Budget Per Day: ${daily_budget:.2f}"))
     
def green(text):
    return f"\033[92m{text}\033[0m"



if __name__ == "__main__":
    main()