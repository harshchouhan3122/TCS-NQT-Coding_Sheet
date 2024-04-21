
# Important

'''
Calculate the Power of a Number : Binary Exponentiation


3

0
Problem Statement: Find the Power of a number.

Examples:

Example 1:
Input: N = 5, k=3
Output: 125
Explanation: Since 5*5*5 is 125.

Example 2:
Input: n=2 k=4
Output: 16
Explanation: Since 2*2*2*2 is 16
'''

# import math
# def power(n,k):
#     return int(math.pow(n,k))

# using exponent operator
def power(n, k):
    return n**k

# using Loop    O(k)
def power(n, k):
    ans = 1
    for i in range(k):
        ans *= n
    return ans

# O(logn)
def power(n, k):
    ans = 1
    while(k!=0):
        if (k%2==0):
            n = n*n
            k /= 2
        else:
            ans = ans * n
            k -= 1
    return ans


n, k = 2, 4
print(power(n,k))

n, k = 5, 3
print(power(n,k))

