#Given a year, determine if it is a leap year.
#Leap year rules: divisible by 4, except for centuries which must be divisible by 400.
#Example: 2020 -> True, 1900 -> False, 2000 -> True

year = int(input("Enter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is a leap year: {is_leap}")