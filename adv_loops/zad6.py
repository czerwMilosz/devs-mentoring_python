from collections import Counter
import datetime
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
    # digits = split_number(NUMBER)
    # digit_counter = count_digits(digits)
    # for digit, count in digit_counter.items():
    #     print(f"{digit}: {count}")
    text_number = str(NUMBER)
    print(dict(Counter(text_number)))
    print({d: text_number.count(d) for d in set(text_number)})
    print({k:v for k,v in {str(d): text_number.count(str(d)) for d in range(10)}.items() if v != 0})
    name = "Jan"
    age = 20
    a = 5
    b = 3
    pi = 3.1415926535
    n = 1000000
    m = 255
    c = 0.314
    now = datetime.datetime.now()
    print(f"my name is {name=} and im {age} years old")
    print(f"{a} + {b} = {a+b}")
    print(f"{a + b =}")
    print(f"{pi:.2f}")
    print(f"{pi:<15} {n:_}")
    print(f"{b:15}")
    print(f"{c:.2%}")
    print(f"{m:b}")
    print(f"{m:o}")
    print(f"{m:x}")
    print(f"{m:X}")
    print(f"{now:%Y-%m-%d}")

    #zrobic tabelke z jsona



if __name__ == "__main__":
    main()