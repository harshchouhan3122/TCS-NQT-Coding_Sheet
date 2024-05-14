

'''
Check if the given String is Palindrome or not


10

0
Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.

Examples:

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.
'''

def isPalindrome(str1):
    return (str1 == str1[::-1])

Str =  "ABCDCBA"
# Output: Palindrome
print(isPalindrome(Str))

Str = "TAKE U FORWARD"
# Output: Not Palindrome
print(isPalindrome(Str))