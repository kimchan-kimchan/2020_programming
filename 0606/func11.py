import math

def circle_area(radius):
    area=math.pi*(radius)**2
    return area

r=int(input("반지름:"))
print("반지름",r,"의 넓이:",circle_area(r))
