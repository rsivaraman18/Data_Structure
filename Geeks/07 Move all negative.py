"""
pgm 1:
Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
Output : [1, 3, 2, 11, 6, -1, -7, -5]

pgm2:
Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
Output : [7, 9, 10, 11, -5, -3, -4, -1]
"""

def segregateElements(arr):
    neg_array = []
    pos_array = []

    for element in arr:
        if element >=0:
            pos_array.append(element)
        else:
            neg_array.append(element)
    for i in range(len(pos_array)):
        arr[i] = pos_array[i]
    for i in range(len(neg_array)):
        arr[len(pos_array) + i] = neg_array[i]

print(segregateElements([1, -1, 3, 2, -7, -5, 11, 6 ]))
print(segregateElements( [-5, 7, -3, -4, 9, 10, -1, 11]))


