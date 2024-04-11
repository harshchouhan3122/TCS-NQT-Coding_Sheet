'''
Problem Statement -

Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.

Constrains-

1<=N<=100

Example 1:

Input :

10  -> Integer

Output :

5    -> result- Integer

Explanation:

Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.
'''

# def toggle_bits(num):
#     # Toggle each bit using bitwise NOT (~) operator
#     toggled_num = ~num
    
#     # Mask the result to keep only the least significant bits
#     # (This is needed because the bitwise NOT operation in Python
#     # operates on an infinite number of bits)
#     # print(num.bit_length())
#     # print(1 << num.bit_length())
#     # print(toggled_num & (1 << num.bit_length()))
#     # print(toggled_num & (1 << num.bit_length())-1)
#     toggled_num &= (1 << num.bit_length()) - 1
    
#     return toggled_num

# def toggle_bits(num):
#     num = list(bin(num)[2:])
#     new = []
#     for i in num:
#         if i == '1': new.append('0')
#         elif i == '0' : new.append('1')
#     new = "".join(new)
#     return int(new, 2)


def toggle_bits(num):
    num = list(bin(num)[2:])
    for i in range(len(num)):
        if num[i] == '1': num[i] = '0'
        elif num[i] == '0' : num[i] = '1'
    num = "".join(num)
    return int(num, 2)


# Test the function
num = 10
toggled_num = toggle_bits(num)
# print("Original num:", num)
print("Toggled num:", toggled_num)




# print(~1)
# print(~0)




# num = "11211"
# print(num)
# print(num.replace('1','2').replace('2','1'))