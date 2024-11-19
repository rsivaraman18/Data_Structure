### Linear Search Algorithm
"""
Find the Index of the Number from a box using Linear Search
"""
numbers = [10,40,60,100,20,60]
x = 20

print('Method 1: Using Enumerate')

for index,number in enumerate(numbers):
    if number ==x:
        print('Index of Number is : ',index)
        break
else:
    print('Finding Number Not in given list')
print('******************')

print('Method 2: Using For Loop')

for i in range(len(numbers)):
    if numbers[i] == x:
        print('Index of Number is : ',i)
else:
    print('Finding Number Not in given list')
print('******************')