"""
Majority Element

prgm1 : 
Input: arr[] = [3, 1, 3, 3, 2]
Output: 3

Input: arr[] = [7]
Output: 7

Input: arr[] = [2, 13]
Output: -1
"""

def majorityElement(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    d = {}
    for element in arr:
        d[element] = d.get(element, 0) + 1

    for key, value in d.items():
        if value > n // 2:  # Check if frequency is greater than n/2
            return key

    return -1   
  




# print(majorityElement([3, 1, 3, 3, 2]))
# print(majorityElement( [7]))
# print(majorityElement([2, 13]))

print(majorityElement([6 ,1 ,15, 19, 9 ,13, 12, 6 ,7 ,2 ,10, 4, 1 ,14 ,11, 14, 14 ,13
]))
