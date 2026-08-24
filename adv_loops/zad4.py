def generate_numbers_with_nested_loops() -> None:
    """
        Generates and prints all 4-digit numbers using nested loops.

        Each loop represents a digit:
        - thousands (1–9)
        - hundreds (0–9)
        - tens (0–9)
        - ones (0–9)
    """
    for i in range(1,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    print(str(i) + str(j) + str(k) + str(l))


def generate_numbers_with_range() -> None:
    """
        Generates and prints all 4-digit numbers using a single loop.
    """
    for i in range(1000, 10000):
        print(i)


def main():
    generate_numbers_with_nested_loops()
    generate_numbers_with_range()


if __name__ == "__main__":
    main()
