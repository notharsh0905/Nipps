#Given a positive integer, print its multiplication table up to 10 using a while loop.
#Example: 7 -> 7x1=7, 7x2=14, ... , 7x10=70

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1