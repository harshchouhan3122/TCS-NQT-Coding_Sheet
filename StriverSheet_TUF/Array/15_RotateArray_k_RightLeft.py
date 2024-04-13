# Most Important

'''
Rotate array by K elements


26

0
Rotate array by K elements

Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Examples:

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.
'''

def rotateArray(arr, k, direction):
    n = len(arr)
    k %= n

    if direction == 'right':
        return arr[n-k:] + arr[:n-k]

    elif direction == 'left':
        return arr[k:] + arr[:k]

arr, k, direction = [1,2,3,4,5,6,7], 2, 'right'
# Output: 6 7 1 2 3 4 5
print(rotateArray(arr, k, direction))

arr, k, direction = [3,7,8,9,10,11], 3, 'left'
# Output: 9 10 11 3 7 8
print(rotateArray(arr, k, direction))