#Write a program to find the sum of first n numbers, where n will be provided by the user. 
#Eg if the user provides n=10 the output should be 55.
num = int(input("Enter the number: "))
total = num * (num + 1) // 2
print("Sum:", total)
