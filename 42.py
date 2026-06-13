total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break
        
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
else:
    average = 0

print("Sum:", total_sum)
print("Average:", average)   