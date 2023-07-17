"""HomeTask_11.

write generator function that has as input
some range value and chunk_size
produces output as lists with len == chunk size
Example:
Call:  chunk_generator(range(11), chunk_size=3) ->
Output:
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
[9, 10]
"""


def chunk_generator(list_range, chunk_size):
    """Generate the output list."""
    list_range = list(list_range)
    for i in range(0, len(list_range), chunk_size):
        yield list_range[i:i + chunk_size]


for result_list in chunk_generator(range(11), chunk_size=3):
    print(result_list)
