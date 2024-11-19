# First and Second Smallests
"""
pgm1 :
    Input: arr[] = [2, 4, 3, 5, 6]
    Output: 2 3 
pgm2: 
    Input: arr[] = [1, 1, 1]
    Output: -1
"""

def minAnd2ndMin(arr):
    sarray = sorted(arr)
    if sarray[0] == sarray[1] :
        print(-1)
        return -1
    else:
        print(sarray[0], sarray[1]) 
        return sarray[0], sarray[1]  
    
minAnd2ndMin([2, 4, 3, 5, 6]) ## Output : -1
minAnd2ndMin([1, 1, 1])    ## Output : -1

minAnd2ndMin([2,2,2,2]) 


