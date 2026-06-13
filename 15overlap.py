#Overlapping rectangles
#Given two rectangles, find if the given two rectangles overlap or not.
#A rectangle is denoted by providing the x and y coordinates of two points:
#the left top corner and the right bottom corner of the rectangle. 
#Two rectangles sharing a side are considered overlapping. 
#(L1 and R1 are the extreme points of the first rectangle 
#and L2 and R2 are the extreme points of the second rectangle).

# Rectangle 1
x1, y1 = map(int, input("Enter L1 (x y): ").split())
x2, y2 = map(int, input("Enter R1 (x y): ").split())

# Rectangle 2
x3, y3 = map(int, input("Enter L2 (x y): ").split())
x4, y4 = map(int, input("Enter R2 (x y): ").split())

# Check no overlap conditions
if x2 < x3 or x4 < x1 or y2 > y3 or y4 > y1:
    print("Rectangles do NOT overlap")
else:
    print("Rectangles overlap")

#ya to ek(dusra b ho sakta) rec dusre k upper hoga ya toh niche 
#matlab ki overlap na hone hi ki condition nikaal lo  