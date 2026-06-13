#Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit
while True:
    print("\nMenu:")
    print("1. cm to ft")
    print("2. km to miles")
    print("3. usd to inr")
    print("4. exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cm = float(input("Enter value in cm: "))
        ft = cm / 30.48
        print("Feet:", ft)

    elif choice == 2:
        km = float(input("Enter value in km: "))
        miles = km * 0.621371
        print("Miles:", miles)

    elif choice == 3:
        usd = float(input("Enter USD: "))
        inr = usd * 83   # approx rate
        print("INR:", inr)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")


#yha p loop baar chal rha h (while true) ki wjh s