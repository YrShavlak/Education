""" Count each vowel occurence in text bellow and replace it."""

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

Counter_Letters = {
    'a': poem_text.count('a') + poem_text.count('A'),
    'e': poem_text.count('e') + poem_text.count('E'),
    'i': poem_text.count('i') + poem_text.count('I'),
    'o': poem_text.count('o') + poem_text.count('O'),
    'u': poem_text.count('u') + poem_text.count('U'),
}

sep_num = 21
print('-' * sep_num)
print(f"| {'Vowel':^8} | {'Count':^6} |")
print('-' * sep_num)

for vowel, count in Counter_Letters.items():
    print(f'| {vowel:^9}|  {count:^5} |')
print('-' * sep_num)

new_text = poem_text.replace('A', 'À').replace('a', 'à').replace('E', 'É')\
    .replace('e', 'é').replace('I', 'Í').replace('i', 'í').replace('O', 'Ó')\
    .replace('o', 'ó').replace('U', 'Ú').replace('u', 'ú')
print(new_text)
