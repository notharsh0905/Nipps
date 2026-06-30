# Take temperature input from the user as a float
celsius = float(input("Enter temperature in Celsius: "))

# Apply the mathematical conversion formula
fahrenheit = (celsius * 1.8) + 32

# Display the converted result rounded to 2 decimal places
print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
