# 20. Sort lst_to_sort from min to max

print(sorted(lst_to_sort))


# 21. Sort lst_to_sort from max to min

print(sorted(lst_to_sort, reverse=True))


# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

lst_to_sort_updated = list(map(lambda x: x*2, lst_to_sort))
print(lst_to_sort_updated)


# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
raised_lists_numbers = list(map(lambda x, y: x**y, list_A, list_B))
print(raised_lists_numbers)


# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

from functools import reduce

sum = reduce(lambda x, y: x+y, lst_to_sort)
print (sum)


# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

lst_to_sort_filtered = list(filter(lambda elem: (elem % 2 == 1), lst_to_sort))
print (lst_to_sort_filtered)


# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

b_negative = list(filter(lambda value: value < 0, range (-10, 10)))
print (b_negative)



# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

lst_common = list(filter(lambda x: x in list_1, list_2))
print(lst_common)
