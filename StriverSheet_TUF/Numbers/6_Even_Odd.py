'''
Check whether a given number is even or odd


2

0
Problem Statement: Given a number n, check whether a given number is even or odd.

Examples:

Example 1:
Input: n=5
Output: odd
Explanation: 5 is not divisible by 2.
 
Example 2:  
Input: n=6
Output: even
Explanation: 6 is divisible by 2.
'''

# Using Arithmatic Operator
def isEven(num):
    if num%2==0:
        print(f"{num} is an Even Number.")
    else:
        print(f"{num} is an Odd Number.")
    return " "
    
# Using Bitwise Operator
def isEven2(num):
    if num&1 == 0:
        print(f"{num} is an Even Number.")
    else:
        print(f"{num} is an Odd Number.")
    return " "


num = 2
print(isEven(num))

num = 5
print(isEven(num))