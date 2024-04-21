


'''
Permutations in which N people can occupy R seats


1

0
Problem Statement: Find permutations in which n people can occupy r seats in a classroom.

Examples:

Example 1:
Input: N = 5, r = 3
Output: 60
Explanation: To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60.

Example 2:
Input: N=6,r = 4.
Output: 360
'''

def seatArrangement(n, r):

    def fact(num):
        if num==1:
            return num
        return num*fact(num-1)

    return int(fact(n)/fact(n-r))

n, r = 5, 3     # Output : 60
print(seatArrangement(n, r))

n, r = 6, 4     # Output : 360
print(seatArrangement(n, r))