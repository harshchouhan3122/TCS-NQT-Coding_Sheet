# Important


'''
Check if a number is prime or not


8

0
Problem Statement: Given a number, check whether it is prime or not. A prime number is a natural number that is only divisible by 1 and by itself.

Examples 1 2 3 5 7 11 13 17 19 …

Examples
Example 1:
Input:
 N = 3
Output:
 Prime
Explanation:
 3 is a prime number

Example 2:
Input:
 N = 26
Output:
 Non-Prime
Explanation:
 26 is not prime
 '''


# Prime -> factors are 1 & itself

def isPrime(num):
    if num < 2:
        return False

    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False

    return True



num = 3
print(isPrime(num))

num = 26
print(isPrime(num))

num = 29
print(isPrime(num))