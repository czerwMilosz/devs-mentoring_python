class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError(f"Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

def main():
    rectangle = Rectangle(width=5, height=10)
    print(rectangle)
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")

if __name__ == "__main__":
    main()