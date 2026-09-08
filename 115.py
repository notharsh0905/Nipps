#Measure execution time of a simple loop using time module.
#Calculate sum of first n natural numbers and print time taken.

import time
n = int(input("Enter n: "))
start = time.time()
total = sum(range(1, n + 1))
end = time.time()
print(f"Sum: {total}, Time: {(end - start)*1000:.2f}ms")