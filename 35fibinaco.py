#Print the first 20 numbers of a Fibonacci series
a = 0
b = 1

for i in range(20):
    print(a)
    next_num = a + b
    a = b
    b = next_num