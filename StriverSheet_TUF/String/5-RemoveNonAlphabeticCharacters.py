

'''
Remove characters from a string except alphabets


0

0
Problem Statement: Write a program to remove all characters from a string except alphabets in a given string.

Examples:

Example 1:
Input: string str = "take12% *&u ^$#forward"
Output: takeuforward
Explanation:
Characters 1,2,%,*,&,^,$,# along with whitespaces are 
removed but the order of remaining alphabets is preserved.

Example 2:
Input: String str = "1.Python & 2.Java"
Output: PythonJava
Explanation: 
Characters 1.&2. along with whitespaces are removed 
but the order of remaining alphabets is preserved.
'''

def removeExtraChar(string):
    str2 = ""
    for char in string:
        if ("A" <= char and char <= "Z") or ("a" <= char and char <= "z"):
            str2 += char
    return str2

# Without using extra space
def removeExtraChar(string):
    i, n = 0, len(string)
    while( i<n):
        if not (("A" <= string[i] and string[i] <= "Z") or ("a" <= string[i] and string[i] <= "z")):
            string = string[:i] + string[i+1:]
            i -= 1
            n -= 1
        i+=1
        n = len(string)
     
    return string



str = "take12% *&u ^$#forward"
# Output: takeuforward
print(removeExtraChar(str))


str = "1.Python & 2.Java"
# Output: PythonJava
print(removeExtraChar(str))



