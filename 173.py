#Implement a function to find the maximum area of water that can be contained between two lines.
#Given n non-negative integers where each represents a point at coordinate (i, height[i]),
#find two lines that together with the x-axis form a container that holds the most water.
#Example: [1,8,6,2,5,4,8,3,7] -> 49

def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

height = list(map(int, input("Enter heights separated by space: ").split()))
print(f"Maximum water area: {max_area(height)}")