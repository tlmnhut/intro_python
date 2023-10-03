first_name = 'Nhut'
print('My first name is {}, which has {} characters'.format(first_name, len(first_name)))

# I prefer the syntax below:
print(f'My first name is {first_name}, which has {len(first_name)} characters')
# You put an f just before the quote, then you directly type the variables inside {}
# Personally I avoid .format() because it requires more effort to do position matching,
# but .format() will be useful when we want to print some customized formats, such as
# 3 digits after the decimal point

last_name = 'Truong'
print('My last name is {}, which has {} characters'.format(last_name, len(last_name)))

full_name = first_name + ' ' + last_name
print('My full name is {}'.format(full_name))
