# Largest Element in Array
# arr = [1, 8, 7, 56, 90]
# Output: 90
  
def largest(arr) :
    max_number = arr[0]
    for number in arr:
        if number > max_number:
            max_number = number
    print('Largest:',max_number)
    return max_number


largest( [1, 8, 7, 56, 90])  # output 90
largest( [5, 5, 5, 5])  # output 5
largest([10])  # output 10
