my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# my_list[::-1] shows the reversed list, which is similar to my_list.reverse()
# however, my_list[::-1] does not change the list, while my_list.reverse() does
# you can do my_list[::-1] then print(my_list), you will see the list is unchanged

# Select the 2nd element in the list
print(my_list[1])

# Select the 2nd last element in the list. You can use both positive and negative indexes.
print(my_list[8], my_list[-2])

# Suppose that we do not know the length of the list in advance,
# and god forbids us from using a negative index, what should you do?
print(my_list[len(my_list) - 2]) # get the length of the list by len(my_list)

# Select three first numbers: [0, 1, 2]
print(my_list[:3], my_list[0:3])

# Select three last numbers: [7, 8, 9]
print(my_list[-3:], my_list[len(my_list)-3:], my_list[7:])

# Select three first and last numbers: [0, 1, 2, 7, 8, 9]
new_list = my_list[:3]
new_list.extend(my_list[-3:])
print(new_list)
# or simpler:
print(my_list[:3] + my_list[-3:])

# Somehow select numbers and print this list: [2, 1, 0, 9, 8, 7]
new_list = my_list[:3]
new_list.reverse()
another_new_list = my_list[-3:]
another_new_list.reverse()
new_list.extend(another_new_list)
print(new_list)
# or simpler:
print(my_list[:3][::-1] + my_list[-3:][::-1])
# my_list[:3].reverse() + my_list[-3:].reverse() does not work
# because while .reverse() modifies the original list, it returns None, so we get None + None (error)

# Select only odd numbers: [1, 3, 5, 7, 9]
print(my_list[1::2])

# Select only odd numbers, but reversed: [9, 7, 5, 3, 1].
print(my_list[::-2], my_list[1::2][::-1])
