"""
Selection Sort is based on the Minimum value moving to the First Index
"""

numbers = [2,5,1,3,4]


for position in range(0,len(numbers)):
    minindex = position
    for i in range(position,len(numbers)):
        if numbers[i] < numbers[minindex]:
            minindex = i
    numbers[minindex],numbers[position] = numbers[position],numbers[minindex]
print(numbers)


