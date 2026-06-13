#User will provide 2 numbers you have to find the HCF of those 2 numbers
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#while b != 0:
#    a, b = b, a % b

#print("HCF is:", a)

a = int(input())
b = int(input())

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF is:", hcf)

#keep min() in mind