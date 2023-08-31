""" 
The function receives a parameter n, which indicates the maximum number of points on one domino tile.

Test values are 0 < n < 1000

Output data:

Your function should return the optional number of diamond stones to be made for a given set of dice.

Example:

For dominoes where the maximum possible number on the knuckle is 2, the possible knuckles will be as follows --> 0 | 1, 0 | 2, 1 | 1, 1 | 2, 2 | 2 therefore, the sum of all values on the knuckles will be 1 + 2 + 1 + 1 + 1 + 2 + 2 + 2 = 12

2 --> 12
3 --> 30
20 --> 4620
"""

def dots_on_domino_bones(n):
    return int(n*(n+1)*(n+2)/2)


print(dots_on_domino_bones(2), 12)
print(dots_on_domino_bones(5), 105)
print(dots_on_domino_bones(13), 1365)
print(dots_on_domino_bones(20), 4620)
print(dots_on_domino_bones(33), 19635)
print(dots_on_domino_bones(50), 66300)
print(dots_on_domino_bones(0), 0)
print(dots_on_domino_bones(137), 1313967)
print(dots_on_domino_bones(198), 3940200)