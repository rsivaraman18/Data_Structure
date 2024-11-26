# First and Second Smallests
"""
pgm1 :
    Input: arr[] = [2, 4, 3, 5, 6]
    Output: 2 3 
pgm2: 
    Input: arr[] = [1, 1, 1]
    Output: -1
""" 
 
def minAnd2ndMin(arr):

    if len(arr) < 2:
        return -1, -1  # Return as a tuple to match expected output

    # Initialize the two smallest numbers
    first_min = second_min = float('inf')

    for num in arr:
        if num < first_min:
            second_min = first_min  # Update second smallest
            first_min = num  # Update smallest
        elif num > first_min and num < second_min:
            second_min = num  # Update second smallest if larger than first_min

    # If second_min is not updated, it means no second distinct minimum exists
    if second_min == float('inf'):
        return -1, -1

    return first_min, second_min
   


print(minAnd2ndMin([2, 4, 3, 5, 6]))
print(minAnd2ndMin([1, 1, 1]))
print(minAnd2ndMin([2,2,2,]))
