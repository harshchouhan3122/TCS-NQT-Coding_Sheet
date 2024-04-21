
'''
Check if the number is an abundant number or not


0

0
Problem Statement: Check if the number is an abundant number or not.

Examples:

Example 1:
Input: 18
Output: Abundant Number
Explanation: Divisors of 18 are 1,2,3,6,9. 1+2+3+6+9=21, Since 21 is greater than 18, 18 is an abundant number.

Example 2:
Input: 21
Output: Not Abundant Number
Explanation:Divisors of 21 are 1,3,7. 1+3+7=11, Since 11 is smaller than 21, 11 is not an abundant number.
'''

def isAbundant(num):
    divisorSum = 1      # 1 is the factor of everynum

    for i in range(2, int(num**0.5)+1):
        if (num%i == 0):
            divisorSum += i
            if int(num/i) != i:
                divisorSum += int(num/i)
    
    return (divisorSum > num)



num = 18        # True
print(isAbundant(num))

num = 21        # False
print(isAbundant(num))