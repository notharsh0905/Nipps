#User will provide 2 numbers you have to find the LCM of those 2 numbers
a = int(input())
b = int(input())

lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM is:", lcm)
        break
    lcm += 1