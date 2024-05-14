# Important

'''
Find the ASCII value of a character


3

0
Problem Statement: Given a character, Find the ASCII value of the character.

Examples:

Example 1:
Input: c = ‘A’
Output: 65
Explanation: ASCII value of A is 65

Example 2:
Input: c = ‘e’
Output: 101
Explanation: ASCII value of e is 101
'''

def ascii(char):
    return ord(char)

def character(ascii):
    return chr(ascii)



c = "A"     # 65
print(ascii(c))
print(character(ascii(c)))


c = "e"     # 101
print(ascii(c))
print(character(ascii(c)))