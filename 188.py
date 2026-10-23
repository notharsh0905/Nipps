#Implement a function to calculate compound interest.
#Given principal amount, annual interest rate, time in years, and number of times interest applied per year.
#Formula: A = P(1 + r/n)^(nt)
#Example: P=1000, r=5%, t=10, n=1 -> A=1647.01

def compound_interest(P, r, t, n):
    r = r / 100
    A = P * (1 + r / n) ** (n * t)
    return round(A, 2)

P = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time in years: "))
n = float(input("Enter number of times interest applied per year: "))
A = compound_interest(P, r, t, n)
print(f"Amount after {t} years: {A}")