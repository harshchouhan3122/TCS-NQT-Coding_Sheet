# Important

'''
Find all repeating elements in an array


2

0
Problem Statement: Find all the repeating elements present in an array.

Examples:

Example 1:
Input: 
Arr[] = [1,1,2,3,4,4,5,2]
Output:
 1,2,4
Explanation:
 1,2 and 4 are the elements which are occurring more than once.

Example 2:
Input:
 Arr[] = [1,1,0]
Output:
 1
Explanation:
 Only 1 is occurring more than once in the given array.
 '''

# Hashmap / Dictionary -> O(n)
def getRepeatedElements(arr):

    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
            continue
        freq[i] += 1
    print("Repeated Elements:", end=" ")
    for i in freq:
        if freq[i] > 1:
            print(i, end=",") 
    return ""


def getNonRepeatedElements(arr):

    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
            continue
        freq[i] += 1
    print("Non Repeated Elements:", end=" ")
    for i in freq:
        if freq[i] == 1:
            print(i, end=",") 
    return ""

arr = [1,1,2,3,4,4,5,2]
print(getRepeatedElements(arr))

arr = [1,1,0]
print(getRepeatedElements(arr))

arr = [1,2,-1,1,3,1]
print(getNonRepeatedElements(arr))

arr = [1,2,3]
print(getNonRepeatedElements(arr))

