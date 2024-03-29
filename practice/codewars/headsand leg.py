""" 
Everybody has probably heard of the animal heads and legs problem from the earlier years at school. It goes:

“A farm contains chickens and cows. There are x heads and y legs. How many chickens and cows are there?” 

Where x <= 1000 and y <=1000

#Task

Assuming there are no other types of animals, work out how many of each animal are there.

Return a tuple in Python - (chickens, cows) and an array list - [chickens, cows]/{chickens, cows} in all other languages

If either the heads & legs is negative, the result of your calculation is negative or the calculation is a float return "No solutions" (no valid cases), or [-1, -1] in COBOL.

In the form:

(Heads, Legs) = (72, 200)

VALID - (72, 200) =>             (44 , 28) 
                             (Chickens, Cows)

INVALID - (72, 201) => "No solutions"
However, if 0 heads and 0 legs are given always return [0, 0] since zero heads must give zero animals.

There are many different ways to solve this, but they all give the same answer.

You will only be given integers types - however negative values (edge cases) will be given.

Happy coding!
"""

def animals(heads, legs):
    #return (Chickens, Cows)\
    if heads%2 == 0:
        cows = ((legs - (2*heads))/2)
        chickens = (heads - cows)
        if cows >= 0 and chickens >= 0 and cows%1 == 0:
            return (int(chickens), int(cows))
        
    return "No solutions"
    #or
    if heads < 0 or legs < 0:
        return "No solutions"
    
    max_cows = heads
    if heads * 4 < legs:
        max_cows = heads -((legs - heads * 2) // 2)
    
    for cows in range(max_cows + 1):
        chickens = heads - cows
        if cows * 4 + chickens * 2 == legs:
            return (chickens, cows)
    return "No solutions"

print(animals(72, 200), (44, 28))
print(animals(116, 282), (91, 25))
print(animals(12, 24), (12, 0))
print(animals(6, 24), (0, 6))
print(animals(344, 872), (252, 92))
print(animals(158, 616), (8, 150))
print(animals(25, 555), "No solutions")
print(animals(12, 25), "No solutions")
print(animals(54, 956), "No solutions")
print(animals(5455, 54956), "No solutions")
print(animals(0, 0), (0, 0))
print(animals(-1, -1), "No solutions")
print(animals(500, 0), "No solutions")
print(animals(0, 500), "No solutions")
print(animals(-45, 5), "No solutions")
print(animals(5, -55), "No solutions")
print(animals(91, 344), "No solutions")
print(animals(341, 960), "No solutions")
print(animals(253, 572), "No solutions")