list_of_lists = [[1, 2, 3], [4, 5, 6]]
list1 = [4, 5, 6, 7]
list1_as_set = set(list1)
result = any(list1_as_set.issuperset(l) for l in list_of_lists)  # True
print(result)
print(list1_as_set)
print(list1_as_set.issuperset([2]))
print(list1_as_set.issuperset([3]))
print(list1_as_set.issuperset([4,5]))
# for l in list_of_lists:
#     if list1_as_set.issuperset(l):
#         result = True
#         break
# else:
#     result = False