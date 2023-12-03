'''
ASSIGNMENT
Write a function num_countries_in_days that takes a maximum amount of days max_days and the time 
increase factor factor, then returns the number of countries an influencer can visit within that time limit.

For example:

- Max days: 2
- Time factor: 1.2
Countries visited: 1
=====================================
- Max days: 3
- Time factor: 1.2
Countries visited: 2

'''
def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        time_left -= time_in_country
        time_in_country *= factor
        count += 1
    return count


# commented
def num_countries_in_days(max_days, factor):
    # This function takes two numbers as input: max_days and factor.
    # max_days is the total number of days that the traveler has,
    # and factor is the number of times the traveler can spend
    # the number of days in a country each day.

    # Here we are declaring three variables:

    # time_left stores the number of days that the traveler has left.
    # count stores the number of countries that the traveler has visited.
    # time_in_country stores the number of days that the traveler spends in a country each day.

    time_left = max_days
    count = 0
    time_in_country = 1

    # This while loop iterates until the traveler has no more days left.

    while time_left >= time_in_country:
        # The traveler spends time_in_country days in a country.
        time_left -= time_in_country

        # The traveler increases the number of days that they spend in a country each day by factor.
        time_in_country *= factor

        # The traveler increases the number of countries that they have visited by 1.
        count += 1

    # This returns the number of countries that the traveler has visited.
    return count
