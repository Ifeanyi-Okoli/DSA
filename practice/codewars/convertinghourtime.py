""" 
Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.

Notes
By convention, noon is 12:00 pm, and midnight is 12:00 am.
On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015.
"""

def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    # return a string in the format "hhmm"
    # hh is the hour, written as two digits, range 00 to 23
    # mm is the minute, written as two digits, range 00 to 59
    # note the leading zeroes
    
    if period == 'am':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    return f'{hour:02}{minute:02}'

#or

    return '%02d%02d' % (hour % 12 + 12 * (period == 'pm'), minute)

print(to24hourtime( 1,  0, 'am'), '0100')
print(to24hourtime( 1,  0, 'pm'), '1300')
print(to24hourtime(12,  0, 'am'), '0000')
print(to24hourtime(12,  0, 'pm'), '1200')
print(to24hourtime( 6, 30, 'am'), '0630')
print(to24hourtime( 9, 45, 'pm'), '2145')

