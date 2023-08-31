""" 
This is a rather simple but interesting kata. Try to solve it using logic. The shortest solution can be fit into one line.

Task
The point is that a natural number N (1 <= N <= 10^9) is given. You need to write a function which finds the number of natural numbers not exceeding N and not divided by any of the numbers [2, 3, 5].

Example
Let's take the number 5 as an example:

1 - doesn't divide integer by 2, 3, and 5
2 - divides integer by 2
3 - divides integer by 3
4 - divides integer by 2
5 - divides integer by 5
Answer: 1

because only one number doesn't divide integer by any of 2, 3, 5
"""

def real_numbers(n):
    return sum(all(num% divisor != 0 for divisor in [2, 3, 5]) for num in range(1, n+1))
    # or
    # count = 0
    # for num in range(1, n+1):
    #     for divisor in [2, 3, 5]:
    #         if num % divisor == 0:
    #             break
    #     else:
    #         count += 1
    # return count
    
    return n - (n // 2 + n // 3 + n // 5 + n // 30) + (n // 6 + n // 10 + n // 15)
    

print(real_numbers(5), 1)
print(real_numbers(10), 2)
print(real_numbers(20), 6)
print(real_numbers(30), 8)
print(real_numbers(40), 10)
print(real_numbers(55), 15)
print(real_numbers(66), 17)
print(real_numbers(75), 20)
print(real_numbers(100), 26)