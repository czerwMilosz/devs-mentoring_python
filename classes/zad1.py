class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")


def main():
    student = Student("Tomasz", 22)
    student.print_info()

if __name__ == "__main__":
    main()