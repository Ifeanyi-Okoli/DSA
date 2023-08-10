""" 
Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the end result once gravity is switched on.

Examples
switch_gravity([
  ["-", "#", "#", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "#", "#", "-"]
]

"""


# def switch_gravity(lst):
#     n = len(lst)
#     for i in range(len(lst)):
#         bottom = n-1
#         for j in range(len(lst[i])):
#             if lst[i][j] == "#" and lst[bottom][j] == "-" and i < n-1:
#                 lst[i][j] = "-"
#                 lst[n-1][j] = "#"
#                 bottom = i + 1
#             # elif lst[i][j] == "#" and lst[n-2][j] == "-" and i < n-2:
#             #     lst[i][j] = "-"
#             #     lst[n-i-1][j] = "#"

#     return lst

import numpy as np

def switch_gravity(lst):
    return np.sort(lst, 0)[::-1].tolist()

# def switch_gravity(lst):
#     if not lst or all(all(cell == '-' for cell in row) for row in lst):
#         return lst

#     rows, cols = len(lst), len(lst[0])
#     for j in range(cols):
#         bottom_row = rows - 1
#         for i in range(rows - 1, -1, -1):
#             if lst[i][j] == "#":
#                 lst[i][j] = "-"
#                 lst[bottom_row][j] = "#"
#                 bottom_row -= 1

#     return lst


# print(switch_gravity([
#     ["-", "#", "#", "-"],
#     ["-", "-", "-", "-"],
#     ["-", "-", "-", "-"],
#     ["-", "-", "-", "-"]
# ]
# ))

# print(switch_gravity([
#     ["-", "#", "#", "-"],
#     ["-", "-", "#", "-"],
#     ["-", "-", "-", "-"],
# ]
# ))

""" 
, [
            ["-", "-", "-", "-"],
            ["-", "-", "#", "-"],
            ["-", "#", "#", "-"]
        ]
"""

# print(switch_gravity([
#     ["-", "#", "#", "#", "#", "-"],
#     ["#", "-", "-", "#", "#", "-"],
#     ["-", "#", "-", "-", "-", "-"],
#     ["-", "-", "-", "-", "-", "-"]
# ]
# ))

""" 
, [
            ["-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
            ["-", "#", "-", "#", "#", "-"],
            ["#", "#", "#", "#", "#", "-"]
        ]
"""

print(switch_gravity([
    ["-", "#", "#", "#", "#", "-"],
    ["#", "-", "-", "#", "#", "-"],
    ["-", "#", "-", "-", "-", "-"],
    ["-", "#", "-", "#", "-", "-"]
]
))


""" 
, [
            ["-", "-", "-", "-", "-", "-"],
            ["-", "#", "-", "#", "-", "-"],
            ["-", "#", "-", "#", "#", "-"],
            ["#", "#", "#", "#", "#", "-"]
        ]
"""

# print(switch_gravity([
#             ["-", "#", "#", "-"],
#             ["-", "-", "#", "-"],
#             ["#", "#", "-", "-"],
#         ]
#         ), [
#             ["-", "-", "-", "-"],
#             ["-", "#", "#", "-"],
#             ["#", "#", "#", "-"]
#         ])

print(switch_gravity([
    ["#"],
    ["-"],
    ["#"],
    ["-"]
]
))

""" 
, [
            ["-"],
            ["-"],
            ["#"],
            ["#"]
        ]
"""

print(switch_gravity([
    ["#"],
    ["#"],
    ["#"],
    ["#"]
]
))

""" 
, [
            ["#"],
            ["#"],
            ["#"],
            ["#"]
        ]
"""
