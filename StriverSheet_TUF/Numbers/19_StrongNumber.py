

'''
Check if a number is a Strong Number or not


0

0
Problem Statement: Given an integer Print “YES” if it is a strong number else print “NO”.

Note : 

When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 
Strong number is also known as Krishnamurthi number/Peterson Number.
Examples:

Examples 1:
Input: N = 145
Output: Yes
Explanation: 1! + 4! + 5! = 145. Hence 145 is a strong number. 

Example 2:
Input:  26
Output: No
Explanation: 2! + 6! = 722. Hence 26 is not a strong number.
'''

# Strong number is also known as Krishnamurthi number/Peterson Number.

# O(n*m)
def isStrong(num):
    
    def fact(n):
        if n==1:
            return n
        return n*fact(n-1)

    org = num
    res = 0

    while(num>0):
        res += fact(num%10)
        num //= 10
    
    return (org==res)

N = 145
# Output: Yes 
print(isStrong(N))

N = 26
# Output: No
print(isStrong(N))