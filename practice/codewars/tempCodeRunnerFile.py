def battle(x, y):
    #Let the battle begin!
    x = sum(ord(i) - 64 for i in x)
    y = sum(ord(i) - 64 for i in y)
    return x if x > y else y if y > x else 'Tie!'