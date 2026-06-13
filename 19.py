#Write a program that will take user input of (4 digits number) 
#and check whether the number is narcissist number or not.
#same as armstrong
num = int(input("Enter a number: "))

temp = num
n = len(str(num))   # number of digits
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10


if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

