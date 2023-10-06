city_A = 'Bolzano-Bozen'
city_B = 'Milan'

# data retrieved on Otc 3 2023
# comp_percent = [consumer_AB, consumer_rent_AB, rent_AB, restaurant_AB, grocery_AB, lpp_AB]
comp_percent = [8.9, 20.6, 42.8, 13.6, 9.6, 50.6]
is_higher = [0, 0, 0, 0, 0, 1]

# convert
comp_percent_convert = [] # to store the converted results
for i in range(len(is_higher)):
    if is_higher[i]:
        comp_percent_convert.append((1 - 1 / (1 + comp_percent[i] / 100)) * 100)
    else:
        comp_percent_convert.append((1/(1 - comp_percent[i]/100) - 1) * 100)

# round the results
round_results = [round(percent, 1) for percent in comp_percent_convert] # list comprehension
# # which is equal to
# round_results = []
# for percent in comp_percent_convert:
#     round_results.append(round(percent, 1))

# if is_higher[0] is 0, then we can retrieve the term "higher" by lower_higher[0]
higher_lower = ['higher', 'lower']
lh_convert = [higher_lower[i] for i in is_higher] # list comprehension
# # which is equal to
# lh_convert = []
# for i in is_higher:
#     lh_convert.append(higher_lower[i])

# print the results
conversion_text = f"""
Consumer Prices in {city_B} are {round_results[0]}% {lh_convert[0]} than in {city_A} (without rent)
Consumer Prices Including Rent in {round_results[1]}% are {lh_convert[1]} than in {city_A}
Rent Prices in {city_B} are {round_results[2]}% {lh_convert[2]} than in {city_A}
Restaurant Prices in {city_B} are {round_results[3]}% {lh_convert[3]} than in {city_A}
Groceries Prices in {city_B} are {round_results[4]}% {lh_convert[4]} than in {city_A}
Local Purchasing Power in {city_B} is {round_results[5]}% {lh_convert[5]} than in {city_A}
"""
print(conversion_text)

# the script is much more compact and manageable for now
