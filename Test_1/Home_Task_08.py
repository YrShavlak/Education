"""Home_Task_08.

Given the list of integers ( positive , negative, zeros)
Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)
"""

l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
l2 = [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]


def max_multiplication(list):
    """Find and print max multiplication."""
    list.sort()
    max_value_list_1 = list[-1] * list[-2] * list[-3]
    max_value_list_2 = list[0] * list[1] * list[-1]
    if max_value_list_1 >= max_value_list_2:
        print(f'Max value_l1 = {max_value_list_1}.'
              f' Nums are: ({list[-1]},{list[-2]},{list[-3]})')
    else:
        print(f'Max value_l1 = {max_value_list_2}.'
              f' Nums are: ({list[0]},{list[1]},{list[-1]})')


max_multiplication(l1)
max_multiplication(l2)
