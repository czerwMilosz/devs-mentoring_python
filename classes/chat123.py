class Dog:
    def __init__(self, name: str, age: int):
        if age < 0:
            raise ValueError("Age must be >= 0")
        self.name = name
        self.age = age

    def bark(self) -> str:
        return f"Woof! My name is {self.name}"

    def have_birthday(self) -> None:
        self.age += 1


def main():
    dog = Dog("Now I am become Death, the Destroyer of Worlds", 10)
    print(dog.bark())
    print(f"Age before birthday: {dog.age}")
    dog.have_birthday()
    print(f"Age after birthday: {dog.age}")
    reksio = Dog("Reksio", -5)
    print(reksio.bark())

if __name__ == "__main__":
    main()
