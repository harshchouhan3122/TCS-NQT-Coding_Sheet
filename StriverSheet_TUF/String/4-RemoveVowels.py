# Important (without using extra space)

'''
Remove all vowels from the String


4

0
Problem Statement: Given a String, write a program to remove vowels from a given String.

Examples:

Example 1:
Input: Str = “take u forward”
Output: tk  frwrd
Explanation: All vowels are removed from the given String.

Example 2:
Input: Str = “I am very happy today”
Output:  m vry happy tdy
Explanation: All vowels are removed from the given String.
'''


def removeVowels(string):
    vowels = set('aeiou')
    str2 = ""
    for char in string:
        if char.lower() in vowels:
            continue
        str2 += char
    str2 = " ".join(str2.split())       # remove extra white spaces
    return str2


# Without using any extra Space
def removeVowels(string):
    vowels = set('aeiou')
    i, n = 0, len(string)
    while( i < n ):
        if string[i].lower() in vowels:
            string = string[:i] + string[i+1:]
        i += 1
        n = len(string)
    string = " ".join(string.split())
    return string




Str = "take u forward"
# Output: tk  frwrd
print(removeVowels(Str))


Str = "I am very happy today"
# Output:  m vry hppy tdy
print(removeVowels(Str))