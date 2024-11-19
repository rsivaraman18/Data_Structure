"""
Rearrang Numbers
pgm1: [9, 4, -2, -1, 5, 0, -5, -3, 2]
O/P:  [9, -2, 4, -1, 5, -5, 0, -3, 2]

pgm2: [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
O/P:  [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]

pgm3: [9, 5, -2, -1, 5, 0, -5, -3, 2]
O/P:  [9, -2, 5, -1, 5, -5, 0, -3, 2]
"""




def rearrange(arr):
    neg_array = []
    pos_array = []
    new_array = []

    for element in arr:
        if element >=0:
            pos_array.append(element)
        else:
            neg_array.append(element)
    maxi = len(pos_array) if len(pos_array) > len(neg_array) else len(neg_array)
    
    for i in range(maxi ):
        if len(pos_array) >i:
            new_array.append(pos_array[i])
        if len(neg_array) >i:
            new_array.append(neg_array[i])
    
    # Making changes to Original Array
    for i in range(len(arr)):
        arr[i] = new_array[i]
    return arr










print(rearrange([9, 4, -2, -1, 5, 0, -5, -3, 2]))
print(rearrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))
print(rearrange( [9, 5, -2, -1, 5, 0, -5, -3, 2]))















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
    dict = {}
    for i in range(len(arr)):
        array = arr[i]
        count = 0
        for element in array:
            if element ==1:
                count = count+1
        dict[i] = count
    print(dict)

    return 'Hii'


print(rowWithMax1s( [[0, 1, 1, 1],
               [0, 0, 1, 1],
               [1, 1, 1, 1],
               [0, 0, 0, 0]]))

# print(rowWithMax1s([[0, 0], 
#                [1, 1]]))
