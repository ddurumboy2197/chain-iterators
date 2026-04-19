import itertools

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

combined_iterator = itertools.chain(list1, list2, list3)

for item in combined_iterator:
    print(item)
