# Very Important

'''
Print all Prime Factors of the given number


0

0
Problem Statement: Given a number n. Print all Prime Factors of the given number n.

Examples:

Example 1:
Input: N = 12
Output: 2,2,3
Explanation: These are the prime factors of 12.

Example 2:
Input: N = 36
Output: 2,2,3,3
Explanation: These are the prime factors of 36.
'''


# def primeFactors(num):

#     def isPrime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n**0.5)+1):
#             if n%i==0:
#                 return False
#         return True

#     ans = []
#     for i in range(2,int(num**0.5)+1):
#         if num%i == 0:
#             if isPrime(i):
#                 ans.append(i)
#             if isPrime(int(num/i)):
#                 ans.append(int(num/i))
#     return sorted(ans)


# def primeFactors(n):
    # ans = []

    # i = 2
    # while(n>1):
    #     if (n%i == 0):
    #         while(n%i==0):
    #             ans.append(i)
    #             n /= i
    #     i += 1
    # return ans

def primeFactors(n):
    ans = []

    i = 2
    while(n>1 or i*i<=n):
        if (n%i == 0):
            while(n%i==0):
                ans.append(i)
                n /= i
        i += 1
    return ans


n = 12
print(primeFactors(n))

n = 36
print(primeFactors(n))

n = 60
print(primeFactors(n))