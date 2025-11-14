import statistics
import math
expenses = []
costs = []


print("Welcome to the best expense tracker. Let us get started")
num_of_items = int(input("How many items did you spend on? "))
for i in range(num_of_items):

    expense_name = str(input("What did you buy? : "))
    expenses.append(expense_name)

    cost = float(input("How much was it? : "))
    costs.append(cost)

for i, (e, c) in enumerate(zip(expenses, costs)):
    print(f"{i} : {e} - {c}")

edit_result = input(
    "Press e to edit responses before the breakdown or p to proceed: ")
if edit_result == 'p':
    average_spent = statistics.mean(costs)

    index_of_highest = costs.index(max(costs))
    highest_spent_on = expenses[index_of_highest]

    total = sum(costs)
    print(f"""Total expenses: {total}
              average spent: {average_spent}
              highest spent on: {highest_spent_on}

 """)
elif edit_result == 'e':
    index_of_exp = int(input("input the index of the item you want to edit: "))
    if 0 <= index_of_exp < len(expenses):
        new_input = input(
            "Now you type in the item in the format (Book 25): ").split()
        expenses[index_of_exp] = new_input[0]
        costs[index_of_exp] = float(new_input[1])
        for i, (e, c) in enumerate(zip(expenses, costs)):
            print(f"{i} : {e} - {c}")
        print("Updated successfully we should now get to the breakdown")
        average_spent = statistics.mean(costs)

        index_of_highest = costs.index(max(costs))
        highest_spent_on = expenses[index_of_highest]

    total = sum(costs)
    print(f"""Total expenses: {total}
average spent: {average_spent}
highest spent on: {highest_spent_on}

    """)
