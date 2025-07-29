import math

# Function to calculate area of a circle
def area_circle(radius):
    return math.pi * radius ** 2

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Main program
if __name__ == "__main__":
    # Circle
    r = float(input("Enter the radius of the circle: "))
    print(f"Area of Circle: {area_circle(r):.2f} sq units")

    # Rectangle
    l = float(input("\nEnter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    print(f"Area of Rectangle: {area_rectangle(l, w):.2f} sq units")

    # Triangle
    b = float(input("\nEnter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))  # <- fixed line here
    print(f"Area of Triangle: {area_triangle(b, h):.2f} sq units")
