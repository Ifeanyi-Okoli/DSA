""" 
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained (Read the notes for more detail about it)
Example
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9.

Notes
"""

def expression_matter(a, b, c):
    # Good Luck!
    return max(a+b+c, a*b*c, (a+b)*c, a*(b+c), a*b+c, a+b*c)


print(expression_matter(2, 1, 2), 6)
print(expression_matter(2, 1, 1), 4)
print(expression_matter(2, 2, 4), 16)
print(expression_matter(3, 3, 3), 27)
print(expression_matter(1, 1, 1), 3)
print(expression_matter(1, 2, 3), 9)
print(expression_matter(1, 3, 1), 5)
print(expression_matter(2, 2, 2), 8)
print(expression_matter(5, 1, 3), 20)
print(expression_matter(3, 5, 7), 105)
print(expression_matter(5, 6, 1), 35)
print(expression_matter(1, 6, 1), 8)
print(expression_matter(2, 6, 1), 14)
print(expression_matter(6, 7, 1), 48)
print(expression_matter(2, 10, 3), 60)
print(expression_matter(1, 8, 3), 27)
print(expression_matter(9, 7, 2), 126)
print(expression_matter(1, 1, 10), 20)
print(expression_matter(9, 1, 1), 18)
print(expression_matter(10, 5, 6), 300)
print(expression_matter(1, 10, 1), 12)