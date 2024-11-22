
"""
Row with more Ones
prg1:
Input: arr[][] = [[0, 1, 1, 1],
               [0, 0, 1, 1],
               [1, 1, 1, 1],
               [0, 0, 0, 0]]
Output: 2
Explanation: Row 2 contains 4 1's.
"""

def rowWithMax1s(arr):
    d = {}
    for i in range(len(arr)):
        array = arr[i]
        count = 0
        for element in array:
            if element ==1:
                count = count+1
        d[i] = count

    
    maxi = -1
    row = 0
    for key,value in d.items():
        if d[key] > maxi: 
            maxi   = d[key] 
            row = key
    print('maxi',maxi)
    if maxi !=0:
        return row
    else:
        return -1
     


print(rowWithMax1s( [[0, 1, 1, 1],
               [0, 0, 1, 1],
               [1, 1, 1, 1],
               [0, 0, 0, 0]]))

print(rowWithMax1s([[0, 0], 
               [1, 1]]))

print(rowWithMax1s([[0],[0]]))
