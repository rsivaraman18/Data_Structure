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

# def findDuplicates(arr):
#     frequenncy = {}
#     duplicates = []

#     for element in arr:
#         frequenncy[element] = frequenncy.get(element,0)+1
    

#     for key,value in frequenncy.items():
#         if frequenncy[key] >1:
#             duplicates.append(key)
#     return sorted(duplicates)


    
def findDuplicates(arr):
    from collections  import Counter
    frequency = Counter(arr)
    print(frequency)

    for key,                     in frequency:
        print(key)
        # if frequenncy[key] >1:
            



            
        

    


# print(findDuplicates([2, 3, 1, 2, 3]) ) 
# print(findDuplicates([0, 3, 1, 2] ) ) 
# print(findDuplicates([2]) ) 
print(findDuplicates( [3 ,1 ,0, 4, 2, 3, 1] ) )
