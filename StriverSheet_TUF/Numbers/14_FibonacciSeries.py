# Important

'''
Print Fibonacci Series up to Nth term


1

0
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Examples:

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)
'''

# Using Recursion (nth term of the fibonacci series)
# def fibonacciSeries(n):
#     if n <= 1:
#         return n
#     return fibonacciSeries(n-1)+fibonacciSeries(n-2)


def fibonacciSeries(n):
    if n > 0:
        series = [0, 1]
        if n < 2:
            return series[:n+1]
        for i in range(n-1):
            series.append(series[-2]+series[-1])
        return series


N = 5
# Output: 0 1 1 2 3 5
print(fibonacciSeries(N))

N =  6
# Output: 0 1 1 2 3 5 8
print(fibonacciSeries(N))