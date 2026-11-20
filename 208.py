#Implement the Josephus problem.
#n people standing in a circle, every k-th person is eliminated.
#Return the safe position (1-indexed).
#Example: n=7, k=3 -> safe position 4

def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + k - 1) % n + 1

n = int(input("Enter number of people (n): "))
k = int(input("Every k-th person eliminated: "))
print(f"Safe position: {josephus(n, k)}")