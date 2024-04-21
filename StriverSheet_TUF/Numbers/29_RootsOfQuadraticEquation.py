# Very Important

'''
Program to Find Roots of a quadratic equation


0

0
Problem Statement: The standard form of a quadratic equation is:

ax2 + bx + c = 0, where a, b and c are real numbers and a != 0

You have given a, b, c of the equation, you have found the roots of the equation.

Examples:

Example 1:
Input: a = 1, b = -3, c = -10
Output: Roots are real and different, i.e(5 , -2).

Example2:

Input: a = 1, b = 1, c = 1
Output: Roots are complex, i.e-(-0.5+i1.732 , -0.5-i1.732).
'''

# root = (-b +- sqrt(b2-4ac)) / 2a

def roots(a, b, c):
    D = (b**2) - (4*a*c)

    if D < 0:
        D = -D

        real = (-b/(2*a))
        img =  round((D**0.5)/(2*a),2)

        root1 = str(real)+" + i"+str(img)
        root2 = str(real)+" - i"+str(img)
    
    else:

        root1 = str((-b+(D**0.5))/(2*a))
        root2 = str((-b-(D**0.5))/(2*a))

    return '('+root1+" , "+root2+')'

a, b, c = 1, 1, 1           # (-0.5 + i0.87 , -0.5 - i0.87)
print(roots(a, b, c))

a, b, c = 1, -3, -10        # (5 , -2)
print(roots(a, b, c))