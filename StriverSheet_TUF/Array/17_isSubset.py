'''
Check if array is subset of another array


4

0
Check if array is subset of another array.

Write a program to find whether an array is a subset of another array or not.

Given arr1[] and arr2[], we need to find whether arr1[] is a subset of arr2[]. An array is called a subset of another if all of its elements are present in the other array.

Note: Array elements are assumed to be unique.

Examples:

Example 1:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [2,4,3,1,7,5,15]
Output: arr1[] is a subset of arr2[]

Example 2:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [4,5,2]
Output: arr1[] is not a subset of arr2[]

Example 3:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [11,12,13,15,16]
Output: arr1[] is not a subset of arr2[]
'''

# using inbuilt function
# def isSubset(arr1, arr2):
#     arr1, arr2 = set(arr1), set(arr2)
#     return arr1.issubset(arr2)



# if we have to check for each other
# def isSubset(arr1, arr2):
#     arr1, arr2 = sorted(set(arr1)), sorted(set(arr2))
#     if len(arr1) < len(arr2):
#         for i in arr1:
#             if i not in arr2:
#                 return False
#         return True
#     else:
#         for i in arr2:
#             if i not in arr1:
#                 return False
#         return True



# if we have to check for arr1 only 
def isSubset(arr1, arr2):
    arr1, arr2 = sorted(set(arr1)), sorted(set(arr2))
    if len(arr1) > len(arr2):
        return False
    for i in arr1:
        if i not in arr2:
            return False
    return True

arr1= [1,2,2,3]     
arr2= [2,4,3,1]
print(isSubset(arr1, arr2))     # True

arr1= [1,3,4,5,2]
arr2= [2,4,3,1,7,5,15]
print(isSubset(arr1, arr2))     # True

arr1= [1,3,4,5,2]
arr2= [4,5,2]
print(isSubset(arr1, arr2))     # False

arr1= [1,3,4,5,2]
arr2= [11,12,13,15,16]
print(isSubset(arr1, arr2))     # False