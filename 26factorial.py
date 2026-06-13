#Write a program that can find the factorial of a given number provided by the user.
num = int(input("Enter a number: "))   

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial is:", fact)



#def factorial(n):
    #if n == 0 or n == 1:   # base case
        #return 1
    #else:
        #return n * factorial(n - 1)   # recursive call

#num = int(input("Enter a number: "))

#if num < 0:
    #print("Not defined")
#else:
    #print("Factorial is:", factorial(num))