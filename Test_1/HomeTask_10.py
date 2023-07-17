"""HomeTask_10.

# open input.txt file and find all small
english letters that match such conditions:
# target small letter round exactly with
three capital english letters on the left and on the right
# Match examples:
# sdTRYaUVKn  -> matches "a"
# NTRSjARTb   -> no match ( not exactly 3 capital
letters on the left)
# zDFGbOPNq   -> matches "b"
# Print Output as : "Result: "<your_found_human_readable_string">
"""

import re

fh = open('input_1.txt', 'rt')
input_text = fh.read()
fh.close()

letters = re.findall(r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])',
                     input_text)

search_text = 'Result: ' + ''.join(letters)
print(search_text)
