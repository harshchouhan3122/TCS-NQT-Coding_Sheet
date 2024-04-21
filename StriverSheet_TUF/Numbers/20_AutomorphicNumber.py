# Important 

'''
Check if a number is Automorphic Number


1

0
Problem Statement: Given a number, check if it is automorphic or not. A number is called an Automorphic number if and only if its square ends in the same digits as the number itself.

Examples:

Example 1:
Input Format: N = 76
Result: Automorphic Number
Explanation: Calculating 76 * 76 gives 5776, it ends with the given number.

Input Format: 25
Result: Automorphic Number
Explanation: Calculating 25 * 25 gives 625, it ends with the given number.
'''

# using String
def isAutomorphic(num):
    check = num*num
    digits = len(str(num))
    return (str(check)[-digits:] == str(num))

# using num comparision
def isAutomorphic(num):
    sq = num*num
    while(num>0):
        if (num%10 != sq%10):
            return False
        num //= 10
        sq //= 10
    return True

N = 76  # True
print(isAutomorphic(N))

N = 25  # True
print(isAutomorphic(N))
