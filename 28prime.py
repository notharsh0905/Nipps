#Write a program to print whether a given number is prime number or not
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


'''import math

num = int(input("Enter a number: "))

if num <= 1:
    print("Not prime")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")'''