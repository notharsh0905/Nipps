#Write a program that will give you the sum of 3 digits
num = int(input("Enter the number: "))
total = 0
for i in range(3):
    digit =num %10
    total = total+digit
    num=num//10

print("The sum is:", total)