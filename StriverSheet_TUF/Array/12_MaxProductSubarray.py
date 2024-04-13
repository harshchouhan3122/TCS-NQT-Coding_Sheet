# Most Important

'''
Maximum Product Subarray in an Array


6

0
Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

Examples
Example 1:
Input:

 Nums = [1,2,3,4,5,0]
Output:

 120
Explanation:

 In the given array, we can see 1×2×3×4×5 gives maximum product value.


Example 2:
Input:
 Nums = [1,2,-3,0,-4,-5]
Output:

 20
Explanation:

 In the given array, we can see (-4)×(-5) gives maximum product value.
'''
# def maxProdSubarray(arr):

#     def product(nums):
#         prod = 1
#         for i in nums:
#             prod *= i
#         return prod

#     subArrays = []

#     res = -float('inf')

#     for i in range(len(arr)-1):
#         subArrays.append([arr[i]])
#         for j in range(i+1, len(arr)):
#             subArrays.append(arr[i:j+1])
#             res = max(res, product(arr[i:j+1]))
#     subArrays.append([arr[-1]])
#     # print(subArrays)
#     return res


def maxProdSubarray(arr):

    def product(nums):
        prod = 1
        for i in nums:
            prod *= i
        return prod

    res = -float('inf')

    for i in range(len(arr)-1):
        res = max(res, arr[i])
        for j in range(i+1, len(arr)):
            res = max(res, product(arr[i:j+1]))
            
    return res



Nums = [1,2,3,4,5,0]            # 120
print(maxProdSubarray(Nums))

Nums = [1,2,-3,0,-4,-5]         # 20
print(maxProdSubarray(Nums))