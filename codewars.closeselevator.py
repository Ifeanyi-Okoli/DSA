

def elevator(left, right, call):
    # Good Luck!
    if abs(call - left) < abs(call - right):
        return "left"
    else:
        return "right"
    
    
print(elevator(0, 1, 0), "left")
print(elevator(0, 1, 1), "right")
print(elevator(0, 1, 2), "right")
print(elevator(0, 0, 0), "right")
print(elevator(0, 2, 1), "right")