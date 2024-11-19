"""
Smallest Positive Integer
"""

def missingNumber(arr):
    mini = 9999999
    for element in arr:
        if (element >=0) :
            
            if element < mini:
                mini = element
    return mini
    
            
        




print(missingNumber([2, -3, 4, 1, 1, 7]))
print(missingNumber([5, 3, 2, 5, 1]))
print(missingNumber([-8, 0, -1, -4, -3]))