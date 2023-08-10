"""m 
Given a sequence of items and a specific item in that sequence, return the item immediately following the item specified. If the item occurs more than once in a sequence, return the item after the first occurence. This should work for a sequence of any type.

When the item isn't present or nothing follows it, the function should return nil in Clojure and Elixir, Nothing in Haskell, undefined in JavaScript, None in Python.

next_item([1, 2, 3, 4, 5, 6, 7], 3) # => 4
next_item(['Joe', 'Bob', 'Sally'], 'Bob') # => "Sally"
"""

def next_item(xs, item):
    
    xs_list = list(xs)
    # print(xs_list)
    for i in range(len(xs_list)):
        if xs_list[i] == item:
            if i + 1 < len(xs_list):
                return xs_list[i + 1]
            else:
                return None  # Return None when the item is the last element in the list
    return None  # Return None if the item is not found in the list

    
    
print(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)
print(next_item(['a', 'b', 'c'], 'd'), None)
print(next_item(['a', 'b', 'c'], 'c'), None)
print(next_item('testing', 't'), 'e')
print(next_item(iter(range(1, 30000)), 12), 13)