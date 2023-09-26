def main():
    print(f"Running Expense Tracker")
    # Get user input for expense
    get_user_expense()

    # Write their expense into a file
    save_expense_to_file()

    # Read file and summrize expense
    summarize_expenses()

def get_user_expense():
    print(f"Getting user expense")
def save_expense_to_file():
    print(f"Saving user expense")
def summarize_expenses():
    print(f"summarize user expense")

if __name__ == "__main__":
    main()