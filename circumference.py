import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    try:
        r = float(input("Enter the radius of the circle").strip())
        if r < 0:
            raise ValueError("Radius cannot be negative.")
        circle = Circle(r)
        print(f"Area of the circle{circle.area():.2f}")
        print(f"Perimeter of the circle{circle.perimeter():.2f}")
    except ValueError as e:
        print("Error", e)

if __name__ == "__main__":
    main()
