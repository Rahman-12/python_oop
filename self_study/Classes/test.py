

# def get_float(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             if value < 0:
#                 raise ValueError('Please enter a positive number')
#             return value
#         except ValueError as e:
#             print('Invalid:', e)


# # income = []


# # def add_income():
# #     for i in range(5):
# #         amount = get_float_input('Enter income amount: ')
# #         income.append(amount)
# #         print('\nIncome added successfully!')
# #         print(income)


# # add_income()


# expenses = {}


# def add_expense():
#     category = input('Enter the category (e.g., Food, Rent, Bill, etc...): ')
#     amount = get_float_input('Enter expense amount: ')
#     # expense.append({'category': category, 'amount': amount})

#     if category in expenses:
#         expenses[category] += amount
#     else:
#         expenses[category] = amount
#     print('\nExpense added successfully!')

#     print(expenses)


# add_expense()

# food_item = {}


# def add_food():
#     food_name = input("What is the name of the food: ")
#     protein = get_float('How much protein is in the food(g): ')
#     carbs = get_float('How much Carbs is in the food(g): ')
#     fat = get_float('How much Fat is in the food(g): ')

#     food_item[food_name] = {'protein': protein, 'carbs': carbs, 'fat': fat}

#     print(food_item)


# add_food()
