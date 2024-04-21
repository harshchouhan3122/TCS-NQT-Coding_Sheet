# Important

'''
Check if given year is a leap year or not


1

0
In this post we will solve the problem "Check if given year is a leap year or not".

Problem Statement: Check if the given year is a leap year or not.

Examples:

Example 1:
Input: 1996
Output: Yes
Explanation: Since 1996 is a leap year answer is “Yes”.

Example 2:
Input: 2000
Output: Yes

Explanation: Since 2000 is a leap year answer is “Yes”.
'''
def isLeapYear(year):

    # if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    #     return True
    # return False

    if year % 400 == 0:
        return True
    
    year %= 100

    if year % 4 == 0:
        return True
    
    return False

year = 1996
# Output: Yes
print(isLeapYear(year))

year = 2000
# Output: Yes
print(isLeapYear(year))