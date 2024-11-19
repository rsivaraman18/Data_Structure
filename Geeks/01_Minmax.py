# Prg 1 : Minimum & Maximum in given array
# Input: arr = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000


def get_min_max( arr):
    min_index = 0
    max_index = 0
    for i in range(len(arr)):
        if arr[min_index] > arr[i]:
            min_index = i
        if arr[max_index] < arr[i]:
            max_index = i
    print(arr[min_index], arr[max_index])
    return arr[min_index], arr[max_index]  



get_min_max([3, 2, 1, 56, 10000, 167])