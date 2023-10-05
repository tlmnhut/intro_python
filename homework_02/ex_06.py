# You can show that there are many methods only belonging to a specific data type
# Methods of list but cannot be found in string: .append(), etc
# Methods of string but cannot be found in list: .lower(), etc

# Some more subtle differences
# Elements of a list may have different data types, while each character in a string is always a string
my_list = ['a', 'b', 1]
print(type(my_list[-1]), type(my_list[0]))  # 1 is int
my_string = 'ab1'
print(type(my_string[-1]), type(my_string[0])) # 1 is str

# You can not re-assign a character in a string
my_string[0] = 'c' # TypeError: 'str' object does not support item assignment
