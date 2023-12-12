list1 = [1,2,3,4,5]
print(list1[0:5:2])

tup = (1,2,3,4,5)
print(tup[::-1])

sets = {1,2,4,5}
te = list(sets)
print(te[1:])

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Extract values for keys 'b' and 'c'
selected_values = [my_dict[key] for key in ['b', 'c']]
print("Selected Values from Dictionary:", selected_values)
