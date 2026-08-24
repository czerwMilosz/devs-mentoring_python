class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        if length <= 0:
            raise ValueError("Square length must be above 0")
        self.length = length

    def area(self):
        return self.length ** 2

    def __repr__(self):
        return f"Square(length={self.length})"

def main():
    square = Square(5)
    print(square.area())

if __name__ == "__main__":
    main()