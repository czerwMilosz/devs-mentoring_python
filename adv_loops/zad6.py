NUMBER = 1235555

def split_number(number: int) -> list[int]:
    """Splits an integer into a list of its digits."""
    return [int(n) for n in str(number)]

def count_digits(digits: list) -> dict[int, int]:
    """Counts how many times each digit appears in the list."""
    digit_counter = {}
    for digit in digits:
        digit_counter[digit] = digit_counter.get(digit, 0) + 1
    return digit_counter

def main():
    digits = split_number(NUMBER)
    digit_counter = count_digits(digits)
    for digit, count in digit_counter.items():
        print(f"{digit}: {count}")


if __name__ == "__main__":
    main()