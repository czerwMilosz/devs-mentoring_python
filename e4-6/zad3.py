def get_user_numbers() -> list[float]:
    numbers = []
    while len(numbers) < 10:
        try:
            number = float(input("Enter a number: "))
            numbers.append(number)
        except ValueError:
            print("Please enter a number")
    return numbers

def get_even_numbers(numbers: list[float]) -> list[float]:
    return [n for n in numbers if n % 2 == 0]


def main():
    numbers = get_user_numbers()
    even_numbers = get_even_numbers(numbers)
    print(even_numbers)

if __name__ == "__main__":
    main()


