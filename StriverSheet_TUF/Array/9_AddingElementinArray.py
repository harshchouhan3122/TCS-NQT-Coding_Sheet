# Important
# arr.insert(idx, ele)
# arr.append(ele)
# arr.pop(idx)
# arr.remove(ele)


'''
Adding Element in an Array


4

0
Problem Statement: Given an array of N integers, write a program to add an array element at the beginning, end, and at a specific position.

Example:
Input: N = 5, array[] = {1,2,3,4,5}
insertbeginning(6)
insertending(7)
insertatpos(8,4)
Output: 6,1,2,8,3,4,5,7
Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4
'''

nums = [1,2,3,4,5]
print(nums)

# Insert at the START
nums.insert(0, 6)
print(nums)

# Insert at the END
nums.append(7)
print(nums)

# Insert at particular POSITION
nums.insert(3,8)
print(nums)

nums.pop(3)
print(nums)

nums.remove(6)
print(nums)