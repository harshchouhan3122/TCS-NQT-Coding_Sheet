
'''
Greatest of three numbers


1

0
Problem Statement: Given three numbers. Find the greatest of three numbers.

Examples:

Example 1:
Input: 1 3 5
Output: 5
Explanation: Answer is 5.Since 5 is greater than 1 and 3.

Example 2:
Input: 1.123  1.124 1.125
Output: 1.125
Explanation: Answer is 1.125. Since 1.125 is greater than 1.123 and 1.124
'''

def greatest(a, b, c):
    if a >= b:
        if a >= c:
            return a
        return c
    else:
        if b >= c:
            return b
        return c


a, b, c = map(float, "1 3 5".split(" ") ) 
a, b, c = map(float, "1 3 3".split(" ") ) 
# Output: 5
print(greatest(a, b, c))


a, b, c = map(float, "1.123 1.124 1.125".split(" ") ) 
# Output: 1.125
print(greatest(a, b, c))
