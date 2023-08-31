""" 
Groups of characters decided to make a battle. Help them to figure out which group is more powerful. Create a function that will accept 2 strings and return the one who's stronger.

Rules:
Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26
Strings will consist of uppercase letters only
Only two groups to a fight.
Group whose total power (A + B + C + ...) is bigger wins.
If the powers are equal, it's a tie.
"""

def battle(x, y):
    #Let the battle begin!
    X = sum(ord(i) - 64 for i in x)
    Y = sum(ord(i) - 64 for i in y)
    return x if X > Y else y if Y > X else 'Tie!'

print(battle("AAA", "Z"), "Z", "Unfair fight!")
print(battle("ONE", "TWO"), "TWO", "Unfair fight!")
print(battle("ONE", "NEO"), "Tie!", "Unfair fight!")
print(battle("FOUR", "FIVE"), "FOUR", "Unfair fight!")