"""
Let us say your expense for every month are listed below,
    1. January - 2200
    2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""

monthly_expense = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?
feb_extra_expense = monthly_expense[1] - monthly_expense[0]
print(f'Feb month extra expense: {feb_extra_expense}')

# Find out your total expense in first quarter (first three months) of the year.
print(f'Quater Expense: {monthly_expense[0]+monthly_expense[1]+monthly_expense[2]}')

# Find out if you spent exactly 2000 dollars in any month
print(f'spent exactly 2000 dollars in any month: {2000 in monthly_expense}')

# June month just finished and your expense is 1980 dollar. 
# Add this item to our monthly expense list
monthly_expense.append(1980)
print(f'June month Expense Adding: {monthly_expense}')

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this 

monthly_expense[3] = monthly_expense[3] - 200
print(f'April expense after retuning item: {monthly_expense}')