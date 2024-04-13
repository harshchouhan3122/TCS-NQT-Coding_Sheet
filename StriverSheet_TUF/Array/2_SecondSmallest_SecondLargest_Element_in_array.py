# Important


'''
Find Second Smallest and Second Largest Element in an array


31

0
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Examples
Example 1:
Input:
 [1,2,4,7,7,5]
Output:
 Second Smallest : 2
	Second Largest : 5
Explanation:
 The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input:
 [1]
Output:
 Second Smallest : -1
	Second Largest : -1
Explanation:
 Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.
 '''

# O(logN)
# def getElement(arr):
#     arr = list(set(arr))
#     arr = sorted(arr)

#     print(arr)
#     print(f"2nd Smallest -> {arr[1]} \n2nd Largest -> {arr[-2]}")
#     return ""

# O(N)
def getElement(arr):
    smallest = secondSmallest = float('inf')
    largest = secondLargest = -float('inf')

    for i in arr:
        smallest = min(smallest, i)
        largest = max(largest, i)
    
    for i in arr:
        if i > smallest and i < secondSmallest:
            secondSmallest = i
        elif i < largest and i > secondLargest:
            secondLargest = i

    print(f"2nd Smallest -> {secondSmallest} \n2nd Largest -> {secondLargest}")
    return ""

# arr = list(map(int, input().split(" ")))

arr = [1,2,4,7,7,5]
print(getElement(arr))