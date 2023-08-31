""" 
#Unflatten a list (Easy)

There are several katas like "Flatten a list". These katas are done by so many warriors, that the count of available list to flattin goes down!

So you have to build a method, that creates new arrays, that can be flattened!

#Shorter: You have to unflatten a list/an array.

You get an array of integers and have to unflatten it by these rules:

- You start at the first number.
- If this number x is smaller than 3, take this number x direct 
  for the new array and continue with the next number.
- If this number x is greater than 2, take the next x numbers (inclusive this number) as a 
  sub-array in the new array. Continue with the next number AFTER this taken numbers.
- If there are too few numbers to take by number, take the last available numbers.
"""

def unflatten(flat_array):
    #your code here
    arr = flat_array[:]
    print(arr)
    result = []
    i = 0
    while i < len(flat_array):
        if flat_array[i] < 3:
            result.append(flat_array[i])
            i += 1
        else:
            result.append(flat_array[i:i+flat_array[i]])
            i += flat_array[i]
    return result


print(unflatten([ 3, 5, 2, 1 ]), [[ 3,5,2 ], 1 ])
print(unflatten([ 1, 4, 5, 2, 1, 2, 4, 5, 2, 6, 2, 3, 3 ]), [1, [4,5,2,1], 2, [4,5,2,6], 2, [3, 3] ])
print(unflatten([ 1, 1, 1, 1 ]),[ 1, 1, 1, 1 ])
print(unflatten([ 1 ]),[ 1 ])
print(unflatten([ 99, 1, 1, 1 ]),[ [ 99, 1, 1, 1 ] ])
print(unflatten([ 3, 1, 1, 3, 1, 1 ]),[[3,1,1], [3,1,1]])