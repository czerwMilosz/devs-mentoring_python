from typing import TypeVar, Generic, Type

T = TypeVar("T") # typ ciasta
S = TypeVar("S") # dekoracja
U = TypeVar("U") # sposob podania


class CheeseCake:
    def __str__(self):
        return "Cheese cake"

class AppleCake:
    def __str__(self):
        return "Apple cake"

class Cream:
    def __str__(self):
        return "Cream topping"

class Fruit:
    def __str__(self):
        return "Fruit topping"

class Plate:
    def __str__(self):
        return "on a plate"

class Box:
    def __str__(self):
        return "in a box"

class BakeryBase(Generic[T]):
    def __init__(self, cake: T):
        self.cake = cake

class Decoratable(Generic[S]):
    def __init__(self, decoration: S):
        self.decoration = decoration

class DecoratedCake(BakeryBase[T], Decoratable[S]):
    def __init__(self, cake: T, decoration: S):
        BakeryBase.__init__(self, cake)
        Decoratable.__init__(self, decoration)

    def describe(self):
        return f"{self.cake} with {self.decoration}"

class CakeOrder(DecoratedCake[T, S], Generic[T, S, U]):
    def __init__(self, cake: T, decoration: S, serving: U):
        super().__init__(cake, decoration)
        self.serving = serving

    def full_description(self):
        return f"{self.cake} with {self.decoration} {self.serving}"

def main():
    cake_1 = First[CheeseCake, Cream](CheeseCake(), Cream())
    cake_2 = First[AppleCake, Cream](AppleCake(), Cream())
    cake_3 = Second[AppleCake, Cream, Plate](AppleCake(), Cream(), Plate())
    print(cake_1.describe())
    print(cake_2.describe())
    print(cake_3.full_description())

if __name__ == "__main__":
    main()
#todo przerobic generyk
#todo abc poczytac abstract base class
#todo protocols
#todo slots w klasach
