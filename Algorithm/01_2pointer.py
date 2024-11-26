"""
2 Pointer Algorithm: Two add two number to achieve Target number.
1.Only If all numbers are in sorted Order.
2.Pointer should not come to same position
3.Only 1 pointer should be moved once.
4.Left pointer should not cross the right pointer.
5.Time Complexity is O(n).
""" 
 
print('Prg 1: ')
""" Program 1: Target = 10 , numbers = [1,2,3,4,5,6] """

arr = [1,2,3,4,5,6]
target = 10
lp = 0
rp = len(arr)-1

while (lp<rp):
    total = arr[lp] + arr[rp]
    if total == target:
        print(f'Left Pointer  :{lp} Right Pinter :{rp}')
        print(f'Numbers are {arr[lp]} , {arr[rp]}  & target is {target}')
        break
    elif total<target:
        lp = lp+1
    elif total>target:
        rp = rp-1
else:
    print('Expected Match Not Found')




