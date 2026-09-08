#Process a CSV-like input string and compute the average of numeric columns.
#Example input: "1,2,3|4,5,6" -> row averages: 2.0, 5.0

data = input("Enter CSV data (rows separated by |): ")
rows = data.split("|")
for row in rows:
    nums = list(map(float, row.split(",")))
    avg = sum(nums) / len(nums) if nums else 0
    print(f"Row average: {avg:.2f}")