'''
Reverse a given Array


10

0
Problem Statement: You are given an array. The task is to reverse the array and print it. 

Examples:

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.'''

def reverse1(arr):
    return arr[::-1]

def reverse2(arr):
    i, j = 0, len(arr)-1
    while(i<j):
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i+1, j-1
    return arr

# def reverse3(arr):
#     arr.reverse()   # not works on integer array
#     return arr


# arr = list(map(int, input().split(" ")))

arr = [1,2,4,7,7,5]
print(reverse1(arr))
print(reverse2(arr))
# print(reverse3(arr))

arr = [10,20,30,40]
print(reverse1(arr))

