from random import randint, sample

def generate_random_number() -> int:
    return randint(5, 120)

def generate_set_of_random_numbers(count:int = 15) -> set[int]:
    numbers = set()
    while len(numbers) < count:
        numbers.add(generate_random_number())
    return numbers

def generate_set_of_random_numbers_v2(count:int = 15) -> set[int]:
    return set(sample(range(1, 121), count))

def generate_set_of_random_numbers_v3(count:int = 15) -> set[int]:
    return {generate_random_number() for _ in range(count)} # nie ma gwarancji 15 liczb w zbiorze

def remove_even_numbers(numbers:set[int]) -> set[int]:
    return {n for n in numbers if n % 2 != 0}

def main():
    numbers = generate_set_of_random_numbers_v2()
    odd_numbers = remove_even_numbers(numbers)
    print(f"All numbers: {numbers}")
    print(f"Odd numbers: {odd_numbers}")

if __name__ == "__main__":
    main()
