def display_menu():
    print('\n---Smart budget tracker---')
    print('1. Add income')
    print('2. Add expense')
    print('3. View summary')
    print('4. Exit')


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError('Please enter a positive number')
            return value
        except ValueError as e:
            print('Invalid:', e)


income = []
expense = []
expenses = {}


def add_income():
    amount = get_float_input('Enter income amount: ')
    income.append(amount)
    print('\nIncome added successfully!')
    print(income)


def add_expense():
    category = input('Enter the category (e.g., Food, Rent, Bill, etc...): ')
    amount = get_float_input('Enter expense amount: ')
    # expense.append({'category': category, 'amount': amount})

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    print('\nExpense added successfully!')


def view_summary():
    total_income = sum(income)
    total_expense = sum(item['amount'] for item in expenses)
    # amounts = []
    # for item in expense:
    #   amounts.append(item['amount'])
    balance = total_income - total_expense

    print('\n Budget summary:')
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expense:.2f}")
    print(f"Current Balance: {balance:.2f}")

    if balance < 0:
        print("You're overspending")
    elif balance < total_income * 0.2:
        print("You're close to budget limit")
    else:
        print("You're doing well!")

    print('\nExpense by category')
    # category_totals = {}

    # for item in expense:
    #   category = item['category'].lower()
    #   category_totals[category] = category_totals.get(category, 0) + item['amount']

    # for cat, amt in category_totals.items():
    #   print(f"{cat.capitalize()} : {amt:.2f}")

    for cat, amt in expenses.items():
        print(f"{cat.capitalize()} : {amt:.2f}")


while True:
    display_menu()
    choice = input('Enter your choice: ')
    if choice == '1':
        add_income()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        view_summary()
    elif choice == '4':
        break
    else:
        print('\nInvalid option')
