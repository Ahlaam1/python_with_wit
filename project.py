import array
import statistics

count = 0
proceed = False
expenses = []
costs = []
quit_track = False
exit_track = False
edit = False


print("Welcome to your favourite expense tracker. Let us get started.")
quit_or_edit = str(
    input(" Press q to quit, or c to continue or e to edit entry: ").lower()
)
if quit_or_edit == 'q':
    quit_track = True
elif quit_or_edit == 'c':
    proceed = True
elif quit_or_edit == 'e':
    edit = True

while proceed:
    expense_name = (str(input("What did you buy?")))

    expenses.append(expense_name)
    count = count + 1

    amount = (float(input("How much was it?")))
    costs.append(amount)

    Total_spent = sum(costs)
    average_spent = statistics.mean(costs)
    highest_cost = max(costs)


if not expenses:
    if edit:
        print("Current expenses: ")
        for i, (e, c) in enumerate(zip(expenses, costs)):
            print(f"{i}: {e} - {c}")
        index_of_exp = int(
            input('Please enter the index of the cost/expense you wish to edit: '))
        for i, (e, c) in enumerate(zip(expenses, costs)):
            if index_of_exp == i:
                dict editing =
                input('Please enter expense and value: ')
            list.append()


def highest_spent_on():
    for i in range(count):
        if costs[i] == highest_cost:
            return expenses[i]


highest_expense = highest_spent_on()


print(f""" 

Expenses recorded
      Total spent: {Total_spent}
      average spent: {average_spent}
      highest cost was {highest_cost} spent on {highest_expense}

      """)
