""" 
In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

years divisible by 4 are leap years
but years divisible by 100 are not leap years
but years divisible by 400 are leap years
Additional Notes:

Only valid years (positive integers) will be tested, so you don't have to validate them
Examples can be found in the test fixture.
"""

def is_leap_year(year):
    #your code here. Try to do it in one line.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2020), True, "Incorrect answer for year = 2020")
print(is_leap_year(2000), True, "Incorrect answer for year = 2000")
print(is_leap_year(2015), False, "Incorrect answer for year = 2015")
print(is_leap_year(2100), False, "Incorrect answer for year = 2100")
