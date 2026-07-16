#Write a program that will take three digits from the user 
#and add the square of each digit.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
sum=0
sq1=num1*num1
sq2=num2*num2
sq3=num3*num3
sum=sq1+sq2+sq3
print("Sum is: ", sum)