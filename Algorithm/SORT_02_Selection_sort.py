"""
Selection Sort is based on the Minimum value moving to the First Index
"""

numbers = [2,5,1,3,4]
minimum = numbers[0]
for i in range(1,len(numbers)):
    if minimum > numbers[i]:
        minimum = numbers[i]
        

