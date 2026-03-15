from pydantic import BaseModel, Field, ValidationError

DICTIONARY = {
    "python": "A popular programming language known for its readability.",
    "algorithm": "A step-by-step procedure used to solve a problem."
}

class WordEntry(BaseModel):
    word: str = Field(..., min_length=1)
    definition: str = Field(..., min_length=1)

def add_word(dictionary):
    while True:
        try:
            word = input("Enter word: ").strip().lower()
            definition = input("Enter definition: ").strip()
            entry = WordEntry(word=word, definition=definition)
            dictionary[entry.word] = entry.definition
            print(f"{entry.word} has been added.")
            return
        except ValidationError:
            print("Word and definition cannot be empty.")

def find_word(dictionary: dict):
    while True:
        word = input("Enter word: ").strip().lower()

        if not word:
            print("Word cannot be empty.")
            continue

        if word in dictionary:
            print(dictionary[word])
            return
        else:
            print("Word not found.")
            return



def delete_word(dictionary: dict):
    while True:
        word = input("Enter word: ").strip().lower()

        if not word:
            print("Word cannot be empty.")
            continue

        if word in dictionary:
            del dictionary[word]
            print(f"{word} has been deleted.")
            return
        else:
            print("Word not found.")
            return

def show_dictionary(dictionary: dict):
    for word, definition in dictionary.items():
        print(f"{word}: {definition}")
    return

def show_menu():
    return (
        "\n1. Add a word with its definition"
        "\n2. Find the definition of a word"
        "\n3. Remove a word and its definition from the dictionary"
        "\n4. Show dictionary"
        "\n5. Exit the program"
    )


def main():
    while True:
        print(show_menu())
        choice = input("Enter choice: ")
        if choice == "1":
            add_word(DICTIONARY)
        elif choice == "2":
            find_word(DICTIONARY)
        elif choice == "3":
            delete_word(DICTIONARY)
        elif choice == "4":
            show_dictionary(DICTIONARY)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

