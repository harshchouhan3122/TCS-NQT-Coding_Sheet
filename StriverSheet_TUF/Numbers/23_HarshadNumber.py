

'''
Check if the given number is Harshad(Or Niven) Number


0

0
Problem Statement: Check if the number is a Harshad(or Niven) number or not.

Examples:

Example 1:
Input: 378
Output: Yes it is a Harshad number.
Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

Example 2:
Input: 379
Output: No
 it is not a Harshad number.
Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number.

'''

def isHarshad(num):
    orgNum = num
    digitSum = 0

    while(num>0):
        digitSum += num%10
        num //= 10
    
    return (orgNum%digitSum==0)



num = 378   # True
print(isHarshad(num))

num = 379   # False
print(isHarshad(num))