
'''
import math

a = 4.7

print(f"a = {a}")
print(f"int(), a = {int(a)}")
print(f"ceil(), a = {math.ceil(a)}")

# check perfact square if .ciel() is not allowed
def perfectSquare(num):
    res = num**0.5
    # if int(res) == math.ceil(res):
    if res == int(res):
        return True
    return False

num = 9
print(perfectSquare(num))
num = 10
print(perfectSquare(num))
'''


# print([1,2,3,_,_,_,_])



