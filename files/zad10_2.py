def count_rows_to_remove(filename: str) -> int:
    rows_to_remove = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            numbers = line.strip().split()
            row = []

            for num in numbers:
                row.append(int(num))

            if row != row[::-1]:
                rows_to_remove += 1

    return rows_to_remove


def save_result(filename: str, result: int) -> None:
    with open(filename, "a", encoding="utf-8") as file:
        file.write("10.2\n")
        file.write(f"{result}\n")


def main() -> None:
    result = count_rows_to_remove("dane.txt")
    save_result("wyniki6.txt", result)


if __name__ == "__main__":
    main()