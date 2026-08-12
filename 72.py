#Given a number, print its multiplication table from 1 to 10.
#Example: 5 -> 5x1=5, 5x2=10, ... , 5x10=50

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")