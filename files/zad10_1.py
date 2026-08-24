def read_pixels(filename: str) -> list[int]:
    pixels = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            numbers = line.strip().split()

            for num in numbers:
                pixels.append(int(num))

    return pixels



def save_result(filename: str, darkest: int, brightest: int) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write("10.1\n")
        file.write(f"{brightest} {darkest}\n")


def main() -> None:
    pixels = read_pixels("dane.txt")

    darkest = min(pixels)
    brightest = max(pixels)

    save_result("wyniki6.txt", darkest, brightest)


if __name__ == "__main__":
    main()