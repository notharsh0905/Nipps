#Implement a function to reverse an integer.
#Assume the environment can only store integers within the 32-bit signed integer range: [-2^31, 2^31 - 1].
#Return 0 when the reversed integer overflows.

def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = int(str(x)[::-1])
    result = sign * reversed_num
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

num = int(input("Enter an integer: "))
print(f"Reversed: {reverse_integer(num)}")