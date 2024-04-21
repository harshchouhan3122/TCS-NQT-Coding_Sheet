'''
Sum of first N Natural Numbers


6

0
Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

Examples:

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
'''

# Using Loop
def NaturalNumSum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

# Using AP
def NaturalNumSum2(n):
    res = n*(n+1)/2
    return int(res)

N = int(input("Enter any num: "))
print(NaturalNumSum(N))
print(NaturalNumSum2(N))
