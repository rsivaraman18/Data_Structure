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
    if len(arr) == 1:
        return arr[0]


    d = {}
    for element in arr:
        d[element] = d.get(element,0) + 1
    
    maxi = 0
    for key,value in d.items():
        if d[key] >maxi:
            maxi = d[key]

    if maxi != 0:
        print('mm',maxi)
        return maxi
    else:
        return -1 
    print(d)




print(majorityElement([3, 1, 3, 3, 2]))
print(majorityElement( [7]))
print(majorityElement([2, 13]))