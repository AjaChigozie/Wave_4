def readable_timedelta(days):
    # insert your docstring here
    """THIS IS A FUNCTION TO SHOW HOW MANY WEEKS AND DAYS ARE IN A GIVEN NUMBER OF DAYS
    INPUT:
    days: The number of days to be checked, in this case 10
    OUTPUT:
    weeks: to show how many weeks can be found in the number of days given.
    remainder: to show the number of days remaining after the week has been checked."""

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


print(readable_timedelta(10))
