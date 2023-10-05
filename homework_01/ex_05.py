city_A = 'Bolzano-Bozen'
city_B = 'Milan'

# data retrieved on Otc 3 2023
consumer_AB = 8.9
consumer_rent_AB = 20.6
rent_AB = 42.8
restaurant_AB = 13.6
grocery_AB = 9.6
lpp_AB = 50.6

# convert
# if price a is lower than price b 20%, it means that price a is equal to 80% of price b
# then you can write a = 0.8*b, then b = 1/0.8*a, which is b = 1.25*a,
# then we can say price b higher than price a 25% (i.e. (1.25 - 1) * 100)
consumer_rev = (1/(1 - consumer_AB/100) - 1) * 100
consumer_rent_rev = (1/(1 - consumer_rent_AB/100) - 1) * 100
rent_rev = (1/(1 - rent_AB/100) - 1) * 100
restaurant_rev = (1/(1 - restaurant_AB/100) - 1) * 100
grocery_rev = (1/(1 - grocery_AB/100) - 1) * 100

# be careful that the last piece of data is "higher", not "lower"
# thus we need to reverse the conversion formula
# you can use the same reasoning as above to derive the formula
lpp_rev = (1 - 1/(1 + lpp_AB/100)) * 100

# since we have not known conditional statements yet, we hard-code the term higher lower for now
lower, higher = 'lower', 'higher'

# print the results
# since there are too many placeholders, .format() is quite difficult to use
# I will directly put the variable in the placeholder {} instead, and add character f right before the quote
conversion_text = f"""
Consumer Prices in {city_B} are {round(consumer_rev, 1)}% {higher} than in {city_A} (without rent)
Consumer Prices Including Rent in {city_B} are {round(consumer_rent_rev, 1)}% {higher} than in {city_A}
Rent Prices in {city_B} are {round(rent_rev, 1)}% {higher} than in {city_A}
Restaurant Prices in {city_B} are {round(restaurant_rev, 1)}% {higher} than in {city_A}
Groceries Prices in {city_B} are {round(grocery_rev, 1)}% {higher} than in {city_A}
Local Purchasing Power in {city_B} is {round(lpp_rev, 1)}% {lower} than in {city_A}
"""
print(conversion_text)

# the script is quite messy for now, but when we further learn about conditional statements, loops, list, function, etc
# we can make it more compact, manageable
