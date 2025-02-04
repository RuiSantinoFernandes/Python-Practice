# String Lists  
# strings lists index
# Exercise 6 (and Solution)
# Ask the user for a string and print out whether this string is 
# a palindrome or not. (A palindrome is a string that reads 
# the same forwards and backwards.)

while True:
    # Take a user input
    user_input = input("Enter a word or phrase... (or 'quit' to exit): ")

    # Make string input lower case
    pal_low = user_input.lower()
    # Remove spaces from string input
    pal = pal_low.replace(" ","")
    # Reverse the input to check palindrome
    reverse = pal[::-1]


    if user_input.lower() == 'quit':
        break # Exit if user quits
    elif pal == reverse:
        print("You entered a palindrome!")
    else:
        print("Your entry is not a palindrome...")