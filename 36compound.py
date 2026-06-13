#Write a program to find the compound interest 
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time (years): "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest:", ci)
print("Total Amount:", amount)