name = 'Leo'
today_ddmmyyyy = '22-09-2023' # DD-MM-YYYY
temp_C = 25
dist_km = 30
money_eur = 2
message_eu = """
Hi Leo, welcome to Rovereto.
Today is 22-09-2023.
The temperature outside is 25 degree C.
Let's go to Trento in the afternoon, which is 30 km from here.
You will pay 2 EUR for the train ticket.
"""

today_mmddyyyy = today_ddmmyyyy[3:5] + '-' + today_ddmmyyyy[0:2] + '-' + today_ddmmyyyy[6:]
temp_F = (temp_C * 9/5) + 32
dist_mile = dist_km / 1.609
money_usd = money_eur * 1.05 # Oct 3 2023, 08:24 UTC
message_us = """
Hi Leo, welcome to Rovereto.
Today is {}.
The temperature outside is {} degree F.
Let's go to Trento in the afternoon, which is {} miles from here.
You will pay {} USD for the train ticket.
""".format(today_mmddyyyy, round(temp_F), round(dist_mile, 1), money_usd)  # round temperature, and
# round distance to 1 digit after the decimal point
print(message_us)

# randomly generate data
import time
seconds = round(time.time())
rand_temp_C = seconds % 61 - 10  # assume that the temperature ranges from -10 50 C

# these multiple assignments in one line can be used for any assignments,
# but I recommend using it for similar assignments
rand_dd, rand_mm, rand_yyyy = seconds % 28 + 1, seconds % 12 + 1, seconds % 50 + 2001
# we assume that dd is from 1 to 28, mm is from 1 to 12, yyyy is from 2001 to 2050
# we can safely avoid silly combinations, e.g. 30-02-2023

# now we combine the three elements, but we want to get 01-01-2023 instead of 1-1-2023
rand_ddmmyyyy = '{:02d}-{:02d}-{}'.format(rand_dd, rand_mm, rand_yyyy)
print(rand_temp_C, rand_ddmmyyyy)
