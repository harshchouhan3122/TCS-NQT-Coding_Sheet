# Important

'''
Find all Symmetric Pairs in the array of pairs


5

0
In this article, we will solve the problem: "Find all Symmetric Pairs in the array of pairs"

Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.

Examples:

Example 1:
Input: (1,2),(2,1),(3,4),(4,5),(5,4)
Output: (2,1) (5,4)
Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.

Example 2:
Input: (1,5),(2,3),(4,2),(5,1),(2,4)
Output: (2,4) (5,1)
Explanation: Since (1,5) and (2,4) are symmetric pairs and (5,1) and (4,2) are symmetric pairs.
'''

# def symmetricPairs(pairs):
#     pairs = pairs[::-1]
#     res = []
#     for i in pairs:
#         check = (i[1],i[0])
#         if check in pairs and check not in res:
#            res.insert(0, i) 
#     return res


def symmetricPairs(pairs):
    res = []
    for i in pairs:
        if (i[1],i[0]) in pairs and i not in res:
            res.append((i[1],i[0]))
    return res


inp_pairs = [(1,2),(2,1),(3,4),(4,5),(5,4)]     # (2,1) (5,4)
print(symmetricPairs(inp_pairs))

inp_pairs = [(1,5),(2,3),(4,2),(5,1),(2,4)]     # (5,1) (2,4)
print(symmetricPairs(inp_pairs))