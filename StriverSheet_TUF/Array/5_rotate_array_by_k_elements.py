# Important

'''
Rotate array by K elements : Block Swap Algorithm


7

0
In this article we will learn a very popular algorithm for "Rotate array by K elements : Block Swap Algorithm".

Problem Statement: Given an array of n size, rotate the array by k elements using the Block Swap Algorithm.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5} K=2
Output: {3,4,5,1,2}
Explanation: Rotate the array to right by 2 elements.

Example 2:
Input: N = 7, array[] = {1,2,3,4,5,6,7} K=3
Output: {4,5,6,7,1,2,3}
Explanation: Rotate the array to right by 3 elements.
'''

# using string slicing
def rotateArray(num, k):
    k = k%len(num)
    return num[k:] + num[:k]

# Block Swap Algorithm
# def rotateArray2(num, k):
#     n = len(num)
#     k %= n  # Calculate the effective rotation amount within the range of array length
#     if k == 0:
#         return num  # No rotation needed if k is 0

#     # Perform block swapping to achieve rotation
#     for i in range(1, k + 1):
#         temp = num[-i]  # Store the value of the last element in the current block
#         j = -i
#         while True:
#             next_idx = (j - k) % n  # Calculate the index of the next element in the current block
#             if next_idx == -i:  # Break if we've returned to the initial position of the block
#                 break
#             num[j] = num[next_idx]  # Swap the elements within the block
#             j = next_idx
#         num[j] = temp  # Place the stored value at its final position in the current block

#     return num


num, k = [1,2,3,4,5,6,7], 8     # 4,5,6,7,1,2,3
print(rotateArray(num, k))
# print(rotateArray2(num, k))

num, k = [1,2,3,4,5], 2         # 3,4,5,1,2 
print(rotateArray(num, k))
# print(rotateArray2(num, k))