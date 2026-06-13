#Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), 
#and tax(if salary is between 5-10lakh –10%),(11-20lakh –20%),(20< – 30%)(0-1lakh print k).
salary = float(input("Enter salary: "))

# Special case
if salary <= 100000:
    print("k")
else:
    # Deductions
    deduction = salary * 0.18

    # Tax calculation
    if 500000 <= salary <= 1000000:
        tax = salary * 0.10
    elif 1100000 <= salary <= 2000000:
        tax = salary * 0.20
    elif salary > 2000000:
        tax = salary * 0.30
    else:
        tax = 0

    in_hand = salary - deduction - tax

    print("In-hand salary is:", in_hand)