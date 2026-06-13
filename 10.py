#Write a program that will take user input of cost price 
#and selling price and determines whether its a loss or a profit
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit of:", sp - cp)

elif sp < cp:
    print("Loss of:", cp - sp)

else:
    print("No profit, no loss")