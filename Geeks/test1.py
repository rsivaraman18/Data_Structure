"""
Smallest Positive Integer
"""

# def missingNumber(arr):
#     big = max(arr)
#     for element in arr:
#         if (element>big): 
#             big = element

#     for number in range(1,big+1):
#         if number not in arr:
#             return number
#             break
#     else:return(big+1)





def missingNumber(arr):
    n = len(arr)
    
    # Step 1: Move all numbers out of range [1, n] to be ignored
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = n + 1  # Set irrelevant numbers to a value greater than n
    
    # Step 2: Mark indices for present numbers
    for i in range(n):
        num = abs(arr[i])  # Work with absolute value in case it's already marked
        if num <= n:
            arr[num - 1] = -abs(arr[num - 1])  # Mark presence by setting negative
    
    # Step 3: Find the first positive index
    for i in range(n):
        if arr[i] > 0:  # Positive value means index+1 is missing
            return i + 1
    
    # If no missing number in range [1, n], return n+1
    return n + 1


    

        
        
print(missingNumber([2, -3, 4, 1, 1, 7]))  # 3
print(missingNumber([5, 3, 2, 5, 1]))   # 4 
print(missingNumber([-8, 0, -1, -4, -3])) # 1

print(missingNumber([1 ,2, 3, 4, 5]))  ### 6
print(missingNumber([2 ,6 ,2 ,-8, -7 ,8]))  #1