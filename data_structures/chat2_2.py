# 2. Policz wystąpienia słów
from collections import Counter
TEXT = "apple banana apple orange banana apple"

def count_words(text: str) -> dict[str, int]:
    """Returns a dictionary with word frequencies in the given text."""
    words = text.split()
    return Counter(words)

def count_words_v2(text: str) -> dict[str, int]:
    counter = {}
    words = text.split()
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

def main():
    print(count_words(TEXT))
    print(count_words_v2(TEXT))

if __name__ == '__main__':
    main()