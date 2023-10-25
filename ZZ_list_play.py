
import random

# set up a list

my_list = []

# generate 4 random numbers between 1 amd 10
for item in range(0, 4):
    # generate number
    random_num = random.randint(1, 10)

    # add number to list
    my_list.append(random_num)

# print the *unsorted* list
print(my_list)

# sort the list
my_list.sort()

my_list_len = len(my_list)

# print the sorted list
print()
print(my_list)
print(f"The list has {my_list_len} items")
print()
