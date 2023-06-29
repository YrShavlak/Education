"""HomeTask_06.

We have two lists with equal or different size
ex. l1=[1,3,5,7]  l2=[1,4,5]
task:
create list that will store such values
list_target = [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set
if no such element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data
should produce list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions
Advices:
set of (list1 indexes union list2 indexes) could
be helpful to get larger indexes scope ( or use if-else)
dict as you remember has default value if key was not found d1.get(key, 0)
"""
l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]

len_l1 = len(l1)
len_l2 = len(l2)
if len_l1 > len_l2:
    indexes = set(range(0, len_l1))
else:
    indexes = set(range(0, len_l2))

l1_dict = {value: key for value, key in enumerate(l1)}
print('l1_dict ', l1_dict)
l2_dict = {value: key for value, key in enumerate(l2)}
print('l2_dict ', l2_dict)

list_target_l1 = [(l1_dict.get(i, 0), l2_dict.get(i, 0)) for i in indexes]
print('list_target_l1 ', list_target_l1)
list_target_l2 = [(l2_dict.get(i, 0), l1_dict.get(i, 0)) for i in indexes]
print('list_target_l2 ', list_target_l2)




