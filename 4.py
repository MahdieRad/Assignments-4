from math import  sin, asin, cos, pi, sqrt


#Modele drje3 ==> x^3 + ax^2 + b x + c = 0

a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))
print((2 * (a**3)/27) - (a*b/3) + c)
A = b - ((a**2)/3)
B = (2 * (a**3)/27) - (a*b/3) + c
DEL= (B**2)/4 + ((A**3)/27)
print("A: ", str(A))
print("B: ", str(B))



if DEL <= 0.0001:
    DEL = 0
print("Delta: ", str(DEL))

if DEL > 0:
    x = (-1 * B/2 + float(sqrt(DEL)) ** (1/3)) + (-1 * B/2 - float(sqrt(DEL)) ** (1/3)) - (a/3)
    print("Result: " + str(x))
elif DEL == 0:
    X = -2 * ((B/2)**(1/3)) - (a/3)
    Y = (B/2) ** (1/3) - (a/3)
    Z = (B/2) ** (1/3) - (a/3)   
    print("X : " + str(X))
    print("Y : " + str(Y))
    print("Z: " + str(Z))
else:
    X = (2/sqrt(3)) * (sqrt(-1 * A)) * sin((1/3) * asin(3 * sqrt(3*B)/2 * (sqrt(-1 * A) **3)))  - a / 3
    Y = (2/sqrt(3)) * (sqrt(-1 * A)) * sin((1/3) * asin(3 * sqrt(3*B)/2 * (sqrt(-1 * A) **3)) + (pi/3)) - a / 3
    Z = (2/sqrt(3)) * (sqrt(-1 * A)) * sin((1/3) * asin(3 * sqrt(3*B)/2 * (sqrt(-1 * A) **3)) + (pi/3)) - a / 3  
    print("X:  " + str(X))
    print("Y: " + str(Y))
    print("Z: " + str(Z))
