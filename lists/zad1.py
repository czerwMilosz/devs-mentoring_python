from string import punctuation

TEXT = ("Napisz program, który wczytuje dowolne zdanie. "
        "Usuń znaki interpunkcyjne, następnie:")

def remove_punctuation(text):
    return "".join(l for l in text if l not in punctuation)


def reverse_words(text):
    text_list = text.split()
    return text_list[::-1]

def main():
    clean_text = remove_punctuation(TEXT)
    print(reverse_words(clean_text))

if __name__ == "__main__":
    main()