'''
Average of all the elements in the array


1

0
Problem Statement: Given an array, we have to find the average of all the elements in the array.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 3
Explanation: Average is the sum of all the elements divided by number of elements.Therefore (1+2+3+4+5)/5 = 3.

Example 2:
Input:  N=6, array[] = {1,2,1,1,5,1}
Output: 1.8
Explanation: Average is the sum of all the elements divided by number of elements.Therefore (1+2+1+1+5+1)/6 = 1.8
'''
def average(arr):
    n = len(arr)
    res = 0
    for i in arr:
        res += i
    res = res/n
    res = "{:.1f}".format(res)
    return res

arr = [1,2,3,4,5]
print(average(arr))

arr = [1,2,1,1,5,1]
print(average(arr))