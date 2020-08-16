# Write a function named readable_timedelta. The function should take one argument, an integer days, and return a
# string that says how many weeks and days that is. For example, calling the function and printing the result like
# this:

# print(readable_timedelta(10))

# should output the following:

# 1 week(s) and 3 day(s).


def readable_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    return"There are {} week and {} days in a total of {} days".format(weeks, remainder, days)

# write your function here


# test your function
print(readable_timedelta(10))
