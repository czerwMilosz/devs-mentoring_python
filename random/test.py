class Point:
    x: float = 5
    y: float = 10

    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         print("Tworze obiekt")
    #         cls._instance = super().__new__(cls)
    #     return cls._instance
        #singletone ^
    #todo poczytac o tym ^
        # oba sa konstruktorami
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Przypisalem x, y")

    def __repr__(self):
        return f"Point(x = {self.x}, y = {self.y})"
    # str dziedziczy z repra jezeli nie jest nadpisany

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __gt__(self, other):
        return self.x > other.x

    def __lt__(self, other):
        return self.x < other.x

from dataclasses import dataclass
@dataclass(frozen = True, order=True)
class SuperPoint:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = SuperPoint(5, 6)
p4 = SuperPoint(7, 8)
print(p3)
print(p4)
print(p4 < p3)
print(id(p1) == id(p2))
print(id(p1))
print(p1 + p2)
print(p1 > p2)
print(p1 < p2)
print(Point(1, 2).x)
print(Point.x)
print(Point(1, 2))
print(repr(Point(1, 2)))

