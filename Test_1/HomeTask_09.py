"""HomeTask_09.

write script that will read "input.txt" file
and find there all characters from english alphabet
collect these characters and their positions in file
after info collected this info as text write
to "output.txt" file in such format
####################
<first found letter> -> pos1
<next_letter> -> pos2
<next_letter -> pos3
etc
#######################
"""
import re

fh = open('input.txt', 'rt')
input_text = fh.read()
fh.close()

english_letter = []
for pos, el in enumerate(input_text, start=1):
    if bool(re.search('[a-zA-Z]', el)):
        english_letter.append((el, str(pos)))

with open('output.txt', 'w') as output_file:
    output_file.write('#######################\n')

    for letter, position in english_letter:
        output_file.write(f'{letter} -> pos{position}\n')

    output_file.write('#######################\n')
