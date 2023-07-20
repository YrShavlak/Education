"""HomeTask_12.

Given list of list of list etc of integers
write recursive function that will
accept as argument target list
and return sum of all integers inside it
Input: [[[[1, 4, 5], [[6, 9],[[[8, 1],
7], 3], 2], 7], 5, 2], 9, [1, 2]]
Output: Target sum = 72
"""


def sum_list(target_list):
    """Sum of all integers in the target_list."""
    total_sum = 0

    for item in target_list:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, list):
            total_sum += sum_list(item)

    return total_sum


input_list = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
result = sum_list(input_list)
print('Target sum =', result)
