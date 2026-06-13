#Take a number from the user and find the number of digits in it.
n = int(input("Enter the number: "))

count = 0

while n > 0:
    n = n // 10
    count += 1

print("Number of digits:", count)