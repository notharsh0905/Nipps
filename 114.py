#Demonstrate try-except-finally for error handling when dividing two numbers.
#Handle ZeroDivisionError and print finally block always executes.

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter valid integers")
finally:
    print("Execution complete")