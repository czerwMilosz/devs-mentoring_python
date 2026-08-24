def remove_duplicates(line: str) -> str:
    words = line.split()
    result = []
    previous_word = ""

    for word in words:
        if word != previous_word:
            result.append(word)
        previous_word = word

    return " ".join(result)


def process_file(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = [remove_duplicates(line) for line in lines]

    with open(output_file, "w", encoding="utf-8") as file:
        for line in cleaned_lines:
            file.write(line + "\n")


def main():
    process_file("przyklad.txt", "nowy_plik.txt")


if __name__ == "__main__":
    main()