

'''
Check if a number is Palindrome or Not


7

0
Problem Statement:  Given a number check if it is a palindrome.

An integer is considered a palindrome when it reads the same backward as forward.

Examples:

Example 1:
Input: N = 123
Output: Not Palindrome Number
Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

Example 2:
Input: N =  121 
Output: Palindrome Number
Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.
'''

def isPalindrome(num):
    org = num
    rev = 0
    while(num>0):
        rev = rev*10 + num%10
        num //= 10
    return (org == rev)



num = 123
print(isPalindrome(num))

num = 1234321
print(isPalindrome(num))