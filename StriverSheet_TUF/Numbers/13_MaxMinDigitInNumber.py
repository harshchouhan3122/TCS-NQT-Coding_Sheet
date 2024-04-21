
'''
Maximum and Minimum Digit in a Number


1

0
Problem Statement: Given a number N, print the smallest and largest digits present in the number.

Examples:

Example 1:
Input: N = 2746
Output: Largest digit: 7
        Smallest digit: 2
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.

Example 2:
Input: N = 23004
Output: Largest digit : 4
        Smallest digit : 0
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.
'''

def minMaxDigit(N):
    largest = -float('inf')
    smallest = float('inf')

    while(N>0):
        digit = N % 10
        N //= 10

        largest = max(largest, digit)
        smallest = min(smallest, digit)
    
    print(f"Largest digit: {largest}")
    print(f"Smallest digit: {smallest}")

    return ""


N = 2746
# Output: Largest digit: 7
#         Smallest digit: 2
print(minMaxDigit(N))

N = 23004
# Output: Largest digit : 4
#         Smallest digit : 0
print(minMaxDigit(N))
