"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    iterations = 0
    while iterations < 3:
        mid_index = int((len(input_array) - 1) / 2)
        num_to_compare = input_array[mid_index]
        if num_to_compare == value:
            return value
        if value > num_to_compare:
            input_array = input_array[mid_index: len(input_array)]
        else:
            input_array = input_array[0: mid_index]
        iterations += 1
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
