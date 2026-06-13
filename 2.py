#Write a program that will convert celsius value to fahrenheit
print("Choose conversion:")
print("1:Cal to far")
print("2:far to cal")

choice=int(input("Choose 1 or 2."))
temp = float(input("Enter the value "))

if choice==1:
    result=(temp * 9/5) +32
    print("temp in far is: ", result)

elif choice == 2:
    result = (temp - 32) * 5/9
    print("Temperature in Celsius is: ", result)

else:
    print("Invalid choice")


