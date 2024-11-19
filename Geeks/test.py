"""
Given an array arr of integers, find all the elements that occur more than once in the array. Return the result in ascending order. If no element repeats, return an empty array.
pgm1:
Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.

pgm2:
Input: arr[] = [0, 3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty.

Input: arr[] = [2]
Output: [] 
Explanation: There is single element in the array. Therefore output is empty.
"""

def findDuplicates(arr):
    duplicates = []
    for element in arr:
        if arr.count(element)>1 and element not in duplicates:
            duplicates.append(element)
    return duplicates

            
        

    


print(findDuplicates([2, 3, 1, 2, 3]) ) 
print(findDuplicates([0, 3, 1, 2] ) ) 
print(findDuplicates([2]) ) 

3 1 0 4 2 3 1