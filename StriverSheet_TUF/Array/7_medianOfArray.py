'''
Find Median of the given Array


3

0
Problem Statement: Given an unsorted array, find the median of the given array.

Examples:

Example 1:
Input: [2,4,1,3,5]
Output: 3

Example 2:
Input: [2,5,1,7]
Output: 3.5
'''
def median(arr):
    n = len(arr)
    arr = sorted(arr)

    if (n%2==0):
        med = (arr[n//2]+arr[(n//2)-1])*0.5

    else:
        med = arr[n//2]

    return med

num = [2,4,1,3,5]
print(median(num))
# Output: 3


num = [2,5,1,7]
print(median(num))
# Output: 3.5
