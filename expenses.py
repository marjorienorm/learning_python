# This was the original version with the expenses hard-coded
# The above is a single line comment example
"""
expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum = 0

for expense in expenses:
    sum = sum + expense

print("You spent $", sum, " on lunch this week.", sep='')
"""

total = 0
expenses = []
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for i in range(0, 7, 1):
    expenses.append( float( input( print("Enter an expense for ", days[i], ":"))))

total = sum( expenses)

print("You spent $", total, " on lunch this week.", sep='')