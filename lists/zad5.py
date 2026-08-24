from string import punctuation

TEXT = ("Napisz program, który wczytuje dowolne zdanie. "
        "Usuń znaki interpunkcyjne "
        "z A Na "
        "a następnie korzystając z metod operujących na listach, program powinien: "
        "Pod pod")

def remove_punctuation(text:str) -> list:
    """Removes punctuation from text and returns a list of words."""
    cleaned_text = "".join(word for word in text if word not in punctuation)
    return cleaned_text.split()

def get_words_amount(text_list:list) -> int:
    """Returns the number of words in the list."""
    return len(text_list)

def get_capital_words(text_list:list) -> list:
    """Returns a list of words starting with a capital letter."""
    return [word for word in text_list if word[0].isupper()]

def find_words_with_indices(text_list:list) -> dict:
    """Finds selected words and returns their indices grouped by word."""
    words = ("a", "z", "na", "pod")
    found_words = {}
    for index, word in enumerate(text_list):
        normalized_word = word.lower()

        if normalized_word in words:
            if normalized_word in found_words:
                found_words[normalized_word].append(index)
            else:
                found_words[normalized_word] = [index]
    return found_words

def get_alphabetical_order(text_list:list) -> list:
    """Returns words sorted alphabetically in lowercase."""
    alphabetical_order = [word.lower() for word in text_list]
    alphabetical_order.sort()
    return alphabetical_order

def main():
    cleaned_text = remove_punctuation(TEXT)
    words_amount = get_words_amount(cleaned_text)
    capital_words = get_capital_words(cleaned_text)
    words_indices = find_words_with_indices(cleaned_text)
    alphabetical_order = get_alphabetical_order(cleaned_text)

    print(f"Length of text: {words_amount}")

    if capital_words:
        print(f"Capital words: {capital_words}")
    else:
        print("No capitalized words found.")

    if words_indices:
        print(f"Words from list indices: {words_indices}")
    else:
        print(f"No words from the list")

    print(f"Alphabetical order: {alphabetical_order}")

if __name__ == "__main__":
    main()