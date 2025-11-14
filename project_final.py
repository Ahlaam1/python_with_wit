import statistics

count = 0
expenses = []
costs = []

print("Welcome to your favourite expense tracker. Let us get started.")
quit_or_edit = input(
    "Press q to quit, or c to continue or e to edit entry: ").lower()

if quit_or_edit == 'c':
    while True:
        expense_name = input("What did you buy? ")
        expenses.append(expense_name)
        count += 1

        amount = float(input("How much was it? "))
        costs.append(amount)

        more = input("Add another? (y/n): ").lower()
        if more != 'y':
            break

elif quit_or_edit == 'e':
    if expenses:
        print("Current expenses: ")
        for i, (e, c) in enumerate(zip(expenses, costs)):
            print(f"{i}: {e} - {c}")

        index_of_exp = int(
            input('Enter the index of the cost/expense you wish to edit: '))
        if 0 <= index_of_exp < len(expenses):
            new_input = input(
                "Enter new expense and cost (e.g. 'Book 25'): ").split()
            if len(new_input) == 2:
                expenses[index_of_exp] = new_input[0]
                costs[index_of_exp] = float(new_input[1])
                print("Updated successfully!")
            else:
                print("Invalid input format.")
    else:
        print("You have nothing to edit buddy.")

if costs:
    total_spent = sum(costs)
    average_spent = statistics.mean(costs)
    highest_cost = max(costs)

    def highest_spent_on(expenses, costs):
        highest_cost = max(costs)
        for i in range(len(costs)):
            if costs[i] == highest_cost:
                return expenses[i]

    highest_expense = highest_spent_on(expenses, costs)

    print(f"""
Expenses recorded
    Total spent: {total_spent}
    Average spent: {average_spent}
    Highest cost was {highest_cost} spent on {highest_expense}
    """)
else:
    print("No expenses recorded.")
