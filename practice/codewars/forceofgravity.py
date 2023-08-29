""" 
Your job is to find the gravitational force between two spherical objects (obj1 , obj2).

input
Two arrays are given :

arr_val (value array), consists of 3 elements
1st element : mass of obj 1
2nd element : mass of obj 2
3rd element : distance between their centers
arr_unit (unit array), consists of 3 elements
1st element : unit for mass of obj 1
2nd element : unit for mass of obj 2
3rd element : unit for distance between their centers
mass units are :

kilogram (kg)
gram (g)
milligram (mg)
microgram (μg)
pound (lb)
distance units are :

meter (m)
centimeter (cm)
millimeter (mm)
micrometer (μm)
feet (ft)
Note
value of G = 6.67 × 10−11 N⋅kg−2⋅m2

1 ft = 0.3048 m

1 lb = 0.453592 kg

return value must be Newton for force (obviously)

μ copy this from here to use it in your solution
"""

def solution(arr_val, arr_unit) :
    # your code goes here
    pass
    
    
print(solution([1000, 1000, 100], ["g", "kg", "m"]), 6.67e-12)
print(solution([1000, 1000, 100], ["kg", "kg", "m"]), 6.667e-9)
print(solution([1000, 1000, 100], ["kg", "kg", "cm"]), 0.0000667)