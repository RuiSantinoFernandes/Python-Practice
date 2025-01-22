# List Overlap  
# Exercise 5 
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#  ...write a program that returns a list that contains only the elements that are 
#   common between the lists (without duplicates). Make sure your program works on 
#   two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at 
#   this point - we’ll get to it soon)

# ANSWER TO PT.1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# common_list = set([i for i in a if i in b])

# print(list(common_list))

import random

rand_list_a = []
rand_list_b = []

for i in range(10,20,1):
    rand_list_a.append(random.randint(1,100))
    rand_list_b.append(random.randint(1,100))

common_list = set([i for i in rand_list_a if i in rand_list_b])

print(rand_list_a, rand_list_b, "Common List: "+ str(list(common_list)))