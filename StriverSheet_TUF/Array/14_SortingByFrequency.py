# Most Important

'''
Sort Elements of an Array by Frequency


3

1
Sort Elements of an Array by Frequency

Problem Statement: Given an array of integers, having some duplicate elements, sort the array by frequency.

Examples:

Example 1:
Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
Output: 2 2 2 1 1 3 3 4 
Explanation: Since  2 is present 3 times in an array , so print it 3 times ,then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.

Example 2:
Input: N = 6, array[] = {-199,6,7,-199,3,5}
Output: -199 -199 3 5 6 7
Explanation: Since -199 is present 2 times so it will be printed at first , then 3 , 5 ,6 ,7 are present once in array , so print them in their sorted order.
'''

# Also can be solved by dictionary 

def sortByFreq(arr):

    setArr = list(set(arr))

    for i in range(len(setArr)):
        setArr[i] = [setArr[i], arr.count(setArr[i])]
    
    setArr = sorted(setArr, key = lambda x:x[1], reverse=True)

    res = []

    for i in setArr:
        for j in range(i[1]):
            res.append(i[0])
    
    return res


arr = [1,2,3,2,4,3,1,2]     # 2 2 2 1 1 3 3 4 
print(sortByFreq(arr))

arr = [-199,6,7,-199,3,5]   # -199 -199 3 5 6 7
print(sortByFreq(arr))