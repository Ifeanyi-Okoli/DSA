""" 
Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

Go on and code some pure awesomeness!
 """
 
def next_id(arr):
    #your code here
    unique_arr = set(arr)
    # print (unique_arr)
    i=0
    while i in unique_arr:
        i += 1
        # print(i)
    
    return i
print(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
print(next_id([5,4,3,2,1]), 0)
print(next_id([0,1,2,3,5]), 4)
print(next_id([0,0,0,0,0,0]), 1)
print(next_id([]), 0)
print(next_id([0,0,1,1,2,2]), 3)
print(next_id([0,1,1,1,3,2]), 4)
print(next_id([0,1,0,2,0,3]), 4)
print(next_id([9,8,0,1,7,6]), 2)
print(next_id([9,8,7,6,5,4]), 0)