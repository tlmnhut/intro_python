# a)
num_sec = 60 * 60 * 24 * 365
print('There are {} seconds in a year'.format(num_sec))

# b)
# import the time module
import time
# get the current time in seconds since January 1, XXXX, 00:00:00 at UTC
seconds = time.time()

# the data type of seconds is float
print(seconds)
print(type(seconds))

# convert float to int
seconds_int = round(seconds)
# round() is better than int()
# example: round(1.6) is 2, but int(1.6) is 1
# you may get the same results with round(seconds) and int(seconds)
# but try to run the script a few times, you will see in some cases
# they are different

# to find out what year XXXX is, we first calculate how many years away since XXXX
# by dividing the number of seconds since XXXX by the number of seconds in a year: seconds_int // num_sec
# then subtract the current year by the obtained result
# // and / are both OK, // gives an integer result
year_xxxx = 2023 - seconds_int // num_sec
print(year_xxxx)
# a better approximation of the number of days in a year is 365.25, because we usually (not always) have
# 1 leap year with 366 days every 4 years

# c)
rand_0_1 = seconds_int % 2
print(rand_0_1)

rand_0_9 = seconds_int % 10
print(rand_0_9)

# to generate a number from 1 to 6, we generate from 0 to 5, then plus 1
rand_1_6 = seconds_int % 6 + 1
print(rand_1_6)

# to generate a number from -5 to 5, we generate from 0 to 10, then minus 5
rand_m5_5 = seconds_int % 11 - 5
print(rand_m5_5)

# if we run the script a few times, we will see that the generated numbers follow an
# increasing pattern, then it starts from low numbers and rises periodically again
# E.g. in the case of rand_0_9, we see something similar like this:
# 3 5 8   0 2 4 7 9   2 3 7 8 ...
# The reason is: seconds_int always increases over time, thus it makes the generated numbers
# increase, and if it goes over the largest number, e.g. 9 in the case of rand_0_9, it starts
# the cycle again
# Because there is a pattern in the "random" numbers, they are not truely random, they are just
# pseudo-random

