#Write a program that can multiply 2 numbers provided by the user without using the * operator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = 0

for i in range(abs(b)):
    result += a

# handle negative numbers
if b < 0:
    result = -result

print("Result:", result)

#here abs is used before b because b can be negative then it will be impossible
