# Very Important

'''
Remove brackets from an algebraic expression


0

0
In this article, we will solve the most asked interview question: “Remove brackets from an algebraic expression”

Problem Statement: 

Remove brackets from an algebraic expression

Write a program to remove brackets from an algebraic expression

Given an algebraic expression, we need to simplify the expression and remove the brackets.

Examples:

Example 1:
Input: “a+((b-c)+d)”
Output: “a+b-c+d”
Explanation: Removed all the brackets in the algebric expression.

Example 2:
Input: “(((a-b))+c)”
Output: “a-b+c”
'''

def removeBrackets(expression):
    str = ""
    for i in expression:
        if i == "(" or i == ")":
            continue
        str += i
    return str


# using dequeue
from collections import deque
def removeBrackets(expression):
    queue = deque()
    for i in expression:
        # queue.appendleft(char)
        if not (i=="(" or i==")"):
            queue.appendleft(i)
    
    exp =""
    while queue:
        exp += queue.pop()

    return exp


expression = "a+((b-c)+d)"
# Output : "a+b-c+d"
print(removeBrackets(expression))

expression = "(((a-b))+c)"
# Output : "a-b+c"
print(removeBrackets(expression))