

'''
Reverse a given String
'''

def reverse(str):
    return str[::-1]

# using Two Pointer Approach
def reverse(str):
    i, j = 0, len(str)-1
    str = list(str)
    while(i<j):
        str[i], str[j] = str[j], str[i]
        i, j = i+1, j-1
    str = "".join(str)
    return str

# using Stack
def reverse(str):
    revString = ""
    stack = []
    for i in str:
        stack.append(i)
    while(len(stack)!=0):
        revString += stack.pop()
    return revString

# using queue
from collections import deque
def reverse(string):
    queue = deque()
    for char in string:
        # queue.appendleft(char)
        queue.append(char)
        print(queue)
    
    reversed_string = ''
    while queue:
        reversed_string += queue.pop()

    return reversed_string


string = "Hello Guys"
print(reverse(string))