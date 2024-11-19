"""Bubble Sort"""

numbers = [2,5,1,3,4]
print('Method1 : For Loop')
for i in range(0,len(numbers)-1):
    for j in range(0,len(numbers)-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1] , numbers[j]        
else:
    print('Sorted Array is,',numbers)




#### Method 2 : Using While Loop
while True:
    flag = True
    for i in range(0,len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            numbers[i],numbers[i+1] = numbers[i+1] , numbers[i]
            flag = False
    if flag == True:
        break
print("Sorted Number is ",numbers)

