""" 
Your task is to find the maximum number of queens that can be put on the board so that there would be one single unbeaten square (ie. threatened by no queen on the board).

The Queen can move any distance vertically, horizontally and diagonally.

Input
The queens(n) function takes the size of the chessboard.

�
∈
�
n∈Z, so it can be negative, and values can go up to 
14
1
1000
141 
1000
 .

Output
The maximum number of queens to leave one single unbeaten square
Return 0 if n is negative.
"""

def queens(n):
    return 0

print(queens(0), 0)
print(queens(1), 0)
print(queens(2), 0)
print(queens(3), 2)
print(queens(4), 6)
print(queens(5), 12)
print(queens(6), 20)
print(queens(20), 342)
print(queens(33), 992)
print(queens(50), 2352)