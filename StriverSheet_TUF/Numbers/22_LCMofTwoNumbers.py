# Very Important

'''
Find LCM of two numbers


0

0
Problem Statement: Find lcm of two numbers.

Examples:

Example 1:
Input: num1 = 4,num2 = 8
Output: 8


Example 2:
Input: num1 = 3,num2 = 6
Output: 6

'''

# LCM = (a*b)/gcd(a,b)

def lcm(n1, n2):
    
    def gcd(a,b):
        if b==0:
            return a
        return gcd(b, a%b)
    
    return int((n1*n2)/gcd(n1,n2))


num1, num2 = 4, 8
print(lcm(num1, num2))      # 8

num1, num2 = 3, 6
print(lcm(num1, num2))      # 6