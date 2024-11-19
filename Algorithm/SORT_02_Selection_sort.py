"""
Selection Sort is based on the Minimum value moving to the First Index
"""

numbers = [2,5,1,3,4]
minindex = 0

for i in range(0,len(numbers)):
    for j in range(1,len(numbers)):
        if numbers[minindex] > numbers[j]:
            minindex = j
    
    numbers[j],numbers[minindex] = numbers[minindex],numbers[j]
    print(numbers)


