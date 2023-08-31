""" 
You need to count the number of prime numbers less than or equal to some natural n.

For example:

count_primes_less_than(34) = 11
count_primes_less_than(69) = 19
count_primes_less_than(420) = 81
count_primes_less_than(666) = 121
In this kata all the tests will be with 
1
⩽
�
⩽
1
0
10
1⩽n⩽10 
10
 
Code length limited to 3000 characters to avoid hardcoding.
Good luck!
"""

# def is_prime(num):
#     if num == 2: return True
#     if num < 2 or num % 2 == 0: return False
#     for i in range(3, int(num**0.5)+1, 2):
#         if num % i == 0: return False
#     return True

# def count_primes_less_than(n: int) -> int:
#     # Your code here
#     count = 0
#     for num in range(2, n):  
#         if is_prime(num): count += 1
#     return count
# # or

# def count_primes_less_than(n: int) -> int:
#     return sum(is_prime(num) for num in range(2, n))

# # or
# def count_primes_less_than(n: int) -> int:
#     return len(is_prime(num) for num in range(2, n))

#or
def count_primes_less_than(n: int) -> int:
    if n <= 2: return 0
    
    sieve = [True] * n
    
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5)+1):
        print(int(n**0.5)+1)
        if sieve[i]:
            for j in range(i*i, n, i):
                
                sieve[j] = False
    print (sum(sieve))
    return sum(sieve)
print(count_primes_less_than(34), 11)
# print(count_primes_less_than(69), 19)
# print(count_primes_less_than(420), 81)
# print(count_primes_less_than(666), 121)
