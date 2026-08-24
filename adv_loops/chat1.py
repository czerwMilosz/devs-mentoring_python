TEXT = "bAnana"

def count_letters(text: str) -> dict:
    letters = {}
    for letter in text.lower():
        letters[letter] = letters.get(letter,0) + 1
    return letters

def main():
    letters_count = count_letters(TEXT)
    for letter, count in letters_count.items():
        print(f"{letter}: {count}")

if __name__ == "__main__":
    main()