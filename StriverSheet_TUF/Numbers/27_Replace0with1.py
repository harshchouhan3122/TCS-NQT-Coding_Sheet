# Important


'''
Example 1:
Input: N = 102003
Output: 112113
Explanation: The 2nd,4th and 5th position from left contain 0.The resultant integer has replaced the 0’s in those  positions with 1.

Example 2:
Input:  204
Output: 214
Explanation: The 2nd position from left contain 0. The resultant integer has replaced the 0 in that position with 1.

'''

# using String
def replace0_1(num):
    num = list(str(num))
    for i in range(len(num)):
        if num[i] == '0':
            num[i] = '1'
    num = "".join(num)
    return int(num)

# using Number only
def replace0_1(num):
    newNum = 0
    exp = 0
    while(num>0):
        digit = num%10
        if digit == 0:
            digit = 1
        newNum = newNum + digit*10**exp 
        exp += 1
        num //= 10
    return newNum


num = 102003    # 112113
print(replace0_1(num))

num = 204    # 214
print(replace0_1(num))