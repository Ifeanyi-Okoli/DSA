""" 
You will be given an array of events, which are represented by strings. The strings are dates in HH:MM:SS format.

It is known that all events are recorded in chronological order and two events could not occur in the same second. Define the minimum number of days during which the log is written.

Example:

Input -> ["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]
Output -> 1

Input -> ["12:12:12"]
Output -> 1

Input -> ["12:00:00", "23:59:59", "00:00:00"]
Output -> 2
"""

# def check_logs(events):
#     def get_day(timestamp):
#         return timestamp[:2]

#     days = 1
#     for i in range(1, len(events)):
#         if get_day(events[i]) != get_day(events[i - 1]):
#             days += 1

#     return days



def check_logs(events):
    days = 1
    if len(events)==1: return days
    else:
        for i in range(1, len(events)):
            cur = events[i][:2]
            prev =events[i-1][:2]
            cmin = events[i][3:5]
            pmin = events[i-1][3:5]
            csec = events[i][6:]
            psec = events[i-1][6:]
            if cur < prev:
                days += 1
            elif cur == prev:
                if cmin < pmin:
                    days += 1
                elif cmin == pmin:
                    if csec < psec:
                        days += 1

        return days

print(check_logs(["12:12:12"]), 1)
print(check_logs(["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]), 1)
print(check_logs(["12:00:00", "23:59:59", "00:00:00"]), 2)