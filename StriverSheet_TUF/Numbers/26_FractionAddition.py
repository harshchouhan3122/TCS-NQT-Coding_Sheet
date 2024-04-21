
# Very Very Important   (input from the user)

'''
Program to Add two fractions


0

0
Problem Statement: Adding two fractional numbers.

Examples:

Example 1:
Input: 3/4 + 1/7 
Output: 25/28
Explanation: Since 3/4 + 1/7 = 25/28

Example 2:
Input: 5/2 + 1/2
Output: 3/1
Explanation: Since 5/2 + 1/2 = 3/1

'''

def add(f1, f2):

    def gcd(a, b):
        if b ==0:
            return a
        return gcd(b, a%b)

    n1, d1 = map(int, f1.split("/"))
    n2, d2 = map(int, f2.split("/"))

    num = d1*n2 + d2*n1
    den = d1*d2

    num, den = int(num/gcd(num,den)), int(den/ gcd(num,den))

    return str(num)+"/"+str(den)


f1, f2 = map(str, input().split("+"))
print(add(f1, f2))