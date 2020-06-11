# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 05:30:45 2019

@author: Medhavi
"""


from random import randint 

def getRandom(x, y): 
	return randint(x,y) 

# A iterative randomized binary search function. 
# It returns location of x in 
# given array arr[l..r] if present, otherwise -1 
def randomizedBinarySearch(arr, l, r, x):
    while (l <= r):
        m = getRandom(l, r)
        if (arr[m] == x):
            return m
        elif (arr[m] < x):
            mid = int((m + r)/2)            
        else:
            mid = int((l+m)/2)
        if (arr[mid] == x):
            return mid
        elif (arr[mid] < x):
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Driver code 
arr = [2, 3, 4, 10, 40] 
n = len(arr) 
x =2
result = randomizedBinarySearch(arr, 0, n-1, x) 
if result == 1: 
	print("Element is not present in array") 
else: 
	print("Element is present at index", result) 

# This code is contributed by ankush_953 

l1 = ["sad","happy","hell","boy"]
l2 = [1,2,3,4]
print(l1)
print(l2)
l3 =  list(zip(l1,l2))


print(l3)
sec = lambda val : val[1]
l3.sort(key = sec,reverse=True)

print(l3)
