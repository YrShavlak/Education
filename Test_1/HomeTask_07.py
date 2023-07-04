"""HomeTask_07.

Convert a non-negative integer num to its
English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"
let's take that number always > 100 and
only three digits
100 <= num <= 999
"""

num = input('Enter value between 100 and 999: ')
num_value = int(num)


def numbertowords(value):
    """Convert numbers to words."""
    if value < 100 or value > 999:
        print('Out of range')
        return

    numeral = {1: 'One', 2: 'Two', 3: 'Tree', 4: 'Four', 5: 'Five', 6: 'Six',
               7: 'Seven', 8: 'Eight', 9: 'Nine'}
    tens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
            14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
            17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    twenty_plus = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                   60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

    def convert(num_arg):
        out = []
        if num_arg >= 100:
            out += [numeral[num_arg // 100], 'Hundred']
            num_arg = num_arg % 100
            if num_arg >= 20:
                out += [twenty_plus[num_arg - num_arg % 10]]
                num_arg = num_arg % 10
            elif num_arg >= 10:
                out += [tens[num_arg]]
                num_arg = 0
            if num_arg:
                out += [numeral[num_arg]]
        return out

    res = convert(value)
    total_res = ' '.join(res)
    print(total_res)


numbertowords(num_value)
