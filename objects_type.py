# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print (id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))


# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))


# 3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))


# 4*. Check the type of the objects by using isinstance.
print ("Is 55 an integer? ", isinstance(int_a, int)),
print ("Is 'cursor' a string? ", isinstance(str_b, str))
print ("Is {1, 2, 3} a set? ", isinstance(set_c, set))
print ("Is [1, 2, 3] a list? ", isinstance(lst_d, list))
print ("Is {'a': 1, 'b': 2, 'c': 3} a dictionary? ", isinstance(dict_e, dict))
