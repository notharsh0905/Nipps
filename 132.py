#Implement a function to convert a decimal number to binary representation.
#Example: 10 -> "1010", 25 -> "11001"

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

num = int(input("Enter a decimal number: "))
print(f"Binary: {decimal_to_binary(num)}")