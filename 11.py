#Write a program to find the simple interest when the value of principle,
#rate of interest and time period is given
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

si = (p * r * t) / 100

print("Simple Interest is:", si)