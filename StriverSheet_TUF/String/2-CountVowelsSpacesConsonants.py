# Important

'''
Count number of vowels, consonants, spaces in String


2

0
Problem Statement: Given a string, write a program to count the number of vowels, consonants, and spaces in that string.

Examples:

Example 1:
Input: string str=”Take u forward is Awesome”
Output: 
Vowels: 10
Consonants: 11
White spaces: 4
Explanation: 



Example 2:
Input: string str=”India won the cricket match”
Output:
Vowels: 8
Consonants: 15
White spaces: 4
'''

def countCharacters(str1):
    vowels = set('aeiou')
    countVowel, countSpace, countConst = 0, 0, 0

    for char in str1:
        if char.lower() in vowels:
            countVowel += 1 
        elif char == " ":
            countSpace += 1
        else:
            countConst += 1
    
    return (countVowel, countSpace, countConst)






str = "Take u forward is Awesome"
# Output: 
# Vowels: 10
# Consonants: 11
# White spaces: 4
# print(countCharacters(str))
print(f"Vowels: {countCharacters(str)[0]}") 
print(f"Consonants: {countCharacters(str)[2]}" )
print(f"White spaces: {countCharacters(str)[1]}") 

print("_______________")


str = "India won the cricket match"
# Output:
# Vowels: 8
# Consonants: 15
# White spaces: 4
# print(countCharacters(str))
print(f"Vowels: {countCharacters(str)[0]}") 
print(f"Consonants: {countCharacters(str)[2]}" )
print(f"White spaces: {countCharacters(str)[1]}") 