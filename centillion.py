import math
def Circle_area(radius):
    return math.pi * radius**2
try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        print("Error: Radius cannot be negative.")
    else:   
        area = Circle_area(radius)
        print(f"Area of the circle with radius {radius} is: {area:.2f}")
except ValueError:
    print("Error:Enter a valid number")