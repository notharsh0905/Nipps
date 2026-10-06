#Implement a function to check if a year is a leap year using a concise one-liner.
#Leap year rules: divisible by 4, except for centuries which must be divisible by 400.

year = int(input("Enter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is a leap year: {is_leap}")