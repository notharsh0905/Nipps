#User will input (3ages).Find the oldest one

print("enter the ages of three people")
age1= int(input())
age2= int(input())
age3= int(input())
if age1>age2 and age1>age3:
    print("age1 is the greatest")
elif age2>age1 and age2>age3:
    print("age2 is the greatest")
elif age3>age1 and age3>age2:
    print("age3 is the greatest")
else:    print("all ages are equal")