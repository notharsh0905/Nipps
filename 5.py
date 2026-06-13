#Write a program that will reverse a four digit number. Also it checks whether the reverse is true
num = int(input("Enter the number:"))
original = num
reverse = 0
for i in range(4):
    digit =num %10
    reverse = reverse*10 + digit
    num=num//10

print("The reversed number is:", reverse)
if original == reverse:
    print("It is TRUE (Palindrome)")
else:
    print("It is FALSE")