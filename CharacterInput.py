# Character Input 
# input strings types int
# Exercise 1
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that 
# they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date 
# the next year). If you want to do this in a generic way, see exercise 39.

# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# Expected Results:
# What is your name? Input: "Rui"
# What is your age? Input: "26"
# Choose a number from 1-50. (This is the number of times your age will be printed.) Input: "5"
#
# Output: 
# Rui you will be 126 years old in 100 years!
# Rui you will be 126 years old in 100 years!
# Rui you will be 126 years old in 100 years!
# Rui you will be 126 years old in 100 years!
# Rui you will be 126 years old in 100 years!

name = input("What is your name? ")
age = int(input("What is your age? "))
age_calc = str(age + 100)
copy = int(input("Choose a number from 1-50. (This is the number of times your age will be printed.) "))

for _ in range(copy):
    print(name + " you will be " + age_calc + " years old in 100 years!")