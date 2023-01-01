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
    compute_array = input_array.copy()
    # 2³ = 8 which is greater than test_list length so I only need 3 iterations to resolve the problem
    while iterations < 3:
        iterations += 1
        currentMiddle = findMiddle(compute_array)
        currentMiddleIndex = compute_array.index(currentMiddle)
        if value == currentMiddle:
            return input_array.index(currentMiddle)
        if value < currentMiddle:
            compute_array = compute_array[0: currentMiddleIndex]
        if value > currentMiddle:
            compute_array = compute_array[currentMiddleIndex + 1::]
    return -1

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
