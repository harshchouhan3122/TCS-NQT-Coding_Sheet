

'''
Factors of a Given Number


1

0
Problem Statement: Find all factors of a number or find all distinct divisors of a natural number.

Examples:

Example 1:
Input: n = 6
Output: 1,2,3,6
Explanation: 6 is divisible by 1,2,3,6

Example 2:
Input: n = 9
Output: 1,3,9
Explanation: 9 is divisible by 1,3,9
'''

# using loop O(n)
def factors(num):
    fact = []
    for i in range(1,num+1):
        if (num%i == 0):
            fact.append(i)
    return fact

# using loop O(sqrt(n))
def factors(num):
    fact = [1, num]
    for i in range(2,int(num**0.5)+1):
        if (num%i == 0):
            fact.append(i)
            if (int(num/i)) not in fact:
                fact.append(int(num/i))
    fact = sorted(fact)
    return fact


n = 6
# Output: 1,2,3,6
print(factors(n))

n = 9
# Output: 1,3,9
print(factors(n))
