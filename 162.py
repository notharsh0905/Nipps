#Implement a function to solve the FizzBuzz problem up to n.
#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz" instead of the number.
#For multiples of both 3 and 5, print "FizzBuzz".
#Example: n = 15 -> 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

n = int(input("Enter n: "))
print(f"FizzBuzz: {fizz_buzz(n)}")