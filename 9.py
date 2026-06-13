#Write a program that take a user inputr of three angles 
#and will find out whether it can form a triangle or not
a= float(input("enter the angle 1: "))
b= float(input("enter the angle 2: "))
c= float(input("enter the angle 3: "))
if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("Can be a triangle")
else:
    print("Can not be a triangle")