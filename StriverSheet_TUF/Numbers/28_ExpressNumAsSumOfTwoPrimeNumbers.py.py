# Important

'''
Express given number as Sum of Two Prime Numbers


1

1
Problem: Given a number n, express the number as a sum of 2 prime numbers.

Examples:

Example 1:
Input : N = 74
Output : True . 
Explanation: 74 can be expressed as 71 + 3 and both are prime numbers. 

Example 2:
Input : N = 11
Output : False. 
Explanation: 11 cannot be expressed as sum of two prime numbers.
'''

def solution(num):
    
    def isPrime(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n% i ==0:
                return False
        return True

    if num < 4:
        return False
    
    for i in range(2, (num//2)+1):
        num1 = i
        num2 = num - num1

        if (isPrime(num1) and isPrime(num2)):
            # print(num1, num2)
            return True

    return False


num = 74        # True
print(solution(num))

num = 11        # False
print(solution(num))
