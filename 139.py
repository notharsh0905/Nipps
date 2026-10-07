#Implement a function to check if two rectangles overlap.
#Each rectangle is defined by (x1, y1, x2, y2) where (x1, y1) is bottom-left and (x2, y2) is top-right.
#Rectangles overlap if there is any common area.
#Example: rect1 = (0, 0, 2, 2), rect2 = (1, 1, 3, 3) -> True (overlap)

x1, y1, x2, y2 = map(int, input("Enter rect1 (x1 y1 x2 y2): ").split())
x3, y3, x4, y4 = map(int, input("Enter rect2 (x1 y1 x2 y2): ").split())

# No overlap if one rectangle is completely to the left, right, above, or below the other
overlap = not (x2 <= x3 or x4 <= x2 or y4 <= y1 or y3 <= y1)
print(f"Rectangles overlap: {overlap}")