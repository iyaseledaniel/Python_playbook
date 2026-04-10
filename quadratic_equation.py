# Program to find the roots of quadratic equation
# User needs to input the coefficients a,b,c of the quadratic expression ax^2 + bx +c
# e.g 3x^2 - 4x + 5 will have coefficients a=+3, b = -4 and c= +5
import math

#Ask user for input for coefficients a,b,c
a = int(input("Enter the value for a : "))
b = int(input("Enter the value for b : "))
c = int(input("Enter the value for c : "))

if (b**2 - 4*a*c ) > 0:
    #Test for distinct roots
    root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("root1 =", root1)
    print("root2 =", root2)
elif (b**2 - 4*a*c) == 0:
    #Test for equal roots
    root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    root2 = root1
    print("root1 =", root1)
    print("root2 =", root2)
else:
    print("Complex root")
    # root1 = (-b + complex(math.sqrt(b**2 - 4*a*c)))/(2*a)
    # root2 = (-b - complex(math.sqrt(b**2 - 4*a*c)))/(2*a)
    # print("root1 =", root1)
    # print("root2 =", root2)