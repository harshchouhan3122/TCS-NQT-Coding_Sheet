# Important


'''
Program to find Sum of GP Series


0

0
Problem Statement: Given a geometric Progression (G.P) sequence with some inputs as:-

a, first term
r, common ratio
n, number of terms
 Write a program to find the sum of the geometric Progression Series.

Examples:

Example 1:
Input: a=1 , r=0.5 , n=3
Output: 1.75
Explanation: The sum of given GP Series is 1.75

Example 2:
Input: a=3 , r=5 , n=2
Output: 18
Explanation: The sum of the given GP Series is 18
'''

# Sum of first n terms of GP : a*(r**n -1)/(r-1)

# GP -> a ar^1 ar^2 ar^3 .... ar^(n-1)

# Using Loop
def sumOfGP(a,r,n):
    res = 0
    for i in range(n):
        res += a*r**i
    return res


# Using GP formula
def sumOfGP2(a,r,n):
    res = a*(r**n -1)/(r-1)
    return res




a, r, n = 1, 0.5, 3
# Output: 1.75
print(sumOfGP(a, r, n))
print(sumOfGP2(a, r, n))

a, r, n = 3, 5, 2
# Output: 18
print(sumOfGP(a, r, n))
print(sumOfGP2(a, r, n))


# a, r, n = map(int, input().split(" "))