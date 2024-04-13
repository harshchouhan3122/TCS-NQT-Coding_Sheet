# Important

'''
Count frequency of each element in the array


11

0
Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Examples:

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	 5  2
        15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	3  1
        4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array

'''

# O(N^2)
def countFreq(arr):
    n = len(arr)
    visited = [False] * n
    for i in range(n):
        if (visited[i] == True):
            continue
        count = 1
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        print(arr[i], count)

# using dictionary  O(N)
def countFrequency1(arr):
    freq = {}

    for i in arr:
        if i not in freq:
            freq[i] = 1
            continue
        freq[i] += 1
    
    # for i in freq:
    #     print(f"{i} -> {freq[i]}")

    return freq

# using set     O(N)
def countFrequency2(arr):
    setArr = list(set(arr))
    for i in range(len(setArr)):
        setArr[i] = [setArr[i], arr.count(setArr[i])]
    return setArr



arr = [10,5,10,15,10,5]
# print(countFreq(arr))
print(countFrequency1(arr))
# print(countFrequency2(arr))


print()

arr = [2,2,3,4,4,2]
# print(countFreq(arr))
# print(countFrequency1(arr))
print(countFrequency2(arr))

