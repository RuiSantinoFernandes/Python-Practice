# Odd Or Even 
# input if types int equality comparison numbers mod
# Exercise 2 

# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.

# Expected Results:
# Enter a number... 372
# Enter another number to check... 66
# 372 is a multiple of 4 and it is even.
# 372 is NOT divisible by 66.

number = int(input("Enter a number... "))
check = int(input("Enter another number to check... "))

# Determine if the number is even, odd, or a multiple of 4
if number % 4 == 0:
    print(f"{number} is a multiple of 4 and it is even.")
else:
    print(f"{number} is {'even' if number % 2 == 0 else 'odd'}.")

# Check divisibility
print(f"{number} is {'divisible' if number % check == 0 else 'NOT divisible'} by {check}.")
