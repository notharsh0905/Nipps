#Implement the Tower of Hanoi problem.
#Move n disks from source peg to target peg using auxiliary peg.
#Print each move.
#Example: n=3 moves: 1->3, 1->2, 3->2, 1->3

def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, source, target)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'B', 'C')