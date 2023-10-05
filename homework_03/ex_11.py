city_A = 'Bolzano-Bozen'
city_B = 'Milan'

# data retrieved on Otc 3 2023
# comp_percent = [consumer_AB, consumer_rent_AB, rent_AB, restaurant_AB, grocery_AB, lpp_AB]
comp_percent = [8.9, 20.6, 42.8, 13.6, 9.6, 50.6]
is_higher = [0, 0, 0, 0, 0, 1]

# convert
comp_percent_convert = [] # to store the converted results
if is_higher[0]:
    comp_percent_convert.append((1 - 1 / (1 + comp_percent[0] / 100)) * 100)
else:
    comp_percent_convert.append((1/(1 - comp_percent[0]/100) - 1) * 100)
if is_higher[1]:
    comp_percent_convert.append((1 - 1 / (1 + comp_percent[1] / 100)) * 100)
else:
    comp_percent_convert.append((1/(1 - comp_percent[1]/100) - 1) * 100)
if is_higher[2]:
    comp_percent_convert.append((1 - 1 / (1 + comp_percent[2] / 100)) * 100)
else:
    comp_percent_convert.append((1/(1 - comp_percent[2]/100) - 1) * 100)
if is_higher[3]:
    comp_percent_convert.append((1 - 1 / (1 + comp_percent[3] / 100)) * 100)
else:
    comp_percent_convert.append((1/(1 - comp_percent[3]/100) - 1) * 100)
if is_higher[4]:
    comp_percent_convert.append((1 - 1 / (1 + comp_percent[4] / 100)) * 100)
else:
    comp_percent_convert.append((1/(1 - comp_percent[4]/100) - 1) * 100)
if is_higher[5]:
    comp_percent_convert.append((1 - 1 / (1 + comp_percent[5] / 100)) * 100)
else:
    comp_percent_convert.append((1/(1 - comp_percent[5]/100) - 1) * 100)
# it is quite messy, we will reduce them with a for loop in the next homework

# if is_higher[0] is 0, then we can retrieve the term "lower" by lower_higher[0]
lower_higher = ['lower', 'higher']

# print the results
conversion_text = f"""
Consumer Prices in {city_B} are {round(comp_percent_convert[0], 1)}% {lower_higher[is_higher[0]]} than in {city_A} (without rent)
Consumer Prices Including Rent in {city_B} are {round(comp_percent_convert[1], 1)}% {lower_higher[is_higher[1]]} than in {city_A}
Rent Prices in {city_B} are {round(comp_percent_convert[2], 1)}% {lower_higher[is_higher[2]]} than in {city_A}
Restaurant Prices in {city_B} are {round(comp_percent_convert[3], 1)}% {lower_higher[is_higher[3]]} than in {city_A}
Groceries Prices in {city_B} are {round(comp_percent_convert[4], 1)}% {lower_higher[is_higher[4]]} than in {city_A}
Local Purchasing Power in {city_B} is {round(comp_percent_convert[5], 1)}% {lower_higher[is_higher[5]]} than in {city_A}
"""
print(conversion_text)

# the script is still quite messy for now, but when we further learn loops and function
# we can make it even more compact, manageable
