'''
Find all Palindrome Numbers in a given range


3

0
Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

Note: A palindromic number is a number that remains the same when its digits are reversed.OR  a palindrome is a number that reads the same forward and backward Eg: 121,1221, 2552

Examples:

Example 1:
Input: min = 10 , max = 50
Output: 11 22 33 44 
Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.

Example2:
Input: min = 100 , max = 150
Output: 101 111 121 131 141 
Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.'''

def isPalindrome(num):
    org = num
    rev = 0
    while(num>0):
        rev = rev*10 + num%10
        num //= 10
    return (org == rev)


def getPalindrome(num1, num2):
    res = []
    for num in range(num1, num2):
        if isPalindrome(num):
            res.append(num)
    return res

min, max = 10 , 50
# Output: 11 22 33 44 
print(getPalindrome(min, max))

min , max = 100 , 150
# Output: 101 111 121 131 141 
print(getPalindrome(min, max))