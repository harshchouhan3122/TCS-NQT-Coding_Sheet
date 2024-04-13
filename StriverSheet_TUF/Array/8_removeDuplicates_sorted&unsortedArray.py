# Important

# 1. From Sorted Array
'''
Remove Duplicates in-place from Sorted Array


20

0
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.

Examples
Example 1:
Input:
 arr[1,1,2,2,2,3,3]

Output:
 arr[1,2,3,_,_,_,_]

Explanation:
 Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Example 2:
Input:
 arr[1,1,1,2,2,3,3,3,3,4,4]

Output:
 arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation:
Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.
'''




# From an unsorted Array

'''
Remove Duplicates From an Unsorted Array


4

0
Problem Statement: Given an unsorted array, remove duplicates from the array.

Examples:

Example 1:
Input: arr[]={2,3,1,9,3,1,3,9}
Output:  {2,3,1,9}

Explanation: Removed all the duplicate elements

Example 2:
Input: arr[]={4,3,9,2,4,1,10,89,34}
Output: {3,4,9,2,1,10,34,89}
Explanation: Removed all the duplicate elements
'''

# For Sorted Array
def removeDuplicate(arr):
    unq = []
    blnk = []

    for i in range(len(arr)):
        if arr[i] not in unq:
            unq.append(arr[i])
        else:
            blnk.append("")

    return unq+blnk


# For unsorted Array
def removeDuplicate1(arr):
    unq = []
    for i in arr:
        if i not in unq:
            unq.append(i)
    return unq
    

# For sorted Array -> using Two Pointer Approach
def removeDuplicate(arr):
    pass


# For unsorted Array -> using dictionary / Hashmap
def removeDuplicate1(arr):
    pass


# From Sorted Array
arr = [1,1,2,2,2,3,3]           # [1,2,3,_,_,_,_]
print(removeDuplicate(arr))

arr = [1,1,1,2,2,3,3,3,3,4,4]   # [1,2,3,4,_,_,_,_,_,_,_]
print(removeDuplicate(arr))


# From an Unsorted Array
arr = [2,3,1,9,3,1,3,9]         # [2,3,1,9]
print(removeDuplicate1(arr))

arr = [4,3,9,2,4,1,10,89,34]    # [3,4,9,2,1,10,89,34]
print(removeDuplicate1(arr))

