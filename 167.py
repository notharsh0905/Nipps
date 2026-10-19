#Implement a function to traverse a matrix in spiral order.
#Given an m x n matrix, return all elements of the matrix in spiral order.
#Example: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix = []
print("Enter matrix rows (space-separated numbers per row, enter 'done' when finished):")
while True:
    row = input()
    if row == 'done':
        break
    matrix.append(list(map(int, row.split())))

if not matrix:
    result = []
else:
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Traverse up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

print("Spiral order:", result)