
# Given an array arr, rotate the array by one position in clock-wise direction.
"""
Input: arr = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]

Input: arr = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]
"""

def rotate(arr):
    last_element = arr.pop()
    arr.insert(0,last_element)
    return arr




print(rotate([1, 2, 3, 4, 5]))
print(rotate([9, 8, 7, 6, 4, 2, 1, 3]))
