'''
Reverse digits of a number


1

0
Problem Statement: Given an integer. Write a program to reverse digits of a number.

Examples:

Example 1:
Input: N = 472
Output: 274
Explanation: Reading the number from back to front, we see that the output should be 274

Example 2:
Input: N = 470
Output: 74
Explanation: Reading the number from back to front, we get 074. For an integer with no decimals, we know that leading zeros have no significance and therefore our answer should be 74
'''

def reverse(num):
    rev = 0
    while(num>0):
        rev = rev*10 + num%10
        num //= 10
    return rev


N = 472
# Output: 274
print(reverse(N))

N = 470
# Output: 74
print(reverse(N))