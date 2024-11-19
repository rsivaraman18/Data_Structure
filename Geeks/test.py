"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
pgm1:
Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
"""

def sort012(arr):
    result = sorted(arr)
    return result


print(sort012([0, 1, 2, 0, 1, 2]))

print(sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
