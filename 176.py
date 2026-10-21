#Implement a function to determine if a integer is a power of four.
#Use the property that a power of four has exactly one bit set in an even position.
#Example: 16 -> True, 5 -> False, 1 -> True (4^0)

def is_power_of_four(n):
    # A power of four must be a power of two and the set bit must be in an even position
    # 0x55555555 has bits set at even positions (0, 2, 4, ...)
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

num = int(input("Enter a positive integer: "))
print(f"{num} is a power of four: {is_power_of_four(num)}")