#Write a program that will tell the number of dogs and chicken are there when 
#the user will provide the value of total heads and legs.
heads = int(input("Enter total heads: "))
legs = int(input("Enter total legs: "))

dogs = (legs - 2 * heads) // 2
chickens = heads - dogs

# Check validity
if dogs < 0 or chickens < 0 or (2*chickens + 4*dogs != legs):
    print("Invalid input")
else:
    print("Dogs:", dogs)
    print("Chickens:", chickens)


#chicken(less legs animal) will be taken first.