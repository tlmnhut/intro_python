num_list = [1, 2, 3]

# What are the results? You may guess the results before running them
num_list * 2 # [1, 2, 3, 1, 2, 3], the list does not change
num_list + [1, 2, 3] # [1, 2, 3, 1, 2, 3], the list does not change
num_list.append([1, 2, 3]) # [1, 2, 3, [1, 2, 3]], a nested list, and the list also changes
num_list.extend([1, 2, 3]) # [1, 2, 3, [1, 2, 3], 1, 2, 3], the list also changes
# append and extend change the list, + and * do not
# + * and extend (if applied to the original list) give the same results

# Create a list of 100 zeros
list_zero = [0] * 100
print(len(list_zero))
# Create a list of 50 zeros following by 50 ones
list_zero_one = [0] * 50 + [1] * 50  # not the same as ([0] + [1]) * 50
print(len(list_zero_one))
