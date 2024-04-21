# Very Important

'''
Find GCD of two numbers


13

0
Problem Statement: Find the gcd of two numbers.

Examples
Example 1:
Input:
 num1 = 4, num2 = 8
Output:
 4
Explanation:
 Since 4 is the greatest number which divides both num1 and num2.

Example 2:
Input:
 num1 = 3, num2 = 6
Output:
 3
Explanation:
 Since 3 is the greatest number which divides both num1 and num2.
 '''

# using Euclidean's Theorem / using recursion
def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)


def gcd(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if (num1%i==0 and num2%i==0):
            return i
    return 1


num1, num2 = 4, 8
# Output : 4
print(gcd(num1, num2))

num1, num2 = 3, 6
# Output : 3
print(gcd(num1, num2))