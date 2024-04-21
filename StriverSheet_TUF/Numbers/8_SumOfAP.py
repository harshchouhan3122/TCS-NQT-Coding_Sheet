# Important

'''
Find Sum of AP Series


0

0
Problem Statement: Given an A.P. Series, we need to find the sum of the Series.

a = first term of A.P.

d= common Difference of A.P.

n= Number of Terms in  A.P.

Examples:

Example 1:
Input:
n=4
a=2
d=2
Output: 20
Explanation: 2+4+6+8 = 20

Input:
n=8
a=2
d=5
Output: 124
Explanation: -2 +3 + 8 + 13 + 18 + 23 + 28 + 33 = 124
'''


'''
What is A.P. (Arithmetic Progression)?

A.P. is the series of terms having the first term as a and d, common difference. Every next term in the A.P. is greater than the previous term by d units.

Example - 

-2, 3 , 8 , 13 , 18 , 23 , 28 , 33

First term , a = - 2

Common Difference , d=5

Last term , an=33
'''

# Sum of AP
# sum = (n/2) (2a + (n-1)*d)

def sumOfAP(n, a, d):
    res = (n/2) * (2*a + (n-1)*d)
    return int(res)

# Using Loop
def sumOfAP2(n, a, d):
    res = 0
    for i in range(n):
        res += a
        # print(a, end=" ")
        a = a+d
    return int(res)

n=4
a=2
d=2
# Output: 20
print(sumOfAP(n, a, d))
print(sumOfAP2(n, a, d))


n=8
a= -2
d=5
# Output: 124
print(sumOfAP(n, a, d))
print(sumOfAP2(n, a, d))


# Taling Input in Single Line
# n, a, d = map(int, input().split(" "))
# print(n, a, d)