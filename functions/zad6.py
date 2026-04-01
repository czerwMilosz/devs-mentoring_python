from random import randint

def get_number_list():
    return [randint(1, 111) for _ in range(10)]

def filter_list(numbers:list[int]) -> list[int]:
    return [num for num in numbers if 10 <= num < 100]

def main():
    numbers = get_number_list()
    filtered = filter_list(numbers)
    print(filtered)

if __name__ == "__main__":
    main()